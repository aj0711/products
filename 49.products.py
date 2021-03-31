#while迴圈用在不知道運行幾次的地方
#二維度的清單，清單中還有清單
products = [] #2
while True: #1
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price =input('請輸入商品價格: ') #4
	#p = [] #5建立小清單
	#p.append(name)
	#p.append(price)
	# p = [name, price] 等同9~11行
	#products.append(p)#3 --> #6把本來的name改成p
	products.append([name, price]) #把9~13行替換掉
print(products)

#products[0][0] #products第0格清單中的第0格 --> 就是第0個商品的名字取出