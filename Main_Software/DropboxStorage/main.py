import hashlib
import os 
import dropbox
import dropbox.files

import requests

def get_new_access_token(client_id, client_secret, refresh_token):
    url = "https://api.dropbox.com/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        response_data = response.json()
        new_access_token = response_data.get("access_token")
        return new_access_token
    else:
        print("Failed to get a new access token.")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

with open("./DropboxStorage/token.txt", "r") as f:
    TOKEN = f.read()

dbx = dropbox.Dropbox(TOKEN)

def token_checker():
    try:
        # Attempt to make a call to the API using the access token
        dbx.files_list_folder('')
        print("Token is valid and not expired.")
    except dropbox.exceptions.AuthError as e:
        print("Token is either expired or invalid.")
        new_token = get_new_access_token()
        with open("./DropboxStorage/token.txt", "w") as f:
            f.write(new_token)
        TOKEN = new_token
        dbx = dropbox.Dropbox(TOKEN)
    except dropbox.exceptions.DropboxException as e:
        print("An error occurred while checking the token:", e)
    
def upload_all_local_files():
    for file in os.listdir("./DropboxStorage/local_files"):
        with open(os.path.join("./DropboxStorage/local_files", file), "rb") as f:
            data = f.read()
            dbx.files_upload(data,f"/{file}")
        
def dropbox_content_hash(file):
    hash_chuck_size = 4 * 1024 * 1024
    with open(file, "rb") as f:
        block_hashes = bytes()
        while True:
            chunk = f.read(hash_chuck_size)
            if not chunk:
                break
            block_hashes += hashlib.sha256(chunk).digest()
        return hashlib.sha256(block_hashes).hexdigest()
        
        

# Assuming you have already initialized the Dropbox API instance 'dbx'

def upload_changed():
    cloud_files = {}
    # dbx = dropbox.Dropbox(TOKEN)
    entries = dbx.files_list_folder("").entries
    for entry in entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            cloud_files[entry.name] = entry.content_hash
            
    for file in os.listdir("./DropboxStorage/local_files"):
        if file in cloud_files.keys():
            local_hash = dropbox_content_hash(os.path.join("./DropboxStorage/local_files", file))
            if local_hash != cloud_files[file]:
                print("File changed ", file)
                with open(os.path.join("./DropboxStorage/local_files", file), "rb") as f:
                    data = f.read()
                    dbx.files_upload(data, f"/{file}", mode=dropbox.files.WriteMode("overwrite"))
            else:
                print("UNCHANGED ", file)
        else:
            print("NEW FILE ", file)
            with open(os.path.join("./DropboxStorage/local_files", file), "rb") as f:
                data = f.read()
                dbx.files_upload(data, f"/{file}", mode=dropbox.files.WriteMode("overwrite"))

# Call the function to execute the synchronization
upload_changed()

