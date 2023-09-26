import hashlib
import os 
import zipfile
import dropbox
import dropbox.files
import requests
import configparser
import shutil
from All_function import all_function

class DropboxSync:
    def __init__(self):
        fn = all_function()
        # self.account = fn.read_config_value("Account","id")
        self.account = fn.read_toml_section_value(r'Main_Software\setting.toml',"Account","id")
        # self.account = user_id
        local_path = "./Main_Software/DropboxStorage/local_files"
        # self.TOKEN =  self.read_config_value("Cred", "access_token") 
        self.TOKEN = fn.read_toml_section_value(r'Main_Software\setting.toml',"Dropbox","access_token")
        self.dbx = dropbox.Dropbox(self.TOKEN)
        self.local_path = local_path
    
    def copy_file(self, source_path, destination_path):
        try:
            # Check if the source file exists
            if not os.path.isfile(source_path):
                print(f"Error: Source file '{source_path}' does not exist.")
                return

            # Check if the destination folder exists
            if not os.path.exists(destination_path):
                print(f"Error: Destination folder '{destination_path}' does not exist.")
                return

            # Get the filename from the source path
            filename = os.path.basename(source_path)
            # Create the complete destination path by joining folder path and filename
            destination_file_path = os.path.join(destination_path, filename)

            # Check if the destination file exists, and if it does, remove it
            if os.path.exists(destination_file_path):
                # print("I remove it")
                os.remove(destination_file_path)

            # Copy the file from source to destination
            shutil.copy2(source_path, destination_file_path)
            print(f"File '{filename}' copied successfully to '{destination_path}'.")

        except Exception as e:
            print(f"An error occurred: {e}")
            
    def read_config_value(self,section, key):
        file_path = "./Main_Software/DropboxStorage/cred.ini"
        config = configparser.ConfigParser()
        config.read(file_path)

        try:
            value = config.get(section, key)
            return value
        except configparser.NoSectionError:
            print(f"Section '{section}' does not exist in the config file.")
        except configparser.NoOptionError:
            print(f"Key '{key}' does not exist in the section '{section}'.")
        
    def store_config_value(self, section, key, value):
        file_path = "./Main_Software/DropboxStorage/cred.ini"
        config = configparser.ConfigParser()
        config.read(file_path)

        if not config.has_section(section):
            config.add_section(section)

        config.set(section, key, value)

        with open(file_path, 'w') as config_file:
            config.write(config_file)
            print(f"Value '{value}' stored successfully for key '{key}' in section '{section}'.")


    def get_new_access_token(self, client_id, client_secret, refresh_token):
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

    def token_checker(self):
        try:
            # Attempt to make a call to the API using the access token
            self.dbx.files_list_folder('')
            print("Token is valid.")
        except dropbox.exceptions.AuthError as e:
            print("Token is either expired or invalid.")
            client_id = self.read_config_value("Cred", "client_id")
            client_secret = self.read_config_value("Cred", "client_secret")
            refresh_token = self.read_config_value("Cred", "refresh_token")
            new_token = self.get_new_access_token(client_id, client_secret,refresh_token)
            # with open("./DropboxStorage/token.txt", "w") as f:
            #     f.write(new_token)
            self.store_config_value("Cred", "access_token", new_token)
            self.TOKEN = new_token
            self.dbx = dropbox.Dropbox(self.TOKEN)
        except dropbox.exceptions.DropboxException as e:
            print("An error occurred while checking the token:", e)

    # def upload_all_local_files(self):
    #     for file in os.listdir(self.local_path):
    #         with open(os.path.join(self.local_path, file), "rb") as f:
    #             data = f.read()
    #             self.dbx.files_upload(data,f"/{file}")

    def dropbox_content_hash(self, file):
        hash_chuck_size = 4 * 1024 * 1024
        with open(file, "rb") as f:
            block_hashes = bytes()
            while True:
                chunk = f.read(hash_chuck_size)
                if not chunk:
                    break
                block_hashes += hashlib.sha256(chunk).digest()
            return hashlib.sha256(block_hashes).hexdigest()
    
    def folder_exists(self, folder_name):
        try:
            # Check if the folder exists
            response = self.dbx.files_get_metadata(f"/{folder_name}")
            return True if isinstance(response, dropbox.files.FolderMetadata) else False
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path() and e.error.get_path().is_not_found():
                return False
            else:
                raise

    # account = "Mahendra2"
    def create_folder(self, folder_name):
        try:
            # Create a new folder with the given name
            self.dbx.files_create_folder(f"/{folder_name}")
        except Exception as e:
            print("An error occurred:", str(e))
            
    def upload_changed(self):
        try:
            self.token_checker()
            if not self.folder_exists(self.account):
                self.create_folder(self.account)
            # self.create_folder(self.account)
            self.copy_file("./Main_Software/Database/mahendra.db", "./Main_Software/DropboxStorage/local_files")
            cloud_files = {}
            entries = self.dbx.files_list_folder(f"/{self.account}").entries
            for entry in entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    cloud_files[entry.name] = entry.content_hash
    
            for file in os.listdir(self.local_path):
                if file in cloud_files.keys():
                    local_hash = self.dropbox_content_hash(os.path.join(self.local_path, file))
                    if local_hash != cloud_files[file]:
                        print("File changed ", file)
                        with open(os.path.join(self.local_path, file), "rb") as f:
                            data = f.read()
                            self.dbx.files_upload(data, f"/{self.account}/{file}", mode=dropbox.files.WriteMode("overwrite"))
                    else:
                        print("UNCHANGED ", file)
                else:
                    print("NEW FILE ", file)
                    with open(os.path.join(self.local_path, file), "rb") as f:
                        data = f.read()
                        self.dbx.files_upload(data, f"/{self.account}/{file}", mode=dropbox.files.WriteMode("overwrite"))
        except Exception as e:
            print("An error occurred:", str(e))
            
    def download_changed(self,download_folder, dropbox_folder):
        # download_folder = "./Main_Software/Download_files"
        # dropbox_folder = '/Mahendra'
        
        for entry in self.dbx.files_list_folder(dropbox_folder).entries:
            local_file_path = os.path.join(download_folder, entry.name)
            
            if os.path.exists(local_file_path):
                local_hash = self.dropbox_content_hash(local_file_path)
                if local_hash != entry.content_hash:
                    print("File changed:", entry.name)
                    self.dbx.files_download_to_file(local_file_path, f"/{entry.name}")
                else:
                    print("UNCHANGED:", entry.name)
            else:
                print("NEW FILE:", entry.name)
                self.dbx.files_download_zip_to_file(local_file_path, f"{dropbox_folder}/{entry.name}")
    
    def convert_bytes(self,bytes_value, to_unit='KB'):
        units = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
        byte_size = bytes_value / (1024 ** units[to_unit])
        return f"{byte_size:.2f} {to_unit}"

    def get_folder_size(self, folder_path):
        total_size = 0

        try:
            for entry in self.dbx.files_list_folder(folder_path).entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    total_size += entry.size
        except dropbox.exceptions.ApiError as e:
            print(f"Error accessing Dropbox: {e}")
        if total_size >0:
            return total_size
        return 0
    
    def extract_zip(self,zip_file_path, extract_to):
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Successfully extracted '{zip_file_path}' to '{extract_to}'.")
        except zipfile.BadZipFile:
            print(f"Error: '{zip_file_path}' is not a valid zip file.")
        except FileNotFoundError:
            print(f"Error: File '{zip_file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
               
    def list_files_in_folder(self,folder_path):
        # folder_path = ""
        try:
            # List files in the given folder
            result = self.dbx.files_list_folder(folder_path)

            for entry in result.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    print(f"File: {entry.name}")
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    print(f"Folder: {entry.name}")
        except dropbox.exceptions.ApiError as e:
            print(f"Error listing files: {e}")
            
    def get_local_folder_size(self,folder_path):
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)

        return total_size

    def delete_local_folder(self,folder_path):
        try:
            shutil.rmtree(folder_path)
            print("Folder deleted successfully.")
        except OSError as e:
            print(f"Error deleting the folder: {e}")
    def run_in_thread(self):
        dropbox_sync = DropboxSync()
        dropbox_sync.upload_changed()
        
fn = DropboxSync()        
# fn.download_changed("./Main_Software/Download_files","/Download")
# dropbox_sync = DropboxSync()
# dropbox_sync.list_files_in_folder("/Mahendra")
# dropbox_sync.file_info()
# ab = dropbox_sync.get_folder_size("/Mahendra")
# print(ab)
# dropbox_sync.download_changed()

# dropbox_sync.upload_changed()
