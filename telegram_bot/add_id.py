import configparser, requests, os

config_filename = "config.ini"
# Obtain the root path
scrpit_path = os.path.abspath(__file__)
root_path = os.path.dirname(os.path.dirname(scrpit_path))
# Config path
config_path = os.path.join(root_path, config_filename)
# Obtain all config data
config = configparser.ConfigParser()
config.read(config_path)
access_token = config["Telegram"]["ACCESS_TOKEN"]
target_user = config["Telegram"]["TARGET_USERNAME"]

def get_user_id(access_token= access_token, target_user= target_user):
    url = "https://api.telegram.org/bot{}/getUpdates".format(access_token)
    response = requests.get(url)
    response = response.json()
    for result in response["result"]:
        message_info = result["message"]["from"]
        username = message_info.get("username")
        if username == target_user:
            user_id = message_info.get("id")
            return user_id

if __name__ == '__main__':
    # add telegram id into config if it is not existing
    if config["Telegram"].get("TARGET_USER_ID", None) != None:
        print ("Telegram ID is already exit")
    else:
        user_id = get_user_id()
        config.set('Telegram','TARGET_USER_ID', str(user_id))
        with open(config_path, 'w') as newini:
            config.write(newini)
        print ("Successfully add Telegram ID")
