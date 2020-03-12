#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#i_content=raw_input('pleaseinput:')
my_sender='332945894@qq.com'
my_pass='ifcgdfheedgocbcf'
my_user='332945894@qq.com'
my_user2='kjnnyz@163.com'

def main():
        msg=MIMEText("财路snsmq-supervisor-报警, IP:39.104.69.64",'plain','utf-8')
        msg['From']=formataddr(["monitor",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="财路snsmq-supervisor报警, IP:39.104.69.64 "                # 邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender,[my_user,my_user2],msg.as_string())
        server.quit()
if __name__ == '__main__':
    main()
