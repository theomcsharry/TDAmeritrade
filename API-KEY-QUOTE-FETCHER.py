import pandas as pd
import time
PART1 = "https://api.tdameritrade.com/v1/marketdata/"
PART2 = "/quotes?apikey="
print("""

░██████╗░██╗░░░██╗░█████╗░████████╗███████╗  ███████╗███████╗████████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔═══██╗██║░░░██║██╔══██╗╚══██╔══╝██╔════╝  ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██║██╗██║██║░░░██║██║░░██║░░░██║░░░█████╗░░  █████╗░░█████╗░░░░░██║░░░██║░░╚═╝███████║█████╗░░██████╔╝
╚██████╔╝██║░░░██║██║░░██║░░░██║░░░██╔══╝░░  ██╔══╝░░██╔══╝░░░░░██║░░░██║░░██╗██╔══██║██╔══╝░░██╔══██╗
░╚═██╔═╝░╚██████╔╝╚█████╔╝░░░██║░░░███████╗  ██║░░░░░███████╗░░░██║░░░╚█████╔╝██║░░██║███████╗██║░░██║
░░░╚═╝░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░░░░╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

""")
time.sleep(1)
print("Creator - Theo McSharry")
time.sleep(1)
print("Contact me at theo@mcsharry.net")
print("https://github.com/theomcsharry/")
time.sleep(0.5)
TICKER=input('Input Ticker You Would Like a Quote For: ')
time.sleep(0.2)
print("If you do not have a TD AMERITRADE API, below, enter: TESTAPI")
APIKEY=input('Input Your TDA Api Key: ')
time.sleep(0.2)
print("Please wait, fetching your quote now.")
URL = ''.join([PART1, TICKER, PART2, APIKEY])
Quote = pd.read_json(URL)
print(Quote)
print('''

Contact me at theo@mcsharry.net''')
print("https://github.com/theomcsharry/")
print("The end! Thanks for using this program! Feel free to donate! Press Enter 5 times to close the program.")
input("5")
input("4")
input("3")
input("2")
input("1")