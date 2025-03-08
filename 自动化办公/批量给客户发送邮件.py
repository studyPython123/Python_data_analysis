# Author: 邵世昌
# CreatTime: 2024/11/23
# FileName: 批量给客户发送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#%% 设置服务器和登入信息
smtp_server = 'smtp.163.com' # 设置要发送邮箱的smtp
port = 25 # 影响端口
username = '18770107022@163.com' # 自己的邮箱
password = 'GQrAYhsGpLNdPU6Z'# 授权码密码
#%% 创建smtp连接
server = smtplib.SMTP()
server.connect(smtp_server, port)
server.login(username, password)
customers = ['2578247403@qq.com'] # 发送的指定邮箱
#%% 创建邮件内容
subject = '这是一封测试邮件？'
body = '''
如果您收到了邮件，无需回复！
'''
for customer in customers:
    # 创建邮件对象
    message = MIMEMultipart()
    message['From'] =username
    message['To'] = customer
    message['Subject'] = Header(subject, 'utf-8')
    # 将文本添加到邮件体
    message.attach(MIMEText(body,'plain','utf-8'))
    # 发送邮件
    server.sendmail(username, customers, message.as_string())
    print(f'email is sent to: {customer}')
server.quit()