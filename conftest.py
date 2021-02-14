import pytest
import requests
from bs4 import BeautifulSoup
import pymysql

print("Firstly we should login CSDN!")
NVC_url = 'https://passport.csdn.net/v1/api/riskControl/checkNVC?nvcValue=%7B%22a%22%3A%22FFFF00000000016C467E%22%2C%22c%22%3A%221613276331269%3A0.06699824382955888%22%2C%22d%22%3A%22nvc_login%22%2C%22h%22%3A%7B%22key1%22%3A%22code0%22%2C%22nvcCode%22%3A400%2C%22umidToken%22%3A%22T2gA7287LiOgjOCItoAKiLAgXXvYLLGI41rRoM1Yh1tQnes2E5Oqv8SIQpaIE8qd-c8%3D%22%7D%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22b%22%3A%22140%235L%2BrHlByzzZdGQo2L5ZTA6SogF%2FLOCNjdIf79d3eedibALmpkJMn9abOKzJNwf%2Fv4i1XjcWrXUAQDaZegKgIe9VyjP%2BZo3hqzznUIQT0M3rzzRbcba7BUbzx2DD3VtgqzT1i06VRU61xzoObV2Eqlj942hc2IsrruKpDxrvZrI7ZbvzLS4Tn9iy2JVWPMhcsiOvnI7BCnfYYK2q7%2BZlCFxHocQKnHJgVcYwFBF2Ib6zsZ%2FY4lfG%2FQBDkMpMUPNGJs7cg8ub4Z%2FKj3xs85xtm6mvsbj3EFcmJf7HHAl1oS4eLvYhhIdyml%2FgfzdEQzTA4G5joPRoP6OQQp%2BLHMCqq7K0IJV02Bu%2Fr5LICiza8pwF%2B0lnccP9AVUm30rTF5Hf8iqb%2F7moKfwHecnkCoORrSCTlj3dIEKVtbeAN7GAK%2F9jnhPSXZmb1zhe5RFWX1Vx4EJqK9dS%2FeDSD%2BB5RA1kWekA8p%2F%2FG92ZfZxkX0Eq7ScPRfIUR88PnpnZH9CDanrwy%2BILxfVFGsmpjQ2eZzYdkHezQdnBLaSLBQehGoB7CwlQSLWwDjDgmHl5kU45Kz78%2BHtUQgsqQLj2F9tIV%2B37kOOABgtuZOf42CX6hRhm8N0IQti2mKp%2FyKNw1E%2FOPBWcIpPOWmzoCg4ASZz28h0rOoPbZ1z3lcHHphkjGdcoCkyzwoCDms9mEsu8vcNDDoiHxZmYkA1cqsZyzXxbmpaRS68bDgMPN%2BXyr0X6FH6yw3G0%2BByt0Assf4eJOFzY%2BdDqESrt0BFSF1oDfiKizHH8sgJFEUj67r9QTPBBb7PR8uoUXqNN0GJBYi%2BxSnbsRmWUVlsZNNe2Z1YxMIbLpf2zeFD9Bp3jYJcGvkiylPbtIZOzVUDzSvKz8to0msyH%2F%2BFzynL%2FDqCJ2L7yTUDMy9%2BpbxnHHIFajBatGWDRvOhdFPQARBWnYCYhdYOqY5%2Fji8eHGzsKrDR%2BHsTf71qUVhbeTkNwIB6MZdAdLh2O17vfjhrzRSOot2ENDKa0ya4iZq2Ea%2BRdfdrCDmUFZOVZ1%2BP%2B81186GmYiFxvAsFEnkevHljz6iROXiKsAA68hUDp63%2BRYyBbYo3lJ5wB3WiDuhYp4KUhvbb%2FqZq8snLxYaPaCL14VJsKAyS0MyzBG1XidYfADA%2Fe78vjlhYt%2BHXGYNpC3rQGDY7aPIheObTbW%2F5K2qtteF6oercSfbKpvwVOwO7SNU1ksp44jfgAcfuYVWuu%2BDB31BgNG%2F3rXO2Usu62fjXedQafS0eK%2B5ZSAJHAm%2B8jfflSsNrdD9zR5rUWktHg2FHdFjnS5vTY5zYKj0OQsDjG692E7cdvPcx72YIM9WgByKhC6HlbT21DtyPMUSi9TbxuFL6uuCq7pnBdMZcDifTOdhYP1AvFSdwOZGtoE42L2oQzhy%2BohFCrDneeKDp2kjNYkt43SWfmtc9OrzwcwtkRrJv9uCAqXrjBE%22%2C%22e%22%3A%220y8NIKqD2V6MZWOAHH3Ywsiw0s7W4Q_p0jyYeFMpOa2Ou02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK6VKuP5lXnK4TP5V-60gN73QBg2__Y2rZaAykJ6RUrfgnggo1h2HkSU45RGVYz2a1Q%22%7D&callBackMethod=jsonp_09640264076523153&source=pc_password'
login_url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
# passport_url = 'https://passport.csdn.net/login?code=public'

