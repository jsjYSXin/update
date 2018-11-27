import turtle as t
t.pensize(2)
colors = ["green","red","pink","blue"]
for x in range(200):
	t.color(colors[x%4])    #循环使用颜色
	t.fd(3*x)  				#向前走
	t.left(90)      		#左转90度
t.done()