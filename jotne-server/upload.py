import requests
import os


def upload_file(PLM_URL, MODEL,REPOSITORY, NODE,token,image_path):
    
    print('\n---- Try to Upload file ----')

    filename = os.path.basename(image_path)
    
    file_to_upload = open(image_path, "rb") 

    data_param={
           'descr':f"{os.path.splitext(filename)[0]}",              # Description of the document
           'title':f"{filename}",                             # Title of the document
           'source':"urn:rdl:epm-std:Unknown",              # Source of the document
           'contentType':'urn:rdl:epm-std:Miscellaneous',   # Content type of the document
           'discipline':'urn:rdl:epm-std:Uncertain',        # Discipline of the document
           'projPhase':'urn:rdl:epm-std:0',                 # Project phase of the document
           'status':'urn:rdl:epm-std:Approved',             # Status of the document
           'editor':'iti_spa',                             # Login of person, who edited the document
           'resp':'iti_spa',                               # Login of person, who responsible for the document
           'rev':'iti_spa',                                # Login of person, who reviewed the document
           'app':'iti_spa',                                # Login of person, who approved the document
           'revMan':'iti_spa'}                             # Login of person, who is the release manager for the document


    #  ------   url ------------------------    ---- repo --------  -model- ---- node --  ----- token---
    # https://treeads.jotne.com/EDMtruePLM/api /TruePLMprojectsRep/ certh/  236223206090/ KCWHSXF54NYR6YPMLX
    url_upload_file=PLM_URL+"/api/dat"+"/"+REPOSITORY + "/" + MODEL + "/" + NODE + "/"+token

    try :
        response = requests.post(url_upload_file,files= {"file" : file_to_upload },data=data_param,timeout=5.0)
        print(f'\nPOST request: {url_upload_file}')
    
        response.raise_for_status()
    
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}\nError Message: {getattr(response, "text", "No response text available")}')
        return None

    # Check the response
    if response.status_code == 200:
        print("\nImage upload successful!")
        # print(response.json())  # Assuming the response is in JSON format
    else:
        print(f"\nImage upload failed. Status code: {response.status_code}")
        print(response.text)