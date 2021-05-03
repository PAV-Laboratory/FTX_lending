from FTX_script.helper import helper
import configparser

lowest_rate = 0.000001

def update_lending(API_KEY="", API_SECRET="", coins_list=[], coins_hold={}, sub_account=None):
    msg = ""
    all_balance = helper.get_balance(API_KEY= API_KEY, API_SECRET= API_SECRET, sub_account= sub_account)
    for balance in all_balance:
        coin = balance["coin"]
        if coin not in coins_list:
            continue
        else:
            total_coin = balance["total"]
            # mins the holding
            total_coin = total_coin - coins_hold.get(coin, 0)
            response = helper.post_lending_offer(pair= coin, size= total_coin, rate= lowest_rate, API_KEY= API_KEY, API_SECRET=API_SECRET, sub_account= sub_account)
            if response == "success":
                msg += "Update {} lending amount to {}\n".format(coin, total_coin)
            else:
                print (response)
                msg += "Fail to lend {} becauase {}".format(coin, response["error"])
    return msg

def lending_info(API_KEY="", API_SECRET="", coins_list=[], sub_account= None):
    response = helper.get_lending_history(API_KEY= API_KEY, API_SECRET= API_SECRET, sub_account= sub_account)
    
    # create a dict for all coin
    coin_history = dict()
    for coin in coins_list:
        coin_history[coin] = []
    
    # store all coin info to dict
    for result in response:
        coin = result["coin"]
        if coin not in coins_list:
            continue
        else:
            coin_history[coin].append(result)
    
    msg = ""
    # coin message for each coin
    for coin in coins_list:
        #msg for last info
        msg += "{} info\n".format(coin)
        last_info = coin_history[coin][0]
        last_rate = last_info['rate']
        last_size = last_info['size']
        last_proceeds = last_info["proceeds"]
        msg += "last size: {}\tlast rate: {:.5f}%\tlast proceeds:{}\n".format(last_size, last_rate*100, last_proceeds)
        
        #msg for all info
        all_rate= []
        for coin_info in coin_history[coin]:
            all_rate.append(coin_info["rate"]+1)
        compound_rate = 1
        for rate in all_rate:
            compound_rate = compound_rate * rate
        compound_rate = (compound_rate - 1) *100
        msg += "compound rate: {:.5f}\n".format(compound_rate)

    return msg

def lending_info_by_time(API_KEY="", API_SECRET="", coins_list=[], start_time= 0, end_time= 0, sub_account= None): 
     response = helper.get_lending_history_by_time(API_KEY= API_KEY, API_SECRET= API_SECRET, start_time= start_time, end_time= end_time, sub_account= sub_account)
         
     # create a dict for all coin
     coin_history = dict()
     for coin in coins_list:
         coin_history[coin] = []
         
     # store all coin info to dict
     for result in response:
         coin = result["coin"]
         if coin not in coins_list:
             continue
         else:
             coin_history[coin].append(result)
     msg = ""
     # coin message for each coin
     for coin in coins_list:
         #msg for last info
         msg += "{} info\n".format(coin)
         last_info = coin_history[coin][0]
         last_rate = last_info['rate']
         last_size = last_info['size']
         last_proceeds = last_info["proceeds"]
         msg += "last size: {}\tlast rate(hourly): {:.5f}%\tlast rate(annual):{:.5f}%\tlast proceeds:{}\n".format(last_size, last_rate*100, last_rate*24*365*100, last_proceeds)
             
         #msg for all info
         all_rate= []
         for coin_info in coin_history[coin]:
             all_rate.append(coin_info["rate"]+1)
         compound_rate = 1 
         for rate in all_rate:
             compound_rate = compound_rate * rate
         compound_rate = (compound_rate - 1) *100
         average_rate = (sum(all_rate)-len(all_rate))/len(all_rate) * 100
         msg += "compound rate: {:.5f}%\n".format(compound_rate)
         msg += "Average rate: {:.5}%\n".format(average_rate)
         msg += "Expected compound rate(monthly): {:.5f}%\n".format((((average_rate/100)+1)**(24*30)-1)*100)


 
     return msg              

if __name__ == '__main__':
    pass
