
# coding: utf-8
import requests
import pandas as pd
import json

url = 'https://api.cnyes.com/media/api/v1/newslist/category/headline' # 連線鉅亨網
payload = {
    'page':1,
    'limit':30,
    'isCategoryHeadline':1,
    'startAt':1753714074,
    'endAt':1754578074
}
res = requests.get(url, params=payload) 
jd = json.loads(res.text) # 解析 JSON 轉成 dict
df = pd.DataFrame(jd['items']['data']) # 取出新聞資料
df = df[['newsId', 'title', 'summary']] # 取出特定欄位
df['link'] = df['newsId'].apply(lambda x: 'https://news.cnyes.com/news/id/' + str(x)) # 建立連結
df.to_csv('news.csv', encoding='utf-8-sig', index=False) # 儲存成 CSV 檔案
print(df)

