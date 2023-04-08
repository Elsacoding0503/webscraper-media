import requests
import os 

stocks = [2330, 6183]

for stock in stocks:
    response_csv = requests.get(f'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230301&stockNo={stock}&response=csv')

    if not os.path.exists('twse_csv'):
        os.mkdir('twse_csv')

    with open(f'twse_csv//{stock}_202303.csv', 'wb') as f:
        f.write(response_csv.content)