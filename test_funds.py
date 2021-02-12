import pytest
import requests
from bs4 import BeautifulSoup
import test_JD
import json
import re


class Test_funds:
    funds_list_url = "http://fund.eastmoney.com/js/fundcode_search.js?v=20210212201438"
    funds_list = []
    fund_code_list = []
    funds_repository_list = []
    fund_detail_url = 'http://fund.eastmoney.com/{}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }

    @pytest.fixture(scope='function', autouse=True)
    def test_get_funds_list(self):
        funds_list_url = self.funds_list_url
        print(funds_list_url)
        s = requests.session()
        res = s.get(funds_list_url, headers=self.headers)
        # print(res.text)
        l1 = re.findall(r'\d{6}', res.text)
        self.fund_code_list = l1
        print(self.fund_code_list)
        return self.fund_code_list
        assert 1

    @pytest.mark.parametrize('fund_code_list', fund_code_list)
    def test_get_funds_repository(self, fund_code_list):
        s = requests.session()
        res = s.get(self.fund_detail_url.format(fund_code_list), headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(res.text)

        title_list = soup.find_all('a')
        for title in title_list:
            if title.get('title') is not None:
                self.funds_repository_list.append(title.get('title'))
        print(self.funds_repository_list)
        return self.funds_repository_list


if __name__ == '__main__':
    pytest.main(['-s', "test_funds.py"])
