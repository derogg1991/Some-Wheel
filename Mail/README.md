# 导入
import SM
# 默认不发送附件需要6个参数
# 调用例子:
f = 'some body@some mail'
p = 'password'
smtp = 'smtp server'
taddr = ['some body@some mail']
t = 'title'
content = 'mail content'
a = SM.SentMail(f, p, smtp, taddr, t, content)
a.sent_mail()
# 需要发送邮件,需要多加两个参数
f = 'some body@some mail'
p = 'password'
smtp = 'smtp server'
taddr = ['some body@some mail']
t = 'title'
content = 'mail content'
# 附件路径(绝对)
filepath = '/path/to/file'
# 附件名(自定义)
filename = 'filename'
a = SM.SentMail(f, p, smtp, taddr, t, content, filepath, filename)
a.sent_mail()
