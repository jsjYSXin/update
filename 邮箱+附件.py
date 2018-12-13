import smtplib#引入一个邮件包发送邮件
from email.mime.text import MIMEText #纯文本文件，构建邮件的正文
from email.header import Header  # 收件人 发件人的主题信息

from email.mime.multipart import MIMEMultipart #导入可以发送附件的包 每一个附件都是一个Multipart
from email.mime.base import MIMEBase #每一个MEMUBase对应的就是一个附件
from email import encoders #把所有文件进行序列化使用

def add_attachment(file):
	with open(file, 'r') as fp:
		mime = MIMEBase('application', 'octect-string', filename = file) #1\指定对象是什么类型 2\以什么形式发送octect-string
		#Disposition处理方式，用attachment（添加附件）
		mime.add_header("Content-Disposition", 'attachment', filename = file) #添加附件的头部
		mime.add_header("content-ID", "<0>") 
		mime.add_header("X-attachment-Id", "0")#告诉浏览器 用什么指定的程序去打开 attachment-Id附件用X（未知）打开
		mime.set_payload(fp.read())
		encoders.encode_base64(mime) #base64跟utf-8一样是一种编码格式
		att_msg.attach(mime)

from_addr = "2240746438@qq.com"
to_addr = "1484180941@qq.com"
#to_addr = from_addr
psw = 'hkipmhydfabbeajd'
smtp_server = "smtp.qq.com"

 # with open("test.html", 'r', encoding = "utf-8") as fp: #发送test.html的文件给收件人
 	# contents = fp.read()

#创建邮件正文对象
contents = "Hellow World!"#邮件的内容
#以utf—8发送，格式为plain,文件名为contents
msg = MIMEText(contents, 'plain', 'utf-8')#MIMEText中的3个参数
# msg['From'] = from_addr
# msg['To'] = to_addr
# msg['Subject'] = "Text"

#创建带附件的邮件对象
att_msg = MIMEMultipart()
att_msg['From'] = from_addr
att_msg['To'] = to_addr
att_msg['Subject'] = "Text"

att_msg.attach(msg) #将正文添加到带附件的邮件对象

#批量添加附件
att = ["test.txt", "test2.txt"]
for a in att:
	add_attachment(a)

#创建服务器连接语句
server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)  #登陆自己的邮箱号 账号 from_addr 密码psw
server.sendmail(from_addr,to_addr,att_msg.as_string())#把msg转化成一个string【to_addr】群发
server.quit()#退出服务器