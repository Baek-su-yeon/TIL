#include <stdio.h>
main() {
	char* p = "KOREA";
	printf("1. %s\n", p);
	printf("2. %s\n", p + 1);
	printf("3. %c\n", *p);
	printf("4. %c\n", *(p + 3));
	printf("5. %c\n", *p + 4);
}

// 답
// 1. KOREA
// 2. OREA
// 3. K
// 4. E
// 5. O