#!/usr/bin/env python

import email
"""用于解析邮件"""
def processMsg(entire_msg):
    body=''
    msg=email.message_from_string(entire_msg)#解析消息
    if msg.is_multipart():
        for part in msg.walk():#遍历消息的附件
            if part.get_content_type()=='text/plain':#判断是否为文本信息
                body=part.get_payload()#从消息的正文中获取特定的部分，通常 decode 标记会设为 True，即邮件正文根据每个Content-Transfer-Encoding 头解码
                break
        else:
            body=msg.get_payload(decode=True)
    else:
        body=msg.get_payload(decode=True)

    return body
