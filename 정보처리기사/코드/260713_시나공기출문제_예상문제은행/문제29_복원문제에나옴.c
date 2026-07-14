#include <stdio.h>
#include <stdlib.h>

struct node {
	char c;
	struct node* p;
};

struct node* func(char* s) {
	struct node* h = NULL, *n;
	// B E S T를 순차적으로 접근하면서 node로 연결
	// 즉 h(= n) -> T -> S -> E -> B -> NULL 인 연결된 노드 생성
	while(*s) {
		n = malloc(sizeof(struct node));
		n -> c = *s++;
		n -> p = h;
		h = n;
	}
	return h;
}

int main( ) {
	struct node* n = func("BEST");
	// T부터 B까지 한글자씩 출력하면서 연결된 노드 타고 이동 NULL이면 끝
	// 즉 BEST를 뒤집어서 출력하게됨
	while(n) {
		putchar(n -> c);
		struct node* t = n;
		n = n -> p;
		free(t);
	}
		return 0;
}

// 답
// TSEB