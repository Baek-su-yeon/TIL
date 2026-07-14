def calc(x, y):
	# 매개변수 x, y를 3으로 곱한 값과 나눈 값을 출력하는 함수
	x *= 3
	y /= 3 # 🚩파이썬의 / 연산자는 항상 실수형 결과 변환
	print(x, y)
	return x
a, b = 3, 12
a = calc(a, b) # x *= 3의 결과만 출력되어 x에 할당, b의 값은 바뀌지 않음
print(a, b)

# 답
# 9 4.0 (해당 출력은 calc 함수 내부의 print(x, y) 결과)
# 9 12 (해당 출력은 print(a, b)의 결과)