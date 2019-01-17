data = []
count = 0
with open('reviews.txt','r') as f: 
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
		 	 #print(len(data))
print('檔案讀取完畢,總共有', len(data),'筆資料')
print(data[0])

#文字記數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word]+=1
		else:	
			wc[word]= 1 #新增key進wc字典
for word in wc:
	if wc[word] >1000000:
		print(word,wc[word])
print(len(wc))		
print(wc['Allen'])
while True:
	word = input('請輸入你要查的字: ')
	if word == 'q':
		print('感謝使用')
		break
	if word in wc:	
		print(word,'出現過',wc[word],'次')
	else:
		print(word,'這個字沒出現過!')	