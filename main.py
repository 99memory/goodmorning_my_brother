from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
    url1 = 'https://geoapi.qweather.com/v2/city/lookup?location=' + city + '&key=72b5d1a456a94bd38c4a5a448fa1da66'
    response1 = requests.get(url1)
    data1 = response1.json()
    id = data1["location"][0]["id"]

    url2 = "https://devapi.qweather.com/v7/weather/3d?location=" + id + "&key=72b5d1a456a94bd38c4a5a448fa1da66"
    response = requests.get(url2)
    data = response.json()
    weather = data["daily"][0]["textDay"]
    top = data["daily"][0]["tempMax"]
    low = data["daily"][0]["tempMin"]
    temperature = (int(top) + int(low)) / 2
    print(weather, temperature)
    return weather, temperature



def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
