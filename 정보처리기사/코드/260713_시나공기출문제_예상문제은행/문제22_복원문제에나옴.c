#include <stdio.h>

typedef struct student {
	char* name;
	int score[3];
} Student;

int dec(int enc) {
	return enc & 0xA5;
}

int sum(Student* p) {
	return dec(p->score[0]) + dec(p->score[1]) + dec(p->score[2]);
}

int main( ) {
	Student s[2] = { "Kim", {0xA0, 0xA5, 0xDB}, "Lee", {0xA0, 0xED, 0x81} };
	Student* p = s;
	int result = 0;
	for (int i = 0; i < 2; i++) {
		result += sum(&s[i]);
	}
	printf("%d", result);
	return 0;
}

// s[]에 순차적으로 접근해서 각 s의 score들을 0x45와 비트 and 연산하는 코드
// 16진수로 표현된 점수를 2진수로 변환해서 and 연산 후 10진수로 다시 변환해서 더해야함
// 16진수에서 10진수 10부터는 A로 표기 (10 = A ~ 15 = F)
// 0xA0 = 10 0 = 1010 0000
// 0xA5 = 10 5 = 1010 0101
// 0xDB = 13 11 = 1101 1011
// 0xED = 14 13 = 1110 1101
// 0x81 = 1000 0001

// 0xA0 & 0xA5 = 1010 0000 = 0xA0 = 10 * 16 + 0 * 1 = 160
// 0xA5 & 0xA5 = 1010 0101 = 0xA5 = 10 * 16 + 5 * 1 = 165
// 0xDB & 0xA5 = 1000 0001 = 8 * 16 + 1 * 1 = 129
// 0xED & 0xA5 = 1010 0101 = 0xA5 = 165
// 0x81 & 0xA5 = 1000 0001 = 129

// result = 160+165+129+160+165+129
// 이거 꼼수 없는지 확인, 시간 너무 오래 걸림

// 답
// 908