import pytest
import requests
from bs4 import BeautifulSoup
import pymysql
import json
import conftest


@pytest.mark.parametrize('user', conftest.users)
def test_login_CSDN_one(user):
    s = requests.session()
    s.get(url=conftest.NVC_url, headers=conftest.headers)
    data = {"loginType": '1', "pwdOrVerifyCode": user['pwd'], "userIdentification": user['user_name'],
            "uaToken": conftest.uaToken,
            "webUmidToken": conftest.webUmidToken}
    res = s.post(url=conftest.login_url, json=data, headers=conftest.headers)
    print(json.loads(res.text))
    if json.loads(res.text)['status'] == True:
        print('Login success!')
    else:
        print('Login failed!')


def test_login_CSDN_two():
    1


if __name__ == '__main__':
    pytest.main(['-s', "test_login.py"])
