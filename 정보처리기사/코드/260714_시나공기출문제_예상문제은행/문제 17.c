#include <stdio.h>
#include <string.h>

void inverse(char *str, int len) {
	// 문장 앞,뒤 뒤집는 함수
	for(int i = 0, j = len - 1; i < j; i++, j--) {
		char ch = str[i];
		str[i] = str[j];
		str[j] = ch;
	}
}

int main() {
	char str[100] = "ABCDEFGH";
	int len = strlen(str); // 8
	inverse(str, len);
	for(int i = 1; i < len; i += 2) {
		// HGFEDCBA 글자를 G부터 2칸씩 넘어가면서 출력
		printf("%c", str[i]);
	}
	return 0;
}

// 답
// GECA

