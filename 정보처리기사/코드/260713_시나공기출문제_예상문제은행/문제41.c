#include <stdio.h>
void swap(int a, int b) {
	// a,b 바꾸는 코드인데 지금 그냥 함수 내부의 지역변수들만 바뀜
	int t = a;
	a = b;
	b = t;
}
int main( ) {
	int a = 11;
	int b = 19;
	swap(a, b); // 즉 이거 해도 실제 main 함수의 a,b는 동일
	switch(a) {
		case 1:
			b += 1;
		case 11:
		// a = 11이므로 b = 21이 되고 break 문이 없어서 default까지 실행
			b += 2;
		default:
		// b = 24
			b += 3;
			break;
	}
	printf("%d", a-b);
}

// 답
// -13