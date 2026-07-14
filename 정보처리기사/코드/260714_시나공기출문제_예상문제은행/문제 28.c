#include <stdio.h>
int func(int a) {
	if (a <= 1) return 1;
	return a * func(a - 1);
	// 5 * func(4)
	// 5 * 4 * func(3) ... 즉, a부터 1까지 곱하는 팩토리얼과 동일한 함수
}
int main() {
	int a;
	scanf("%d", &a);
	printf("%d", func(a));
}

// 답 (a = 5라고 가정)
// 120