#!/usr/bin/env python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

#list of mail address you wana to send

MailDic = {"163.com":"smtp.163.com"}
MailUser = '***'
MailPswd = '***'
MailPostfix = '163.com'
MailHost = 'smtp.163.com'

def SendMail(to, sub, content):
    
    Me = MailUser + "<" + MailUser + "@" + MailPostfix + ">"
    Msg = MIMEText(content)
    Msg['Subject'] = sub
    Msg['From'] = Me
    Msg['To'] = to
    
    try:
        s = smtplib.SMTP()
        s.connect(MailHost)
        s.login(MailUser, MailPswd)
        s.sendmail(Me, to, Msg.as_string())
        s.close()
        return True
    except Exception, e:
        #print str(e)
        return False
        
def main(sub,content):
    if SendMail(to, sub, content):
        return
    else:
        return
    return 0

if __name__ == '__main__':
    SendMail('ppp@qq.com','***','***')
