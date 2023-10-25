 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
#                                                                                                                          #
#   _/\/\/\/\/\________/\/\______/\/\/\/\/\/\____/\/\/\/\/\__________/\/\/\/\/\____/\/\/\/\______/\/\/\/\____/\/\_______   #
#   _/\/\____/\/\____/\/\/\/\________/\/\______/\/\________________/\/\__________/\/\____/\/\__/\/\____/\/\__/\/\_______   #
#   _/\/\/\/\/\____/\/\____/\/\______/\/\________/\/\/\/\__________/\/\__________/\/\____/\/\__/\/\____/\/\__/\/\_______   #
#   _/\/\__________/\/\/\/\/\/\______/\/\______________/\/\__/\/\__/\/\__________/\/\____/\/\__/\/\____/\/\__/\/\_______   #
#   _/\/\__________/\/\____/\/\______/\/\______/\/\/\/\/\____/\/\____/\/\/\/\/\____/\/\/\/\______/\/\/\/\____/\/\/\/\/\_   #
#   ____________________________________________________________________________________________________________________   #
#   ___/\/\/\/\____/\/\____/\/\______/\/\______/\/\____/\/\__/\/\/\/\/\/\______/\/\/\/\/\______/\/\/\/\____/\/\/\/\/\/\_   #
#   _/\/\____/\/\__/\/\____/\/\____/\/\/\/\____/\/\/\__/\/\______/\/\__________/\/\____/\/\__/\/\____/\/\______/\/\_____   #
#   _/\/\____/\/\__/\/\____/\/\__/\/\____/\/\__/\/\/\/\/\/\______/\/\__________/\/\/\/\/\____/\/\____/\/\______/\/\_____   #
#   _/\/\__/\/\____/\/\____/\/\__/\/\/\/\/\/\__/\/\__/\/\/\______/\/\__________/\/\____/\/\__/\/\____/\/\______/\/\_____   #
#   ___/\/\/\/\/\____/\/\/\/\____/\/\____/\/\__/\/\____/\/\______/\/\__________/\/\/\/\/\______/\/\/\/\________/\/\_____   #
#                                                                                                                          #
#   WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.   #
#   ____________________________________________________________________________________________________________________   #
#   _______________________________________________               ____ _ ____ ______ ___________________________________   #
#   ________________________&&&%%@&%&,,(*___________  BUIDLED BY |    \ /    |      | __________________________________   #
#   __________________#/&@@&&@@&%(@@&&&@&&(#____________________ |  o  |  o  |      | __________________________________   #
#   ___ S'GETIT _____/&@@@@@&&&@@&@&%@&@&(@#@%&_________________ |   _/|     |_|  |_| __________________________________   #
#   _______________%&&&&@&@@@@%@@&%#@@@@@&%&@(((________________ |  |  |  _  | |  | ____________________________________   #
#   ______________&&@@@@&@@@@@@&@&&@@&#@@@#&@#&@#_______________ |__|  |__|__| |__| ____________________________________   #
#   _____________/@@@&@@@@@@@@&#&&&%@&@@&%&#@&&/@(_______________  _____ ____ ____  ______ ____  ____  ____  ___ _______   #
#   _____________(&@&@@@@&%%///////(%/(&%%#&&@&##@@_____________  / ___/     |    \|      |    |/    |/    |/   \ ______   #
#   _____________*@@&&&&&/////***********/&%#&@%%@______________ (   \_|  o  |  _  |      ||  ||  o  |   __|     | _____   #
#   ______________@@@&@@(&///********,,,,**&%#(&@#_______________ \__  |     |  |  |_|  |_||  ||     |  |  |  O  | _____   #
#   _______________@@&&@(////@#*****,@@,,,,&%@@%@________________ /  \ |  _  |  |  | |  |  |  ||  _  |  |_ |     | _____   #
#   _______________@&&&&////*//*/*,*,**,..,(%#@#_________________ \    |  |  |  |  | |  |  |  ||  |  |     |     | _____   #
#   _________________**//(///&&&&&&%%%(,...////___________________ \___|__|__|__|__| |__| |____|__|__|___,_|\___/ ______   #
#   ____ WAGMI _______@@@@(////*,,,,(/,,,.@&@%(___________________  ←← THIS GUY ________________________________________   #
#   ______________________@@////*****,,,@@#________________________ ____________________________________________________   #
#   ______________________*@,@@(//*_________________________________ This bot statistically arbitrages pairs on dYdX ___   #
#   ___________________________//**,.________________________________ by analyzing candlestick data, when it finds a ___   #
#   __________________________(/***,.__________ LFG00000 _____________ highly profitable / probable trade it employs ___   #
#   ______________________*@&///****,,*&&______________________________ the Kelly criterion to determine how much of ___   #
#   __________________*@@@@@@@@@@&&&%%%%%%%%&___________________________ ur bankroll should be invested 4 top profit ___   #
#   ______________#@@@@@@@@@@@@@@&&&&&%%%%#####%%*______________________________________________________________________   #
#                                                                                                                          #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
                                                                                                                                                                                                                                                       
 # IMPORT REQUIRED PARTS # # # # # # # # # # # # # # # # # # # o                                                           
