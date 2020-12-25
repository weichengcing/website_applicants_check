
import requests
import time


def sendline(msg):
    requests.post("https://notify-api.line.me/api/notify", data={"message": msg}, headers={
                  "Authorization": "Bearer line notify token"})


while True:
    print('----------------------')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('正在檢查報名狀態')
    r = requests.post("要檢查的網址")
    
    if "檢查是不是有名額釋出的文字" not in r.text:
        sendline("有名額快報名 要檢查的網址")
        exit(0)
    else:
        print('沒有 ~~ Q Q')
    if (int(time.strftime("%d", time.localtime())) > 23):
        sendline("任務結束 bye bye")
        time.sleep(1)
        exit(0)
    time.sleep(300)
