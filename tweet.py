#自動ツイート
import os, json
import requests
from requests_oauthlib import OAuth1Session
import datetime
import time


API_KEY = '自分のAPI_KEYを入力'
API_KEY_SECRET= '自分のAPI_KEY_SECRETを入力'
ACCESS_TOKEN = '自分のACCESS_TOKENを入力'
ACCESS_TOKEN_SECRET = '自分のACCESS_TOKEN_SECRETを入力'

twitter = OAuth1Session(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

update_url = "https://api.twitter.com/1.1/statuses/update.json"
url_media = "https://upload.twitter.com/1.1/media/upload.json"

# ローカルの動画ファイルサイズを取得
strdate=datetime.datetime.now().strftime('%Y_%m%d')
totalBytes = os.path.getsize("./Movies/Movie"+strdate+".mp4")

# メディアIDの取得
initParams = {
    "command": "INIT",
    "media_type": "video/mp4",
    "total_bytes": totalBytes,
    "media_category": "tweet_video"
}
initResponse = twitter.post(url=url_media, data=initParams)
media_id = initResponse.json()['media_id']

# 分割アップロード
segment_id = 0
bytesSent = 0
with open("./Movies/Movie"+strdate+".mp4", "rb") as f:
    while bytesSent < totalBytes:
        # 4MBずつアップロード
        chunk = f.read(4*1024*1024)

        addParams = {
            "command": "APPEND",
            "media_id": media_id,
            "segment_index": segment_id
        }

        files = {"media": chunk}

        appendResponse = twitter.post(url=url_media, data=addParams, files=files)
        
        segment_id += 1
        bytesSent = f.tell()
        print("%s of %s bytes uploaded" % (str(bytesSent), str(totalBytes)))

    print("アップロード完了")

    # ファイナライズ処理
    finalizeParams = {"command": "FINALIZE", "media_id": media_id}

    finalizeResponse = twitter.post(url=url_media, data=finalizeParams)

    statusParams = {"command": "STATUS", "media_id": media_id}

    statusResponse = twitter.get(url=url_media, params=statusParams)
    processingInfo = statusResponse.json().get("processing_info", None)

    while processingInfo['state'] == 'in_progress':
        time.sleep(1)
        statusResponse = twitter.get(url=url_media, params=statusParams)
        processingInfo = statusResponse.json().get("processing_info", None)
        print(processingInfo)
    
    #テキスト入力
    text = 'ツイートしたいテキスト入力'

    # ツイート
    params = {"status": text, "media_ids": media_id}

    twitter.post(url=update_url, data=params)