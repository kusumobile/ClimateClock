import time
import datetime

xDay = datetime.datetime.strptime('2028-1-1 00:00:00','%Y-%m-%d %H:%M:%S')

yDay = datetime.datetime.now()

remaining = "残り"

def clock():
  global remaining
  zDay = xDay - yDay

  while True:
    while True:
      day  = str(int(zDay.days))
      hour = str(int(zDay.seconds/3600))
      min  = str(int((zDay.seconds/60)%60))
      sec  = str(int((zDay.seconds)%60))
      remaining = "残り"+ day + "日" + hour + "時間" + min + "分" + sec + "秒"
      print(remaining)
      zDay -= datetime.timedelta(seconds=1)
      time.sleep(1)

clock()
