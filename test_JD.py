# -*-coding=utf-8-*-
import pytest
import requests
from bs4 import BeautifulSoup
import pandas
import openpyxl
import allure
from uuid import uuid1

'''
@Author:renyang
@Time:20120209
'''


@allure.feature('Test_JD')
class Test_JD:
    # 京东页面地址
    # info_list = []
    search_goods = ['巧克力', '鼠标']
    users = [{'user_name': 'Alex', 'pwd': '123'}, {'user_name': 'RenYang', 'pwd': '123'}]
    JD_url = 'https://www.sina.com.cn/'

    @pytest.fixture(scope='function', autouse=True)
    def login(self):
        self.data = {"loginType": "1", "pwdOrVerifyCode": Test_JD.users[0]['user_name'],
                     "userIdentification": Test_JD.users[0]['pwd']}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
        }

        return self.headers

    @allure.story('test_search_goods')
    @pytest.mark.parametrize("search_goods", search_goods)
    def test_search_goods(self, search_goods):
        jd_search_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&suggest=1.def.0.base&wq=qk&pvid=6a18d924eea747c2bc5172eb208da263'.format(
            search_goods)
        s = requests.session()
        res = s.get(jd_search_url, headers=self.headers)
        res.encoding = 'utf-8'
        # print('get response is  ' + res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(res.text)

        goods_title_list = soup.find_all('a')
        for goods_title in goods_title_list:
            if goods_title.get('title') is not None:
                print(goods_title.get('title'))

        # print('search_goods is '.capitalize() + search_goods + " jd search url is " + jd_search_url)
        assert 1

    @pytest.mark.functional_test
    @pytest.mark.skipif(condition=0 > 1, reason="skip")
    def test_order_detail(self):
        # order detail page to show goods info
        assert 1

    @allure.story('test_login_by_account')
    @pytest.mark.parametrize('users', users)
    def test_login_by_account(self, users):
        print('user name is '.capitalize() + users['user_name'])
        assert 1

    def test_get_sina_info(self):
        s = requests.session()
        website_list = []
        img_url_list = []
        # get and print sina news title

        res = s.get(Test_JD.JD_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(res.text)

        info_list = soup.find_all(attrs={'target': '_blank'})
        # print(soup.find_all(attrs={'target': '_blank'}))

        for info in info_list:
            # print(info.get('href'))
            if info.get_text() is not None:
                website_list.append(info.get_text())

        # print(website_list)
        df = pandas.DataFrame(data=website_list)
        df.to_excel('./website_list.xlsx')

        # print img links for sina website
        img_list = soup.find_all('img')
        for img in img_list:
            if img.get('data-src') is not None:
                img_url_list.append('http:' + img.get('data-src'))
        print(img_url_list)

        for img_url in img_url_list:
            1
        # self.download_img(img_url)
        return img_url_list

    def download_img(self, img_url):
        try:
            s = requests.session()
            res = s.get(img_url, headers=self.headers)
            f = open('./img/' + str(uuid1()) + '.jpg', 'wb')
            f.write(res.content)
        except Exception as e:
            print(e)
        pass

    @pytest.mark.xfail(condition=1 > 2, reason='fail')
    def test_login_CSND(self):
        1


if __name__ == '__main__':
    pytest.main(['-s', "test_JD.py"])
