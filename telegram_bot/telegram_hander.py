import telegram


def send_message(text="", access_token="", target_user_id=""):
    #access_token = config["Telegram"]["ACCESS_TOKEN"]
    bot = telegram.Bot(token=access_token)
    bot.send_message(chat_id= target_user_id, text= text, parse_mode=telegram.ParseMode.MARKDOWN)

if __name__ == '__main__':
    import os, configparser
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
    target_user_id = config["Telegram"]["target_user_id"]
    send_message("test message", access_token=access_token, target_user_id=target_user_id)

