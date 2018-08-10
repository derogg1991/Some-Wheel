#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# test env == python3.5.2

from email.mime.text import MIMEText
from email import encoders
# 改变编码支持中文
from email.header import Header
# 格式化发件人、收件人
from email.utils import parseaddr, formataddr
# 附件支持
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

class SentMail(object):

    def __init__(self, faddr, passwd, smtp, taddr, title, content, filepath=None, filename=None):
        self.faddr = faddr
        self.passwd = passwd
        self.smtp = smtp
        self.taddr = taddr
        self.title = title
        self.content = content
        self.filepath = filepath
        self.filename = filename

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    def sent_mail(self):
        if type(self.taddr) != list:
            print('接收人请定义为list')
        else:
            # 建立MIMEmultipart对象msg,此对象即为邮件
            msg = MIMEMultipart()
            faddr = self.faddr
            taddr = self.taddr
            msg['From'] = self._format_addr(faddr)
            msg['To'] = self._format_addr(taddr)
            msg['Subject'] = Header(self.title, 'utf-8').encode()
            text = MIMEText(self.content, 'plain', 'utf-8')
            msg.attach(text)
            if self.filepath and self.filename:
                # 实例化附件
                atta = MIMEApplication(open(self.filepath, 'rb').read())
                atta.add_header('Content-Disposition', 'attachment', filename=self.filename)
                msg.attach(atta)
            server = smtplib.SMTP(self.smtp, 25)
            # 打印出和smtp交互的信息
            server.set_debuglevel(1)
            server.login(self.faddr, self.passwd)
            server.sendmail(self.faddr, self.taddr, msg.as_string())
            server.quit()
