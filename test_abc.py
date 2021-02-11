import pytest
import requests
from bs4 import BeautifulSoup


class Test_CSDN:
    @pytest.fixture(scope='function')
    def login(self):
        print("Firstly we should login CSDN!")
        url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
        passport_url = 'https://passport.csdn.net/login?code=public'
        data = {"loginType": "1", "pwdOrVerifyCode": "123", "userIdentification": "17608462201"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
        }

        s = requests.session()
        res_two = s.post(url=url, json=data, headers=headers)
        # r2_cooike = res_two.cookies.get_dict()
        # print(r2_cooike)
        # print(res_two.json())

        res_1 = s.get(passport_url, headers=headers)
        # print(res_1.text)
        soup = BeautifulSoup(res_1.text, 'html.parser')

        title = soup.find('title').get_text()
        des = soup.find(attrs={'name': 'description'}).get('content')
        print('title is : {}, description is {}'.format(title, des))

        users = [{'user_name': 'ren', 'pwd': '123'}, {'user_name': 'yang', 'pwd': '123'}]
        return users

    @pytest.mark.parametrize("user_name,pwd", [('ren', '123'), ('yang', '123')])
    def test_case_one(self, user_name, pwd):
        print("------->case 1 user_name : {}, pwd : {} ".format(user_name, pwd))
        assert user_name == 'ren'

    @pytest.mark.function_test
    @pytest.mark.skipif(condition=0 > 1, reason="skip")
    def test_case_two(self, login):
        print("------->case 2")
        assert login[0]['user_name'] == 'ren'


if __name__ == '__main__':
    pytest.main(['-s', "test_abc.py"])
