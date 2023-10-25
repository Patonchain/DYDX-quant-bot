 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
#                                                                                                                          #
#           _______      ,-----.    ,---.   .--.   .-'''-. ,---------.    _____.  ,---.   .--.,---------.   .-'''-.        #
#          /   __  \   .'  .-,  '.  |    \  |  |  / _     \\          \ .'  __  \ |    \  |  |\          \ / _     \       #
#         | ,_/  \__) / ,-.|  \ _ \ |  ,  \ |  | (`' )/`--' `--.  ,---'/   '  \  \|  ,  \ |  | `--.  ,---'(`' )/`--'       #
#       ,-./  )      ;  \  '_ /  | :|  |\_ \|  |(_ o _).       |   \   |___|  /  ||  |\_ \|  |    |   \  (_ o _).          #
#       \  '_ '`)    |  _`,/ \ _/  ||  _( )_\  | (_,_). '.     :_ _:      _.-`   ||  _( )_\  |    :_ _:   (_,_). '.        #
#        > (_)  )  __: (  '\_/ \   ;| (_ o _)  |.---.  \  :    (_I_)   .'   _    || (_ o _)  |    (_I_)  .---.  \  :       #
#       (  .  .-'_/  )\ `"/  \  ) / |  (_,_)\  |\    `-'  |   (_(=)_)  |  _( )_  ||  (_,_)\  |   (_(=)_) \    `-'  |       #
#        `-'`-'     /  '. \_/``".'  |  |    |  | \       /     (_I_)   \ (_ o _) /|  |    |  |    (_I_)   \       /        #
#          `._____.'     '-----'    '--'    '--'  `-...-'      '---'    '.(_,_).' '--'    '--'    '---'    `-...-'         #
#   ____________________________________________________________________________________________________________________   #
#   PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS.COOL WWW.PATS   #
#                                                                                                                          #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
                                                                                                                            
 # IMPORT REQUIRED PARTS # # # # # # # # # # # # # # # # # # # #                                                           
#                                                                                                                           
from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET                                                               
from decouple import config                                                                                                 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # ACTIVATE MAINNET / GOERLI TESTNET # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                                          #
#                                                                                                                          #
#            .-')     ('-.            ('-.           .-') _          _   .-')              _ .-') _    ('-.                #
#           ( OO ). _(  OO)         _(  OO)         (  OO) )        ( '.( OO )_           ( (  OO) ) _(  OO)               #
#           (_)---\_(,------,--.    (,------.  .-----/     '._        ,--.   ,--..-'),-----.\     .'_(,------.             #
#           /    _ | |  .---|  |.-') |  .---' '  .--.|'--...__)       |   `.'   ( OO'  .-.  ,`'--..._)|  .---'             #
#           \  :` `. |  |   |  | OO )|  |     |  |('-'--.  .--'       |         /   |  | |  |  |  \  '|  |                 #
#            '..`''.(|  '--.|  |`-' (|  '--. /_) |OO  ) |  |          |  |'.'|  \_) |  |\|  |  |   ' (|  '--.              #
#           .-._)   \|  .--(|  '---.'|  .--' ||  |`-'|  |  |          |  |   |  | \ |  | |  |  |   / :|  .--'              #
#           \       /|  `---|      | |  `---(_'  '--'\  |  |          |  |   |  |  `'  '-'  |  '--'  /|  `---.             #
#            .-')-_' `-('-.-`-.-')-' .-')-_-'  `-----'  `--'    _  .-')--'   `--_ .-')-_---'('-.----' `(`-.--'             #
#           (  OO) ) _(  OO) ( OO ).(  OO) )                   ( \( -O )       ( (  OO) ) _(  OO)    _(OO  )_              #
#           /     '.(,------(_)---\_/     '._        .-'),-----.,------.        \     .'_(,------,--(_/   ,. \             #
#           |'--...__|  .---/    _ ||'--...__)      ( OO'  .-.  |   /`. '       ,`'--..._)|  .---\   \   /(__/             #
#           '--.  .--|  |   \  :` `.'--.  .--'      /   |  | |  |  /  | |       |  |  \  '|  |    \   \ /   /              #
#              |  | (|  '--. '..`''.)  |  |         \_) |  |\|  |  |_.' |       |  |   ' (|  '--.  \   '   /,              #
#              |  |  |  .--'.-._)   \  |  |           \ |  | |  |  .  '.'       |  |   / :|  .--'   \     /__)             #
#              |  |  |  `---\       /  |  |            `'  '-'  |  |\  \        |  '--'  /|  `---.   \   /                 #
#              `--'  `------'`-----'   `--'              `-----'`--' '--'       `-------' `------'    `-'                  #
#                                                                                                                          #
#                                                                                                                          #
# # # # # # # # #                                                                                                          #
# MODE = "DEV"  # DELETE THE "#" TO MAKE YOUR CHOICE ACTIVE                                                                #                                         #
MODE = "TEST"   # ONLY ONE MODE CAN BE ACTIVE AT A TIME                                                                    #                                    #
# # # # # # # # #                                                                                                          #
#                                                                                                                          #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
                                                                                                                            
 # EXIT ALL TRADES # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
