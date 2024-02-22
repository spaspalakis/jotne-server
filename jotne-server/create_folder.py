"""
This part of the code is copied from this file: ~./TREEADS/server/REST_API_Examples_4.0.html

1. First we call API (Section 3):
    For retrieving all projects info with funtion get_root_breakdown_element()
    We get the name and the instance id of project and use them to create a new folder

2. Call API (Section 5) to create new breakdown element.
"""

import requests




#####################  root_bd element infomration ######################


def get_root_breakdown_element(PLM_URL,model,token,repository):

    print('\n---- Retrieve Project Info ----')

    url_get_root_bd_info = PLM_URL + "/api/bkd/" + repository + "/" + model + "/" + token
    print("\nPerforming request: " + url_get_root_bd_info)
    try:
        response= requests.get(url_get_root_bd_info, timeout=2.0)
        response.raise_for_status()
        return response.json() if response.ok else None
    except requests.exceptions.RequestException as e:
        print('Request failed {}\nError Message:  {}'.format(e, response.text))
        return None




#####################  Creating new BD element ###################### 


def create_new_bd_element(PLM_URL,model,node,token,folder_name,repository):
    
    print('\n---- Create folder ----')
    
    data_param={'act_timestamp':'',                                # Current time stamp
                'descr':'stores sensors data',                      # Description of element  
                'name':f'{folder_name}',                                   # Required Breakdown element name
                'nodeType':'urn:rdl:epm-std:Unit',                  # Node type
                'tmpl':''}                                          # Name of the breakdown template
    

    create_new_bd_ele_url=PLM_URL+"/api/bkd/create"+"/"+repository + "/" + model + "/" + f'{node}' + "/"+token
    print("\nPerforming request: " + create_new_bd_ele_url)
    try:
        response = requests.post(create_new_bd_ele_url,params=data_param,timeout=2.0)
        response.raise_for_status()
        return response.json() if response.ok else None
    except requests.exceptions.RequestException as e:
        print('Request failed {}\nError Message:  {}'.format(e, response.text))
        return None
    

