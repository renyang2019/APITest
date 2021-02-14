import pytest
import requests
from bs4 import BeautifulSoup
import test_JD
import json
import re

from conftest import login_CSDN_one


class Test_funds:
    print(login_CSDN_one)
    funds_list_url = "http://fund.eastmoney.com/js/fundcode_search.js?v=20210212201438"
    funds_list = []

    funds_repository_list = []
    fund_detail_url = 'http://fund.eastmoney.com/{}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }

    # @pytest.fixture()
    def get_funds_code_list(self):
        funds_list_url = self.funds_list_url
        print('funds_list_url is : ' + funds_list_url + '\n')
        s = requests.session()
        res = s.get(funds_list_url, headers=self.headers)
        # print(res.text)
        self.fund_code_list = re.findall(r'\d{6}', res.text)

        # print(self.fund_code_list)
        assert 1
        return self.fund_code_list

    # @pytest.mark.parametrize('fund_code', get_funds_code_list())
    def test_get_funds_repository(self):
        for fund_code in self.get_funds_code_list()[5:7]:
            l1 = []
            # funds_repository_list=[]
            print('fund_code is : ' + fund_code + '\n')
            s = requests.session()
            res = s.get(self.fund_detail_url.format(fund_code), headers=self.headers)
            print('fund_detail_url : ' + self.fund_detail_url.format(fund_code) + '\n')
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            # print('resoponse is : ' + res.text+'\n')

            title_list = soup.find_all('a')
            for title in title_list:
                if title.get('title') is not None:
                    l1.append(title.get('title'))
                    # print('title is : ' + title.get('title'))
            print(l1[2:12])
            self.funds_repository_list = self.funds_repository_list + l1[2:12]

        print(self.funds_repository_list)
        assert 1
        # return self.funds_repository_list


if __name__ == '__main__':
    pytest.main(['-s', "test_funds.py"])
