"""
    需求: 使用 requests 库实现 TPShop 的登录功能
    分析: 步骤
        1. 先获取验证码(访问验证码接口)
        2. 再设置账号密码验证码访问登录接口
    框架搭建完毕，但是登录失败，为什么?
        核心: cookie
        1. 第一次发送请求，获取验证码时，相当于第一次去银行开户
           服务器为客户端创建了 Session,并将Session的ID以Cookie 的方式响应回了客户端
        2. 第二次访问时,按道理讲，应该提交第一次请求响应的 Cookie，但是实际没有提交
    解决:
        1. 从第一次响应中提取出 Cookie(银行卡)
        2. 第二次请求时，提交步骤1提取的 Cookie
"""
# 1. 导包
import requests

# 2. 访问获取验证码的接口


# 3. 下面的方法登录后获得服务器返回的token，存入变量username中
# 要素1
url = "https://passport.csdn.net/v1/register/authorization/status"
# 要素2
#myData =  {"username":"13012345678","password":"123456","verify_code":"8888"}
# 要素3
# 核心2:提交 Cookie
response = requests.post(url,cookies={'SESSION':'1daeb8aa-0ffc-4443-b50b-b32b720862a9'})

print("-"*80)
print("UserToken:",response.cookies['UserToken'])
print("响应体:",response.json())
UserName=response.cookies['UserName']
print(UserName)



#第二个请求手动带入前面函数返回的token，username
url = "https://www.csdn.net/community/toolbar-api/v1/get-user-info"
response = requests.get(url,cookies={'UserName':UserName})
response.encoding='utf-8'
print('response is : '+response.text)

print(response.status_code)
print('nickName is :'+response.json()['data']['nickName'])
print(response.headers.get("Content-Type"))
# 核心1:获取服务器响应的 Cookie
print("获取所有cookie:", response.cookies)
# 获取指定 Cookie
myCookieValue = response.cookies.get("dc_session_id")
print("dc_session_id:", myCookieValue)