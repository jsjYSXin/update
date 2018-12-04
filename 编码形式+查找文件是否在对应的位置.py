"""
	检测文件编码形式，以及文件夹的行数，空格的行数
"""
from chardet import detect
from os.path import *
count,blanks = 0,0
with open("a.txt", 'rb') as fp:
	#检测文件编码，编码信息保存到code中
	code = detect(fp.read())['encoding']
	print(code)

with open("a.txt", 'r',encoding=code) as fp:
	while True:
		line = fp.readline()
		if not line:
			break
		if len(line.strip())==0:#【同if (len(line)-1)==0:  blanks+=1】运行结果一样
			blanks+=1
		# if (len(line)-1)==0:
		# 	blanks+=1
		#print(len(line.strip()))打印每行空格数
		count+=1
print(count,blanks)

path = r"D:\dirs\a.txt"
print(isfile(path))