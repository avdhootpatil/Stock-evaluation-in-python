import pandas as pd
import matplotlib.pyplot as plt
import os


def test_function(message):
    print("Your message is", message)
    
    
    
def symbol_to_path(symbol, base_dir='data'):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
    
    
def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True,usecols=  ['Date','AdjClose'],
        na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp,how="inner")
    return df


def plot_data(df,title="stock"):
    ax = df.plot(title=title,fontsize=2) #creating object of the plot
    ax.set_xlabel("Date")         #setting x label on plot object
    ax.set_ylabel("Price of stock")  #setting ylabel on plot object
    plt.show()