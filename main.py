from FTX_script.lending import update_lending, lending_info_by_time
from telegram_bot.telegram_hander import send_message
from datetime import datetime
import configparser, os

config_filename = "config.ini"
# Obtain the root path
scrpit_path = os.path.abspath(__file__)
root_path = os.path.dirname(scrpit_path)
# Config path
config_path = os.path.join(root_path, config_filename)
# Obtain all config data
config = configparser.ConfigParser()
config.read(config_path)
API_KEY= config["FTX"]["API_KEY"]
API_SECRET= config["FTX"]["API_SECRET"]
coins_list = config["FTX"]["coins"].split(',')
coins_hold = {coin_detail.split(",")[0]: float(coin_detail.split(",")[1]) for coin_detail in config["FTX"]["coins_hold"].split(';')}
sub_account= config["FTX"]["sub_account"]

access_token = config["Telegram"]["ACCESS_TOKEN"]
target_user_id = config["Telegram"]["target_user_id"]


if __name__ == '__main__':
    now = datetime.now()
    currect_timestamp = datetime.timestamp(now)
    msg = ""
    try:
        msg+= update_lending(API_KEY=API_KEY, API_SECRET=API_SECRET, coins_list=coins_list, coins_hold= coins_hold, sub_account= sub_account)
    
    except:
        pass

    try:
        msg+= lending_info_by_time(API_KEY=API_KEY, API_SECRET=API_SECRET, coins_list=coins_list, start_time=0, end_time= currect_timestamp, sub_account= sub_account)
    except:
        pass
    print (msg)
    send_message(text= msg, access_token=access_token, target_user_id=target_user_id)
    # Obatin the current time for logging
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Script run @", current_time)