#                                                                                                                           
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS, DAILY_DIVINATION
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message
from i_ching import divination
import time

#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # o  

 # DIVINATION # # # # # # # # # # # # # # # # # # # # # # # # o  
# 
if DAILY_DIVINATIONS:
    print(divination())
                                                                                                                                                                                                                                                      
 # START THE APP # # # # # # # # # # # # # # # # # # # # # # # # o o 
#                                                                                                                                                                                    
if __name__ == "__main__":
    
    # CONNECT TO CLIENT
    send_message("I'm awake")
   
    try:
        client = connect_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client... ", e)
        exit(1)                                                                                             
        #                                                                                                                           
         # # # # # # # # # # # # # # # # # # # # # # # # # # # o o o # format all sections like this, number of o = number of indent it ends on, atthe top it hows many indents it starts on, make visually debugging stupid python indent errors
                                                                                                                            
      # ABORT ALL POSITIONS # # # # # # # # # # # # # # # # # # #                                                           
     #   
    #                                                                                                                         
    if ABORT_ALL_POSITIONS :
        try:
            print("Closing all positions... ")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print(e)
            print("Error closing all positions... ", e)
            exit(1)  
            #
             #                                                                                                                           
              # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
                                                                                                                             
      # FIND COINT PAIR # # # # # # # # # # # # # # # # # # # # # # #                                                       
     #                                                                                                                           
    #
    if FIND_COINTEGRATED:

        # CONSTRUCT MARKET PRICES
        try:
            print("Give me like 5 mins and ill give you a dataframe of market prices... ")
            df_market_prices = construct_market_prices(client)
            print("Asking the I Ching ...")
            print(divination())
        except Exception as e:
            print(e)
            print("Error constructing market prices: ", e)
            exit(1)  

        # STORE COINTEGRATED PAIRS
        try:
            print("Storing cointegrated pairs... ")
            stores_result = store_cointegration_results(df_market_prices)
            if stores_result != "saved":
                
                print("Error saving cointegrated pairs.. ")
                exit(1) 
        except Exception as e:
            print(e)
            print("Error saving cointegrated pairs: ", e)
            exit(1)
            #
             #                                                                                                                           
              # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 
      # SET TO ALWAYS RUN TOGGLE # # # # # # # # # # # # # # # # # # # # # #
    #
    while True:

         # MANAGE OPEN TRADES # # # # # # # # # # # # # # # # # # # # # #
        #
        if MANAGE_EXITS:
            try:
                print("Reading crypto twitter to make sure trades we made aren't shit... ")
                print("Checking existing positions...")
                manage_trade_exits(client)
                print("I checked the positions")

            except Exception as e:
                print(e)
                print("Error managing exitting positions:", e)
                print("I honestly dont even know what i'm doing")
                exit(1)  
     #  
      #  
       #                                                                                                                           
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         
        
    # PLACE TRADES FOR OPENING POSITIONS # # # # # # # # # # # # # #
   #
        if PLACE_TRADES:
            try:
                print("Finding trading opportunities... ")
                print("Scrolling bird app for alpha...")
                print("Calling Degen Steve... ")
                print("Stevethen has blessed us with alpha... ")
                open_positions(client)

            except Exception as e:
                print(e)
                print("Error trading pairs:", e)
                print("Degen Dan said the markets are in a gulley! Have you thought about getting into AI?")
                exit(1)    
       #                                                                                                                           
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
