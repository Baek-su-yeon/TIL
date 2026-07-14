def cnt(str, p):
	# str 문장에서 p의 길이만큼 슬라이싱 했을 때
	# p의 글자와 동일한 sub 개수 출력
	result = 0
	for i in range(len(str)):
		sub = str[i:i+len(p)]
		if sub == p:
			result += 1
	return result
str = "abdcabcabca"
p1 = "ca"
p2 = "ab"
print(f'ab{cnt(str, p1)} ca{cnt(str, p2)}')

# 답
# ab3 ca3