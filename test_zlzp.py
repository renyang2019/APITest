# -*- coding: utf-8 -*-
import requests
# 使用urlencode将key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串。
from urllib.parse import urlencode
from requests.exceptions import RequestException
# responce使用Content-Encoding=br压缩，所以需要brotli模块用于解压
# import brotli
# 将json文件保存到本地XXX.json，再次读取将json字符串转换为对应的python数据类型（load 方法），主要是{}对象转dict,[]数组转list
import json
import sqlite3

# sqllite3的数据库位置
# conn = sqlite3.connect('D:\\Program Files\\sqlite\\data\\智联招聘福州（java_python）\\jobData.db')
# get方式提交的参数字典
param = {
    'start': 180,
    'pageSize': 60,
    'cityId': 801,
    'workExperience': -1,
    'education': -1,
    'companyType': -1,
    'employmentType': -1,
    'jobWelfareTag': -1,
    'kw': 'python',
    'kt': 3,
    'lastUrlQuery': {"p": 4, "pageSize": "60", "jl": "801", "kw": "python", "kt": "3"}
}
# http协议中request请求的请求头信息，数值可以使用本地浏览器开发者工具（F12）查看并修改
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Host': 'fe-api.zhaopin.com',
    'Referer': 'https://sou.zhaopin.com/',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Origin': 'https://sou.zhaopin.com',
    # cookie 修改为(本地的cookie)
    "Cookie": 'adfbid2=0; x-zp-client-id=3e29f9a3-b0fe-4ec6-bf26-b690a4fc9e3a; sts_deviceid=17801cfe49b3fc-02299f9d7b0d9f-53e356a-921600-17801cfe49c481; locationInfo_search={%22code%22:%222406%22%2C%22name%22:%22%E9%95%BF%E6%B2%99%E5%8E%BF%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; adfcid2=www.baidu.com; ZP_OLD_FLAG=false; urlfrom2=121113803; dywea=95841923.563355151111102200.1615089367.1616144098.1616412814.16; dywez=95841923.1616412814.16.7.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.1025597109.1615089368.1616144099.1616412817.15; __utmz=269921210.1616412817.15.7.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/; LastCity%5Fid=765; LastCity=%E6%B7%B1%E5%9C%B3; urlfrom=121113803; adfbid=0; sts_sg=1; sts_sid=17876e8ecb25df-0066007cecf78d-5771031-921600-17876e8ecb3aa5; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.K60000azYgcknkR4bdKXKslUjH3_vrLdYM0Vevn8fGDzr8qAt1XL0ta3T5wPMbwz5PHgmppZ5WRxJppYco_DZZ-7xbegw2cvbHdph13i2028F2w2ULh4jhxZSEv2kO6vUdKy3XkkeFJ91AmquvTd3kg7s8R_HACe8pzmvz7vf_LLOMupCXwm_9ScjkNYj5i8cFDGmfL7cfhX6H8g_E9m4EBmHwJr.7Y_NR2Ar5Od669BCXgjRzeASFDZtwhUVHf632MRRt_Q_DNKnLeMX5Dkgbooo3eQr5gKPwmJCRnTxOoKKsTZK4TPHQ_U3bIt7jHzk8sHfGmEukmnTr59l32AM-YG8x6Y_f3lZgKfYt_QCJamJjArZZsqT7jHzs_lTUQqRHArZ5Xq-dKl-muCyrMWYv0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqd_xKJVgfko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqd_xKJVgfko60ThPv5HD0IgF_gv-b5HDdnWf4Pj6Ln1n0UgNxpyfqnHfzPHfYnWf0UNqGujYknjbsnjnLnsKVIZK_gv-b5HDznWT10ZKvgv-b5H00pywW5R420APzm1YzPHns%26ck%3D8801.2.195.388.157.410.162.192%26dt%3D1616902666%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26tpl%3Dtpl_12273_24677_20875%26l%3D1524948733%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526linkType%253D; at=04a66f078f6c4a8bac6fda40bb0edf67; rt=f322af4f2aa94a2b880e5503907151d3; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1616497495,1616584831,1616764344,1616902714; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1616902721; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22624979186%22%2C%22first_id%22%3A%2217801cfe4e2424-0bbe4628ddb6d7-53e356a-921600-17801cfe4e3d34%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22%24device_id%22%3A%2217801cfe4e2424-0bbe4628ddb6d7-53e356a-921600-17801cfe4e3d34%22%7D; selectCity_search=801; ssxmod_itna=YuDQ7KAKGK0IKmqYKGHLfjphpPnvnCi=iox0vW4PGzDAxn40iDtrxXDGTxO2ibhCDUge0rbKjMmiqEbFBmKAT=rx0aDbqGk536G4GGAxBYDQxAYDGDDPDoEPD1D3qDkLxYPGWbqA3DYxDrE=KDRxi7DDvd7x07DQH8D+PhR2YC5DAebmKD9gYDsp0vPmK+G38xg1R7DlKLDCK1Rp9kQ4Gdmj0oqlPNOi2xM3hi/DrtMmwo4Px2=mDTWYeqdCr5iWpXWWDDiahX4D; ssxmod_itna2=YuDQ7KAKGK0IKmqYKGHLfjphpPnvnCi=DnFgiqDtDl69DjbCf8o07PjDLxYFhD==; ZL_REPORT_GLOBAL={%22jobs%22:{%22funczoneShare%22:%22dtl_best_for_you%22%2C%22recommandActionidShare%22:%224bfda6a6-aff8-41ea-9f1e-3abe9a4ded79-job%22}}; sts_evtseq=44; acw_tc=ac11000116169071407571128e00edd146b336a1498da88fe8d4171bfb5e64'
    # cookie 读者在本地浏览器的开发者工具中复制即可
}


def getPage(city='', keyword='', pageNo=4):
    param['start'] = 60 * (pageNo - 1)
    param['kw'] = keyword
    tempDict = {"p": 4, "pageSize": "60", "jl": "681", "kw": "python", "kt": "3"}
    tempDict['p'] = pageNo
    tempDict['kw'] = keyword
    # print(tempDict)
    param['lastUrlQuery'] = tempDict
    # print(str(tempDict))
    # print(param)
    # print(urlencode(param))
    url = 'https://fe-api.zhaopin.com/c/i/search/positions'
    print('url is :' + url)
    filename = '智联_' + city + '_' + keyword + '_第' + str(pageNo) + '頁_数据.json'
    print(filename)
    try:
        # 获取网页内容，返回html数据
        response = requests.post(url, headers=headers, json=param)
        # 通过状态码判断是否获取成功
        # print(response.encoding)
        # print(response.headers)
        # print(response.headers['Content-Encoding'])  Content-Encoding=br
        # 此处必须使用brotli进行解压，否者为乱码，其中brotli模块安装可能失败，提示microsoft visual c++ 14.0 is required，可以通过安装解决
        # tempData = brotli.decompress(response.content)
        response.encoding = 'utf-8'
        data = response.json()
        print(data)

        with open(filename, 'w', encoding='utf-8')as f:
            f.write(data)

        if response.status_code == 200:
            return data
        return None
    except RequestException as e:
        return None


if __name__ == '__main__':
    # 由于爬取数据时，发现python才7页，java远多于7页，所以为了便于处理比较，将数据爬取页数设置为7
    totalPage = 7
    # 下载json文件
    for pageNo in range(1, totalPage + 1):
        data = getPage(city='福州', keyword='python', pageNo=pageNo)
