class Cls:
	x, y = 10, 20
	def chg(self):
		# x와 y를 바꾸는 함수
		# self.x = ..., self.y = ...가 실행되는 순간
		# a 객체 안에 인스턴스 변수 x, y가 새로 생긴다
		temp = self.x
		self.x = self.y
		self.y = temp
a = Cls( )
print(a.x, a.y)
a.chg( )
print(a.x, a.y)

# 답 (출력에 ',' 안나옴 주의)
# 10 20
# 20 10