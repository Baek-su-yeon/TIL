#include <stdio.h>
main() {
	int E[] = { 64, 25, 12, 22, 11 };
	int n = sizeof(E) / sizeof(E[0]);
	// int type size = 4, 이거 말고 다른 자료형 크기도 알고있으면 좋을 것 같으니 해설에 포함해줘
	// n = 20 / 4 = 5
	int i = 0; // 1
	do {
		int j = i + 1; // 1
		do {
			if (E[i] > E[j]) {
			int tmp = E[i];
			E[i] = E[j];
			E[j] = tmp;
			} // {25,64,12,22,11} -> {12,64,25,22,11} -> {11,64,25,22,12}
			j++; // j = 2 -> 3 -> 4
		} while (j < n);
		i++;
	} while (i < n - 1);
	// 결국 위에 do - while문 끝나면 E 오름차순 정렬됨

	for (int i = 0; i <= 4; i++)
		printf("%d ", E[i]);
}

// 답
// 11 12 22 25 64 