uaToken = "140#3YbrQnQ7zzZCGQo2mxX+f6SDTg4CQhulNFzIV1f6h4YxrsG7toh6xRVA719jfxZyE87/86UBH1TU3qhqg9hytNtovossLFyulp1zz/jmo8BFMFzx0Hcza3Jjzzrb22U3lp1xzN1itI+YBFrrLPc3L6gqzzrVKsmx4VsDabLBZSXrPtrPHpcDuz0FgQq0cfIk33mWsj8cIuqHpputW7O1iYs5nttzrO+Bz1uagk+B9RxpzIHoMD5dgOgtWygxsmhPlWRHh0k8sBgL8z6U0esIC5i8yCa5PrE/tYc6J98YG6yIbyrAs/KYN8B6wNPIV27n+8ayEiTa4/I7LRK59t+lbC2EEcLWA9Oz376mZhPId6sI388Ld1LBEeOe0oLU0qjCQ60A1YBmsD4bAxrK3TYWelJnO+ZT8NepieiXhNTxJmzNdp/5rr4SMweYtyFOfBmGnsWNmcaD4k7SEyiMPkrZiWF6aFIWEi83kkm0E5/LQAxbPBqPynWq+4qPL7IPlZy5N4y7Zl55Amh2x/kLHTNnD/CZV0DywrQIpo+uWlAV2S9ZIXld2DA+B+VxKhRB55Ozl8FYWd9cWluXNsD4drZbpfjX+GDbKwsNFsThCnxFsTj7eGZMDfrpuoP+wkt95PREpTYilqNDVEBnf+7F4x/6I6H35wwV72XfFKlMUnl0L3QUw1W8QerRNVW1BUfxU9iqGBTtzy8zknOZ17TGSFDkV6jeF0Q/rZvi2r6NXEYeYHGrtBlAv9xDu3yhHPInAksjlVHn8y0SnPJe3g22LzjvjCRIzWq+R4vjx0NdUe3htqVuNOFpdUT7eMCgQLL+A7XgyJzLzMyw4fifA9Cj8QWKh62MFD9Bp3jYJcGvkiylPbtIZOzVUDzSvKz8to0msyH/+FzynL/DqCJ2L70pG1kePoopb/vjTEroAqaDPWFgFn3TH/yv2oRXFXEMb9Sg8t7JX8PKOxNXw1fEn1rYWUj2ivKfAYoKnOjTTxJYvLcm6Aarr8RbfM9xycXVFM3C/uyfqIZ0Kpf7HpQWysOhq24wV8ytCVbQeA9LB7YrxH21Jn0xHdPE6h5GvLUCBqxT3zmnAzkvmRyesPjKV6JAKB1FATkvtIjrrugsZ75xiWc9C+dOnAZcMBnq6cWGqz0CgsAYf/EjbhDWwIkb8PTNDwEOpQxzS+gwoLY+MK0de0lvcOEAVkywDKkEAj0gYDlAltKulVkRolWfi5oSjp80FtJS0bWBH2PHI/e3Wv59m/oBBgxbd/1oVWh5cuiJQDf5G+pOCv3cjTPRA2l8naFxdxbSlKyc1iliu+DyJReU4hTGNi69AyuSOukM4T8Vz7Vi2QSmCSQRsWBP96SZUuE7vJu/ax0EAmhVcVa4PjySfrYo1Jm4P+XywXfmmlovAB1cZ7HnREqIzuiybXdk4fkvosWjRezX2fqEf9/uAgqMCeiwFroN9xjcFZ08e6m4RQIVf0KoFxmzT8E053K3yl77SicPyW+tLEnrohF4HEYC0dfpWYJH3IpR6sQZpZm1N+hfvISE5SOv17/d3B8WHO+Q"
webUmidToken = "T2gACOjMA5Vljw-ne3FZwoIxKsstbCC8kcTuLakAmnWOTDjGzqn9WCefAF4QrIcHPIU="

users = [{'user_name': '1', 'pwd': '1'}, {'user_name': '17608462206', 'pwd': '123'}]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
}


@pytest.mark.parametrize('user', users)
@pytest.fixture(scope='session')
def login_CSDN_one(user):
    s = requests.session()
    s.get(url=NVC_url, headers=headers)
    data = {"loginType": '1', "pwdOrVerifyCode": user['pwd'], "userIdentification": user['user_name'],
            "uaToken": uaToken,
            "webUmidToken": webUmidToken}
    res = s.post(url=login_url, json=data, headers=headers)
    # print(res.json())
    return res.json()


@pytest.fixture(scope='session')
def login_CSDN_two(user):
    1
