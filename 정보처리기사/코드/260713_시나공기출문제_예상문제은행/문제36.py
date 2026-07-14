lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol[0])
print(lol[2][1])
for sub in lol: # lol 이중리스트를 한 행씩 뽑음
	for item in sub: # 한 행의 각 원소를 뽑음
		print(item, end=' ') # 각 원소를 하나씩 출력하는데 뒤에 ' ' 붙일 것
	print() # \n 대신 줄바꿈

# 답
# [1,2,3]
# 7
# 1 2 3
# 4 5
# 6 7 8 9