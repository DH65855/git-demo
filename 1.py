
# coding: utf-8
import requests
import pandas as pd
import json
import datetime as dt

data = []
url = 'https://api.cnyes.com/media/api/v1/newslist/category/headline' # 連線鉅亨網
payload = {
    'page':1,
    'limit':30,
    'isCategoryHeadline':1,
    'startAt':int((dt.datetime.today() - dt.timedelta(days=11)).timestamp()),
    'endAt':int(dt.datetime.today().timestamp())
}

res = requests.get(url, params=payload) 
jd = json.loads(res.text) # 解析 JSON 轉成 dict
data.append(pd.DataFrame(jd['items']['data']))
for i in range(2, jd['items']['last_page'] + 1):
    print('i = ', i)
    payload['page'] = i
    res = requests.get(url, params=payload) 
    jd = json.loads(res.text) # 解析 JSON 轉成 dict
    data.append(pd.DataFrame(jd['items']['data']))

df = pd.concat(data, ignore_index=True) # 取出新聞資料
df = df[['newsId', 'title', 'summary']] # 取出特定欄位
df['link'] = df['newsId'].apply(lambda x: 'https://news.cnyes.com/news/id/' + str(x)) # 建立連結
df.to_csv('news.csv', encoding='utf-8-sig', index=False) # 儲存成 CSV 檔案
print(df)

