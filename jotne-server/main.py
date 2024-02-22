import requests
import json
import os 
import argparse
import pprint as pp

from pathlib import Path

# Functions
from login import get_token
from download import process_file
from upload import upload_file
import create_folder as cf

# CREDENTIALS = {
#         "group": "sdai-group",    # User group,Default parameter for All users
#         "user": "iti_spa",        # PLM User name
#         "pass": "gw7#jR9"         # PLM Password
#     }


PLM_URL = "https://treeads.jotne.com/EDMtruePLM"    
MODEL="Test"                                        # Project name
REPOSITORY="TruePLMprojectsRep"                     # project repository  
NODE='214748369471' #"214748369610"     


def get_arguments():

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--group", default="sdai-group", help="User group")
    parser.add_argument("--user", default="iti_spa", help="PLM User name")
    parser.add_argument("--password", default="gw7#jR9", help="PLM Password")
    
    parser.add_argument('--post', action="store_true", help='Create a POST request')
    parser.add_argument('--get', action="store_true", help='Create a GET request')
    parser.add_argument('--create-folder', action="store_true", help='Create a folder element in DB')

    parser.add_argument("--path", default="./images/goats_2_fr0050.jpg", help="Path of the image you want to upload")
    parser.add_argument("--search", default="goats_2_fr0000.jpg", help="Pattern you want to search ")
    parser.add_argument("--folderName", default="ODE_Test", help="Define the name of the new folder you want to create")

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
    create_folder = args.create_folder
    folder_name = args.folderName

    # log in to the server. Return tokenID 
    token = get_token(credentials) 

    if token:
        if post: # Upload files with POST request
            
            upload_file(PLM_URL, MODEL,REPOSITORY, NODE,token,image_path)
        
        elif get: # Download files with GET request

            # search_pattern =  "goats_2_fr0000.jpg"
            process_file(PLM_URL, MODEL, token, search_pattern,REPOSITORY)
        
        elif create_folder:
        
            # folder_name = 'ODE_Test'
            
            # Call get_root_breakdown_element to get instance_id. 
            # Instance id changes every time, so you must retrieve it in every log in 
            root_bd = cf.get_root_breakdown_element(PLM_URL,MODEL,token,REPOSITORY)
            # print(f'\nroot_bd: {root_bd}')

            if root_bd:                     
                print('The root bd element of the project: {}, and instance_id is: {}'.format(
                root_bd['root_bkdn_elem']['name'],
                root_bd['root_bkdn_elem']['instance_id']
                ))

            new_node = root_bd['root_bkdn_elem']['instance_id']
            # print(type(new_node))

            # Call create_new_bd_element to create a new folder for the Project="Test"
            new_folder = cf.create_new_bd_element(PLM_URL,MODEL,new_node,token,folder_name,REPOSITORY)
            # pp.pprint(new_folder)
            
            if new_folder:
                print(f'New folder: {folder_name} successfully created')

        else:
            raise ValueError("use correct argument")

