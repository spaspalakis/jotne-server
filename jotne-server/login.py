import requests

"""


This function attempts to authenticate with the server using provided credentials.
Upon successful login, the server issues a token ID in response.

"""

PLM_URL = "https://treeads.jotne.com/EDMtruePLM"    # change this to project speciic URL

def get_token(credentials):
    
    print('\n---- Try to Log In ----')

    get_token_url = PLM_URL + "/api/admin/token"      # API to get token

    try:
        print("\nPerforming request: " + get_token_url )
        response = requests.post(get_token_url , data=credentials, timeout=5.0)
        response.raise_for_status()

        if 'token' in response.json():
            token = response.json()['token']
            print(f"\nSuccessfully logged in. | token: {token}")
            return token
        else:
            print("Error: Token not found in the response.")
    except requests.exceptions.RequestException as e:
         print('Request failed {}\nError Message:  {}'.format(e, response.text))