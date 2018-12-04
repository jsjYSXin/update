"""
	文件夹的行数
"""
count,blanks = 0,0
with open("a.txt") as fp:
	while True:
		line = fp.readline()
		if not line:
			break
		if len(line.strip())==0:
			blanks+=1
		# if (len(line)-1)==0:
		# 	blanks+=1
		#print(len(line.strip()))
		count+=1
print(count,blanks)