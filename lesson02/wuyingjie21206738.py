from email.utils import localtime
import time
import requests
heards = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}
url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/f4032135-d166-412f-9f2c-d86af6bb6ab8'
respo = requests.get(url,headers=heards).json()
def strfime(args):
    pass
def pupu(respo):
    name = respo['data']['name']
    a=respo['data']['price']
    b=respo['data']['market_price']
    print("现在的时间是：",strfime("%Y-%m-%d %H:%M:%S"),localtime())
    print(name,  "原价",b / 100)
    print(name,"现价",a/100)
if __name__ == '__main__':
    def sleep_time(hour, min, sec):
        return hour * 3600 + min * 60 + sec
    # 时间间隔
    second = sleep_time(0, 0, 2)
    while True:
        time.sleep(second)
        pupu(respo)
