from datetime import date
from datetime import datetime
import calendar
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import talib
import time
#ASCII:
print("""\

 /$$$$$$$$                       /$$ /$$                           /$$$$$$$$                  /$$
|__  $$__/                      | $$|__/                          |__  $$__/                 | $$
   | $$  /$$$$$$  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$          | $$  /$$$$$$   /$$$$$$ | $$
   | $$ /$$__  $$|____  $$ /$$__  $$| $$| $$__  $$ /$$__  $$         | $$ /$$__  $$ /$$__  $$| $$
   | $$| $$  \__/ /$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$         | $$| $$  \ $$| $$  \ $$| $$
   | $$| $$      /$$__  $$| $$  | $$| $$| $$  | $$| $$  | $$         | $$| $$  | $$| $$  | $$| $$
   | $$| $$     |  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$
   |__/|__/      \_______/ \_______/|__/|__/  |__/ \____  $$         |__/ \______/  \______/ |__/
                                                   /$$  \ $$                                     
                                                  |  $$$$$$/                                     
                                                   \______/                                      
                    """)

print("Project made by Alexander Leontaridis - Source code has copyright claims.")
print("-------------------------------------------------------------------------")
print("---------------------------------V. 0.2.0--------------------------------")
print("-------------------------------------------------------------------------")
#Menu:

print("""\

[1] RSI
More soon...
                    """)



def technical_1():

    selected_ticker = input('Enter ticker:')

    start_date = input('Enter start date (ex. 2022-10-13): ')
    end_date = input('Enter end date (ex. 2022-10-14): ')
    interval = input("Enter interval (ex. 1m): ")
    data = yf.download(selected_ticker, start=start_date, end=end_date, interval=interval)

    def RSI(data, window=14, adjust=False):
        delta = data['Close'].diff(1).dropna()
        loss = delta.copy()
        gains = delta.copy()

        gains[gains < 0] = 0
        loss[loss > 0] = 0

        gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
        loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

        RS = gain_ewm / loss_ewm
        RSI = 100 - 100 / (1 + RS)

        return RSI

    reversed_df = data.iloc[::-1]
    data["RSI"] = talib.RSI(reversed_df["Close"], 14)

    ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
    ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
    ax1.plot(data['Close'], linewidth=2.5)
    ax1.set_title(selected_ticker)
    ax2.plot(data['RSI'], color='red', linewidth=1.5)
    ax2.axhline(30, linestyle='--', linewidth=1.5, color='grey')
    ax2.axhline(70, linestyle='--', linewidth=1.5, color='grey')
    ax2.set_title(f'{selected_ticker} RSI')
    
    def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()
    items = list(range(0, 57))
    l = len(items)
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
    # Do stuff...
        time.sleep(0.001)
    # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    plt.show()

def options():
    while(True):
        result=input('Option:')
        if result=='1':
            technical_1()
        x=input('would you like to continue? Yes or No') 
        if x.lower() =='no':   
            break
        if x.lower() == "yes":
            options()
options()