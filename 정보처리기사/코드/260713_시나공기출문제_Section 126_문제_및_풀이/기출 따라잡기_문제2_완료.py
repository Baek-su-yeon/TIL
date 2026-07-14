def func(value):
	if type(value) == type(100): # type(100): 정수형
		return 100
	elif type(value) == type(""):
		return len(value) # func(a)의 결과로 5 출력
	else:
		return 20 # func(b), func(c)의 결과로 20 출력
a = "100.0" # 문자열형, 길이는 1 0 0 . 0 총 5
b = 100.0 # 실수형
c = (100, 200) # 튜플
print(func(a) + func(b) + func(c)) # 5 + 20 + 20

# 답
# 45