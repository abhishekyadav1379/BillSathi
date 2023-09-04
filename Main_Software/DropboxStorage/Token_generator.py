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

# Replace these with your actual values
client_id = "x8j8s1nw1mew1rz"
client_secret = "hwc5c841gd9gswf"
refresh_token = "fQJ_d-KEgTEAAAAAAAAAAYq0J7mTBqNQQOABxb7IKu3-fgcAzaiiH_Yr03NHjHJW"

new_access_token = get_new_access_token(client_id, client_secret, refresh_token)
if new_access_token:
    print(f"New Access Token: {new_access_token}")
