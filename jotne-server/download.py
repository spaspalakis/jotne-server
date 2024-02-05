import requests
from pathlib import Path


def make_request(url, params=None, is_json=True, method='get', headers=None, timeout=4.0):
    """
    Generic function to make HTTP requests and handle errors.
    """
    try:
        if method.lower() == 'get':
            response = requests.get(url, params=params,timeout=timeout)
        else:
            raise ValueError("Unsupported HTTP method")

        response.raise_for_status()

        return response.json() if is_json else response
    
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}\nError Message: {getattr(response, "text", "No response text available")}')
        return None


def process_file(base_url, model, token, search_pattern, repository):
    

    try:
        headers = {'Authorization': f'Bearer {token}'}  # Assuming token is used as a bearer token

        data_param = {
            'case_sens': 'no',
            'domains': '',
            'node': '',
            'page': '',
            'page_size': '',
            'pattern': search_pattern,
            'props': ''
        }

        # File quick search
        search_url = f"{base_url}/api/dat/q_search/{repository}/{model}/{token}"
        print(f'\nsearch_url: {search_url}')

        search_result = make_request(search_url, params=data_param, headers=headers)
        print(f'\ndoc_search_result: {search_result}')

        if not search_result:
            raise ValueError("Document search yielded no results")

        doc_info = search_result[0]['doc_info'] 
        # print(f'\ndoc_info: {doc_info}')
        doc_file_prop = {'name': doc_info['file_name'], 'ver': doc_info['instance_id']} # Returns the dict: {'name': 'goats_2_fr0012.jpg', 'ver': 214748376996}
        # print(f'\ndoc_file_prop: {doc_file_prop}')

        # Get file properties
        file_prop_url = f"{base_url}/api/dat/file/link/{repository}/{model}/{token}"
        file_properties = make_request(file_prop_url, params=doc_file_prop, headers=headers)
        print(f'\nfile_properties: {file_properties}')

        if not file_properties:
            raise ValueError("No file properties found for the document")

        # Download data
        download_url = f"{base_url}/api/dat/file/data/{file_properties['source']}/{file_properties['title']}/{token}"
        file_data = make_request(download_url, is_json=False, headers=headers)
        # print(f'\nfile_data: {file_data}')

        if not file_data:
            raise ValueError("File download failed")

        # Save the file
        folder_path ='download_folder'
        
        # Create the folder if it doesn't exist
        Path(folder_path).mkdir(parents=True, exist_ok=True)
        
        # Build the full path including the folder and file name
        required_filename = Path(folder_path) / Path(file_properties['title'])

        # required_filename = Path(file_properties['title'])
        required_filename.write_bytes(file_data.content) 
        print('\nFile downloaded and saved as:', required_filename)

    except Exception as e:
        print(f"An error occurred: {e}")
