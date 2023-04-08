import requests
import os 

response_csv = requests.get('https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230301&stockNo=2330&response=csv')

if not os.path.exists('twse_csv'):
    os.mkdir('twse_csv')

with open('twse_csv//2330_202303.csv', 'wb') as f:
    f.write(response_csv.content)