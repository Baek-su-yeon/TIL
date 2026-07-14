#include <stdio.h>
char n[30];
char* getname() {
	printf("이름 입력 : ");
	gets(n);
	return n;
}

main() {
	char* n1 = getname();
	char* n2 = getname();
	char* n3 = getname();
	printf("%s\n", n1);
	printf("%s\n", n2);
	printf("%s\n", n3);
}

// 답
// getname()이 동일한 전역변수 n을 사용하므로
// 결국 가장 마지막에 입력된 n3의 값이 3번 출력될 것