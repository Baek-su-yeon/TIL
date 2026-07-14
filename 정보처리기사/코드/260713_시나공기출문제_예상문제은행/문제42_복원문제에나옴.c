#include <stdio.h>
void func(char *d, char *s) {
	while (*s) {
		// teststring의 앞 5글자를 first로 바꿈
		*d = *s;
		d++;
		s++;
	}
	// 5글자 first를 바꾼 후 마지막 6번째 글자도 '\0'으로 변경
	*d = '\0';
}
int main( ) {
	char* str1 = "first";
	char str2[50] = "teststring";
	int result = 0;
	func(str2, str1);
	for (int i = 0; str2[i] != '\0'; i++) {
		// 현재 str2 = first\0ring\0
		result += i; // 0 + 1 + 2 + 3 + 4
	}
	printf("%d\n", result); 
	return 0;
}

// 답
// 10