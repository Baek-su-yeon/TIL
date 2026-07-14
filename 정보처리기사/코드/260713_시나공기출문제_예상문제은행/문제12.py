a = sum = 0
while a < 10:
	# a가 짝수일 때만 sum에 합
	a += 1
	if a%2 == 1:
		continue
	sum += a # 2 + 4 + 6 + 8 + 10 = 30
print(sum)

# 답
# 30