import smtplib
from email.mime.text import MIMEText #纯文本文件

from_addr = "2240746438@qq.com"
#to_addr = "1484180941@qq.com"
to_addr = from_addr
psw = 'hkipmhydfabbeajd'
smtp_server = "smtp.qq.com"

with open("test.html", 'r', encoding = "utf-8") as fp:
	contents = fp.read()

#contents = "<h1>Hellow World!</h1>"#邮件的内容
#以utf—8发送，格式为plain,文件名为contents
msg = MIMEText(contents, 'plain', 'utf-8')#MIMEText中的3个参数
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Text"

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())#把msg转化成一个string
server.quit()#退出服务器
