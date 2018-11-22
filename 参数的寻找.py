c = 789
def foo():
	#c = 456  若外层函数还没有C，就去全局变量里面查找	
	def bar():
		#c = 123	内层函数里面没有C，那就可以去外层函数里面寻找	
		print("c=", c)
	bar()	
if __name__ == '__main__':
	
	foo()
	hanshu = foo
	hanshu()
	'''print(__name__)
	#查看內键变量
	print(locals())#返回一个字典
	print(globals())'''
	print(foo)#返回函数的首地址