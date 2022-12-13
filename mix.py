#実行プログラム
import schedule
import datetime
from time import time
from time import sleep

print("自動ツイート実行中")

#自動撮影
def auto_photo():
    import photo

#動画作成
def auto_movie():
    import movie

#自動ツイート
def movie_Tweet():
    import tweet


schedule.every(10).minutes.do(auto_photo)   #10分に1回自動撮影
schedule.every().days.at("動画作成したい時間").do(auto_movie)
schedule.every().days.at("ツイートしたい時間").do(movie_Tweet)

#イベント実行
while True:
    schedule.run_pending()
    sleep(1)

