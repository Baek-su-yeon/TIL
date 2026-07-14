#include <stdio.h>
struct Test {
	int i;
	const char *g;
};
int main( ) {
	struct Test test[ ] = {{1, "AB"}, {2, "DC"}, {3, "EB"}};
	struct Test *p = &test[1];
	printf("%s", p->g + (p->i - 1));
	// p -> g = &test[1].g 즉, "DC"의 시작 주소를 "D"를 가리킴
	// p -> i - 1 = test[1].i = 2 - 1 = 1
	// "D"의 주소 + 1 = "C"
	return 0;
}

// 답
// C