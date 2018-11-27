'''
	文件夹目录的遍历查询，
'''
import os
#print(os.getcwd())获取当前路径
root_path = os.getcwd()
offset = len(root_path.split("\\")) #输出目录的级数长度（最基本的5级）
#获取全部的目录(遍历)
for root,files,dir in os.walk(root_path):
	current_dir = root.split("\\") #获取所有的目录名称
	indent_level = len(current_dir) - offset #indent_level 总长度-最基本的目录长度
	print(indent_level*"\t", current_dir[-1])#输出最后一级的目录名称

#print(20*"?")输出20个问号
#print(root_path.split("\\")[-1]) 具体显示到某一级