ABORT_ALL_POSITIONS = False                                                                                                 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # FIND PAIRS TOGGLE # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                    
#                                                                                        
FIND_COINTEGRATED = False                                                                                                 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # PLACE TRADES TOGGLE # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
PLACE_TRADES = True                                                                                                         
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # AUTO MANGE POSITIONS TOGGLE # # # # # # # # # # # # # # # # #                                                          
#                                                                                                                           
MANAGE_EXITS = False                                                                                                         
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                             
                                                                                                                            
 # DATA RESOLUTION # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
RESOLUTION = "1HOUR"                                                                                                        
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # DATA WINDOW # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
WINDOW = 21                                                                                                                 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # OPENING THRESHHOLDS # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
MAX_HALF_LIFE = 24                                                                                                          
ZSCORE_THRESH = 0.5                                                                                                        
USD_PER_TRADE = 100                                                                                                          
USD_MIN_COLLATERAL = 1888                                                                                                   
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # CLOSING THRESHOLD # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
CLOSE_AT_ZSCORE_CROSS = True                                                                                                
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

 # OPEN AI API KEY # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
OPENAI_API_KEY = config("OPENAI_API_KEY")                                                                                               
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # ETH ADDRESS # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
ETHEREUM_ADDRESS = "0xb2D838612872586C88F4f53AF3678f7e8e54Fb39"                                                             
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                            
                                                                                                                            
 # KEYCHAIN - TEST # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET") 
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET") 
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET") 
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")  
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
                                                                                                                            
 # KEYCHAIN - PROD # # # # # # # # # # # # # # # # # # # # # # #                                                            
#                                                                                                                           
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET") 
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET") 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                             
                                                                                                                             
 # KEYCHAIN - EXPORT # # # # # # # # # # # # # # # # # # # # # #                                                           
#                                                                                                                           
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE=="DEV" else DYDX_API_KEY_TESTNET 
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE=="DEV" else DYDX_API_SECRET_TESTNET 
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE=="DEV" else DYDX_API_PASSPHRASE_TESTNET 
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "DEV" else STARK_PRIVATE_KEY_TESTNET 
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
                                                                                                                             
 # APIs - EXPORT # # # # # # # # # # # # # # # # # # # # # # # #                                                         
#                                                                                                                           
HOST = API_HOST_MAINNET if MODE == "DEV" else API_HOST_GOERLI
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                                                                                                                             
 # HTTP PROVIDER # # # # # # # # # # # # # # # # # # # # # # # #                                                         
#                                                                                                                           
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/_ytxiSzPROL6TJJst9NDuwGfjEddN67_"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/fX1FwzTUi31SaE7-_rfniIKGmhUEZpsx"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "DEV" else HTTP_PROVIDER_TESTNET
#                                                                                                                           
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                  