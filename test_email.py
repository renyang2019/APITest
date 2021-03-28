from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

# sender_qq为发件人的qq号码
sender_qq = '418474236'
# pwd为qq邮箱的授权码
pwd = '**iao***lxpic***'
# 收件人邮箱receiver
receiver = ['418474236@qq.com']
# 邮件的正文内容
mail_content = '你好，我是来自知乎的[renyang HIT] ，现在在进行一项用python登录qq邮箱发邮件的测试'
# 邮件标题
mail_title = 'From renyang 的邮件'


def send_mail(sender_qq='', pwd='', \
              receiver=[], mail_title='', mail_content=''):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq + '@qq.com'

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


def get_mail_content():
    return mail_content


for i in range(10):
    send_mail(sender_qq=sender_qq, pwd=pwd, \
              receiver=receiver, mail_title=mail_title, \
              mail_content=get_mail_content())
