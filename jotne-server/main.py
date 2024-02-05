import requests
import json
import os 
import argparse

from pathlib import Path

# Functions
from login import get_token
from download import process_file
from upload import upload_file

CREDENTIALS = {
        "group": "sdai-group",    # User group,Default parameter for All users
        "user": "iti_spa",        # PLM User name
        "pass": "gw7#jR9"         # PLM Password
    }


PLM_URL = "https://treeads.jotne.com/EDMtruePLM"    
MODEL="Test"                                        # Project name
REPOSITORY="TruePLMprojectsRep"                     # project repository  
NODE="214748369610"     


def get_arguments():

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--post', action="store_true", help='Create a POST request')
    parser.add_argument('--get', action="store_true", help='Create a GET request')
    
    return parser.parse_args()


if __name__ == "__main__":

    args = get_arguments()

    post = args.post
    get = args.get   

    token = get_token(CREDENTIALS) 
    
    if post: # Upload files with POST request
        upload_file(PLM_URL, MODEL,REPOSITORY, NODE,token)
    
    elif get: # Download files with GET request

        search_pattern =  "goats_2_fr0000.jpg"
        process_file(PLM_URL, MODEL, token, search_pattern,REPOSITORY)
    else:
        raise ValueError("use POST/GET argument")

