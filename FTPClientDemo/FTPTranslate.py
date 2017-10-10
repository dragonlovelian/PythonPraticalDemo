#!/usr/bin/env python

import ftplib
import os
import socket

HOST='ftp.mozilla.org'                          #解析的url
DIRN='pub/mozilla.org/webtools'                 #ftp服务器文件的位置
FILE='bugzilla-LATEST.tar.gz'

def main():
    try:
        f=ftplib.FTP(HOST)                      #创建一个FTP对象尝试连接到FTP服务器
    except (socket.error,socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('connecting to host "%s"' % HOST)
    try:
        f.login()                               #尝试用匿名登陆
    except ftplib.error_perm:
        print('error:no support anonymously')
        f.quit()
        return
    print('login in as anonymous')
    try:
        f.cwd(DIRN)                             #转到要下载的文件目录
    except ftplib.error_perm:
        print('error:cannot cd to "%s"' % DIRN)
        f.quit()
        return
    print('changed to "%s"' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write) #传入一个回调函数，每次收到二进制数据的时候就会调用这个函数写入文件
    except ftplib.error_perm:
        print('error:cannot read file "%s"' % FILE)
        os.unlink(FILE)
    f.quit()

if __name__=='__main__':
    main()


