#include <stdio.h>
#include <stdlib.h>

main(int argc, char *argv[]) {
	int v1 = 0;
	int v2 = 35;
	int v3 = 29;
	if (v1 > v2 ? v2 : v1)
		v2 = v2 << 2;
	else
		v3 = v3 << 2;
		// v3 = 29 = 11101 << 2 -> 1110100
		// 그냥 << 1는 그 수에 *2와 같음 즉, 29 * 2 * 2 = 116
	printf("%d", v2 + v3);
	return 0;
}

// 답
// 151