data = []
count = 0
with open('reviews.txt','r') as f: 
	for line in f:
		data.append(line)
		count += 1
		#if count % 1000 == 0:
		 	 #print(len(data))
print('檔案讀取完畢,總共有', len(data),'筆資料')

#算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	#print(sum_len)

print('留言的平均長度是',sum_len/len(data))	

#篩選留言長度小於100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言長度小於100')	
print(new[0])
print(new[1])	

#篩選有說good的
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到good')		
print(good[0])		

###清單快寫法
#留言中有提到bad的
bad = [ d for d in data if 'bad' in d]
print(bad[1])
print('一共有',len(bad),'筆留言提到bad')
#全部留言中是否提到look
look = [ 'look' in d for d in data] 
print(look[0])
