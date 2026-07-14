#include <stdio.h>
#define MAX_SIZE 10

int isWhat[MAX_SIZE]; // isWhat[10]
int point = -1;

int isEmpty() {
	if (point == -1) return 1;
	return 0;
}

int isFull() {
	if (point == 10) return 1;
	return 0;
}

void into(int num) {
	// 스택 채우는 함수
	// point는 채워진 인덱스에 있게됨
	if (isFull() == 1) printf("Full");
	else isWhat[++point] = num;
}

int take() {
	// 실제로 값을 삭제하는거는 아님
	// point를 통해서 삭제될 값을 출력하고, point 이동만함
	if (isEmpty() == 1) printf("Empty");
	else return isWhat[point--];
	return 0;
}

main() {
	into(5); into(2); // isWhat = {5,2}, point = 1
	while (!isEmpty()) {
		printf("%d", take()); // isWhat = {5,2}, point = 0
		into(4); into(1); printf("%d", take()); // isWhat = {4,1}, point = 0
		into(3); printf("%d", take()); printf("%d", take()); // isWhat = {3,1}, point = -1
		into(6); printf("%d", take()); printf("%d", take()); // isWhat = {6,1}, point = -1
	}
}

// 답
// 21136Empty