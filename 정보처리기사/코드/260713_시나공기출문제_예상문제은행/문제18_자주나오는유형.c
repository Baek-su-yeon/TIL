#include <stdio.h>
struct Node {
	int value;
	struct Node* next;
};
void func(struct Node* node){
	// while문은 node가 비었거나, 연결된 node가 없으면 중단됨
	while(node != NULL && node -> next != NULL) { // n2는 연결된 노드가 없으므로 중단
		// 아래부터 각 변수의 변경되는 과정을 기술
		int t = node -> value; // t = n1.value = 1
		node -> value = node -> next -> value; // n1.value = n3.value = 3
		node -> next -> value = t; // n3.value = 1
		node = node -> next -> next; // node = node -> next = n3.next = n2
	}
}
int main( ) {
	struct Node n1 = {1, NULL};
	struct Node n2 = {2, NULL};
	struct Node n3 = {3, NULL};
	n1.next = &n3;
	n3.next = &n2;
	// 여기까지 실행되면 각 노드의 상태는 n1 -> n3 -> n2로 연결되어 있음
	func(&n1);
	struct Node* current = &n1;
	// while문은 current가 가리키는 node가 비어있으면 중단
	// 즉 n1 -> n3 -> n2 차례로 node를 순회하면서 각 노드의 value 출력할 것
	while(current != NULL){
		printf("%d", current -> value);
		current = current -> next;
	}
	return 0;
}

// 답
// 3
// 1
// 2