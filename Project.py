import pandas as pd 
import sqlalchemy
import asyncio
from binance import AsyncClient, BinanceSocketManager
from binance.client import Client
from sqlalchemy.sql.expression import true
import config
from datetime import datetime, timedelta

client = Client(config.api_key, config.api_secret)

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')

df = pd.read_sql('BTCUSDT',engine)

def strategy(mins, open_position=False):
    while True:
        import datetime
        meta = sqlalchemy.MetaData()
        meta.reflect(bind=engine)
        too_old = datetime.datetime.today() - datetime.timedelta(minutes=3)
        lookback = (datetime.datetime.today() - datetime.timedelta(minutes=mins))
        lookbackperiod = df.loc[lookback:]
        #lookback = datetime.datetime.today() - datetime.timedelta(minutes=mins)
        print(lookbackperiod)
        #cumret = (lookback.Price.pct_change() +1).cumprod() - 1
        #print(cumret)
        print('1')
        if not open_position:
            print('no')
            
strategy(1)

