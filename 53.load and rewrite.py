#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續,跳到下一迴,商品和價格這一行會跳過
		name, price = line.strip().split(',')#.split是用來切割字串，括號內是用什麼來切割，原例是遇到','就來切割#.strip把換行符號去除 #從左而右處理，先strip再split
		#name = s[0] 可以直接透過name and price 來取代第6、7行
		#price = s[1]
		products.append([name, price])
print(products)

	#while迴圈用在不知道運行幾次的地方
	#二維度的清單，清單中還有清單

#讓使用者輸入
products = [] #2
while True: #1
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price =input('請輸入商品價格: ') #4
	price = int(price)
	#p = [] #5建立小清單
	#p.append(name)
	#p.append(price)
	# p = [name, price] 等同9~11行
	#products.append(p)#3 --> #6把本來的name改成p
	products.append([name, price]) #把9~13行替換掉
print(products)

	#products[0][0] #products第0格清單中的第0格 --> 就是第0個商品的名字取出

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是', p[1]) #印出products裡面的小清單p

	#字串可以用加和乘 'a' + 'b' = 'ab' , 'a' * 3 = 'aaa'

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #f是這個寫csv檔的稱呼,打開csv撰寫後存成f 
	#如果存檔時出現亂碼,可以在後方加入utf-8編碼
	#把csv的檔案加上欄位名稱
	f.write('商品,價格\n') 
	for p in products: #一個個存取清單中的資料
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n是分行,f.write代表真的寫入, ','作用為字串分隔



