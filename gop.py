from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S %p")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
lam = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
def get_wifi_info():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Lấy giao diện WiFi đầu tiên

    iface.scan()  # Quét mạng WiFi
    scan_results = iface.scan_results()

    if len(scan_results) == 0:
        return "Không có mạng WiFi nào được tìm thấy", None

    wifi_info = scan_results[0]
    ssid = wifi_info.ssid
    bssid = wifi_info.bssid

    return ssid, bssid
if __name__ == "__main__":
    ssid, bssid = get_wifi_info()
weather_description = get_weather()
System.Clear()
banner=f"""
\033[1;31m┌════════════════════════════════════════════════════════┐
\033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
\033[1;32m████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
\033[1;33m██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
\033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
\033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
\033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
\033[1;34m┠════════════════════════════════════════════════════════┨
\033[1;32m ➯ Cre   : Nguyễn Hoàng Nam                                         
\033[1;36m ➯ Nhóm Zalo  : https://zalo.me/g/pdsvkf650                                                
\033[1;33m ➯ Facebook: facebook.com/nam.nhn131                                
\033[1;34m└════════════════════════════════════════════════════════┘
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0)
print(f"{do} ➩ {trang}Ngày{trang} : {vang}{ngay_hom_nay}{lam} |{trang} Tháng{trang}: {vang}{thang_nay} {lam}| {trang}Năm{trang}: {vang}{nam_}{lam} | {trang}Thời Gian: {vang}{time}")
print(f"{do} ➩ {trang}Thành Phố : {vang}{city} {lam}|{trang} Khu Vực: {vang}{region} {lam}| {trang} Quốc gia: {vang}{country} {lam}| {trang} Tọa độ: {vang}{latitude}, {longitude} {lam}| {trang} Nhiệt độ: {vang}{weather_description}")
print(f"{do} ➩ {trang}Tên Mạng : {vang}{ssid} {lam}| {trang}Địa Chỉ MAC : {vang}{bssid}")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print(f"""{do}[{vang}</>{do}]LƯU Ý:{trang}Tool Riêng Của Nam Dev """)
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[1] \033[1;32mVÀO TOOL TRAO ĐỔI SUB      \033[1;35m  ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[2] \033[1;32mVÀO TOOL TƯƠNG TÁC CHÉO      \033[1;35m║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[3] \033[1;32mVÀO TOOL TIỆN ÍCH FB        \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[4] \033[1;32mVÀO TOOL TIKTOK             \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[5] \033[1;32mVÀO TOOL GOLIKE		\033[1;35m║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[6] \033[1;32mVÀO TOOL ENCODE      \033[1;35m        ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print(f"\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[7] \033[1;32mVÀO TOOL SPAM SMS + CALL    \033[1;35m ║")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[8] \033[1;32mVÀO TOOL DDOS + DEFACE      \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[9] \033[1;32mVÀO TOOL MAIL    	       \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[10] \033[1;32mVÀO TOOL PROXY    	       \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[11] \033[1;32mVÀO TOOL TIỆN ÍCH KHÁC     \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[00] \033[1;32mTHOÁT TOOL                 \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
sleep(0.2)
chon = int(input('\033[1;33mnhn\033[1;95m@\033[1;36mNamDev$ '))
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/tds.py').text)
elif chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/ttc.py').text)
elif chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/tienichfb.py').text)
elif chon == 4 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/tiktok.py').text)
elif chon == 5 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/golike.py').text)
elif chon == 6 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/encode.py').text)
elif chon == 7 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/spamsms.py').text)
elif chon == 8 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/ddos.py').text)
elif chon == 9 :
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/mail.py').text)
elif chon == 10:
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/proxy.py').text)
elif chon == 11:
	exec(requests.get('https://raw.githubusercontent.com/namhoang131/namdev1/main/tienich.py').text)
elif chon == 00 :
	print(f"{lam}Cảm Ơn Bạn Đã Dùng Tool Của {vang}Nguyễn Hoàng Nam")
else :
	sys.exit('Vui Lòng Chọn Đúng Chế Độ!')
