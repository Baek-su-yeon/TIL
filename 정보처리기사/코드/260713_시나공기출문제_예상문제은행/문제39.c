#include <stdio.h>
#define MAX_SIZE 10

int isWhat[MAX_SIZE];
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
	if (isFull() == 1) printf("Full");
	else isWhat[++point] = num;
}

int take() {
	if (isEmpty() == 1) printf("Empty");
	else return isWhat[point--];
	return 0;
}

main() {
	into(5); into(2); // isWhat = {5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0}, point = 1
	while (!isEmpty()) {
		printf("%d", take()); // point = 1 실행 후 0 
		into(4); into(1); printf("%d", take());
		// isWhat = {5, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0}, point = 2 실행 후 1
		into(3); printf("%d", take()); printf("%d", take());
		// isWhat = {5, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0}, point = 2 실행 후 1 실행 후 0
		into(6); printf("%d", take()); printf("%d", take());
		// isWhat = {5, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0}, point = 1 실행 후 0 실행 후 -1
	}
}

// 답
// 213265