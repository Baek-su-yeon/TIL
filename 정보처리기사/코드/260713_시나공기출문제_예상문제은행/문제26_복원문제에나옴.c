#include <stdio.h>
#define SIZE 3

typedef struct {
	int a[SIZE];
	int front;
	int rear;
} Queue;

void enq(Queue* q, int val) {
	q -> a[q -> rear] = val;
	q -> rear = (q -> rear + 1) % SIZE;
}

int deq(Queue* q) {
	int val = q -> a[q -> front];
	q -> front = (q -> front + 1) % SIZE;
	return val;
}

int main( ) {
	// 큐 직접 구현한 코드
	Queue q = {{0}, 0, 0}; // 큐 리스트, front, rear 상태 표시
	enq(&q, 1); // 큐에 1 삽입, rear = 1
	enq(&q, 2); // 큐에 2 삽입, rear = 2
	deq(&q); // 1 출력, front = 1
	enq(&q, 3); // 큐에 3 삽입, rear = 3
	// 현 시점 q = {{1,2,3}, 1, 3}
	printf("%d 그리고 %d", deq(&q), deq(&q));
	return 0;
}

// 답
// 2 그리고 3