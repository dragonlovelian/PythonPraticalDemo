#!/usr/bin/env python

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

"""发送Html文本"""
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('hello world!\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello world!</h4></body></html>', 'html')
    email.attach(html)
    return email


"""发送图片 参数为图片的路劲"""
def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    return email


"""发送一个消息  参数1为原地址 参数2为目标地址 参数3为要发送的消息"""
def sendMsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()


if __name__ == '__main__':
    print('sneding multipart alternative msg...')
    msg = make_mpa_msg()
    msg['From'] = '发送者的邮箱'
    msg['To'] = ', '.join('接收者的邮箱')
    msg['Subject'] = 'email test'
    sendMsg('发送者的邮箱', '接收者的邮箱', msg.as_string())
