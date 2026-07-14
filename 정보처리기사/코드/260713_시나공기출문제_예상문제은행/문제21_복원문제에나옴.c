#include <stdio.h>
#include <stdlib.h>
void set(int** arr, int* data, int rows, int cols) {
	for (int i = 0; i < rows * cols; ++i) {
		arr[((i + 1) / rows) % rows][(i + 1) % cols] = data[i];
		// ((i + 1) / rows) % rows = 1 / 3 % 3 = 0
		// (i + 1) % cols = 1 % 3 = 1
		// 즉 arr[0][1]부터 값을 채우기 시작해서 마지막에 i = 8이 되면 arr[0][0]에 data[8]의 값을 채움
	}
}
int main( ) {
	int rows = 3, cols = 3, sum = 0;
	int data[] = {5, 2, 7, 4, 1, 8, 3, 6, 9};
	int** arr;
	arr = (int**) malloc(sizeof(int*) * rows);
	for (int i = 0; i < cols; i++) {
		arr[i] = (int*) malloc(sizeof(int) * cols);
	}
	// 여기까지 실행되면 arr[3][3] 메모리 공간 확보된 것
	set(arr, data, rows, cols);
	// arr = [[9,5,2],[7,4,1],[8,3,6]]
	for (int i = 0; i < rows * cols; i++) {
		sum += arr[i / rows][i % cols] * (i % 2 == 0 ? 1 : -1);
		// arr[0][0]부터 arr[2][2]까지 순회하면서 i가 짝수면 더하고, 홀수면 빼라
		// sum = 9 - 5 + 2 - 7 + 4 - 1 + 8 - 3 + 6 = 13
	}
	for(int i = 0; i < rows; i++) {
		free(arr[i]); // 할당된 공간 비움
	}
	free(arr);
	printf("%d", sum);
}

// 답
// 13