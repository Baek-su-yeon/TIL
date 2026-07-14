a = [1, 2, 3, 4, 5]
x = 100
if x == 10:
	a = list(map(lambda num : num + 10, a))
elif x == 50:
	a = list(map(lambda num : num + 50, a))
else: # x = 100 이어서 여기 실행
	a = list(map(lambda num : num + 100, a))
	# map(함수, 반복가능한 객체)
	# lambda 매개변수:반환할_표현식
	# a 리스트 안에 원소들 하나씩 꺼내서 100더한 후 리스트로 출력
print(a)
# 답: [101, 102, 103, 104, 105]