#include <stdio.h>
int main( ) {
	int arr[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	// arr 내부형태
	// arr[0] = [[1,2,3],
	// arr[1] = [4,5,6],
	// arr[2] = [7,8,9]]
	int* parr[2] = {arr[1], arr[2]}; // parr[0]과 parr[1]은 &arr[1][0], &arr[2][0]를 가지고 있는 것
	printf("%d", parr[1][1] + *(parr[1]+2) + **parr);
	// parr[1][1] = arr[2][1] = 8
	// *(parr[1] + 2): parr[1] + 2 = &arr[2][0] + 2 = &arr[2][2] -> *(&arr[2][2]) = arr[2][2] = 9 
	// **parr: *parr = &arr[1][0] -> **parr = arr[1][0] = 4
}

// 답
// 21