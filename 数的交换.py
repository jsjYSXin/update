'''
	函数传的是值不是地址，数之间地址的交换
	每个数有一个对象，每一个对象有一个地址
'''
def add(x, y):
	print(id(x), id(y))
	x = 2;
	y = 6;
	print(id(x), id(y))
	return x+y

a = 1  #没一个数都有一个地址
b = 2
print(id(a), id(b))
add(a, b)
print(id(a), id(b))