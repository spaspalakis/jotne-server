import requests
import json
import os 
import argparse

from pathlib import Path

# Functions
from login import get_token
from download import process_file
from upload import upload_file

# CREDENTIALS = {
#         "group": "sdai-group",    # User group,Default parameter for All users
#         "user": "iti_spa",        # PLM User name
#         "pass": "gw7#jR9"         # PLM Password
#     }


PLM_URL = "https://treeads.jotne.com/EDMtruePLM"    
MODEL="Test"                                        # Project name
REPOSITORY="TruePLMprojectsRep"                     # project repository  
NODE="214748369610"     


def get_arguments():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--group", default="sdai-group", help="User group")
    parser.add_argument("--user", default="iti_spa", help="PLM User name")
    parser.add_argument("--password", default="gw7#jR9", help="PLM Password")
    
    parser.add_argument('--post', action="store_true", help='Create a POST request')
    parser.add_argument('--get', action="store_true", help='Create a GET request')

    parser.add_argument("--path", default="./images/goats_2_fr0050.jpg", help="Path of the image you want to upload")
    parser.add_argument("--search", default="goats_2_fr0000.jpg", help="Pattern you want to search ")

    return parser.parse_args()


if __name__ == "__main__":

    args = get_arguments()

    # Create dictionary for credentials
    credentials = {
        "group": args.group,
        "user": args.user,
        "pass": args.password
    }
    
    image_path = args.path
    search_pattern = args.search
    post = args.post
    get = args.get   

    # log in to the server. Return tokenID 
    token = get_token(credentials) 
    
    if post: # Upload files with POST request
        
        upload_file(PLM_URL, MODEL,REPOSITORY, NODE,token,image_path)
    
    elif get: # Download files with GET request

        # search_pattern =  "goats_2_fr0000.jpg"
        process_file(PLM_URL, MODEL, token, search_pattern,REPOSITORY)
    else:
        raise ValueError("use POST/GET argument")

