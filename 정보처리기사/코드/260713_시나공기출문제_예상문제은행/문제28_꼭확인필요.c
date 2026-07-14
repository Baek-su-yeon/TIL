#include <stdio.h>
int isPerfectNum(int num) {
	int sum = 0;
	for (int i = 1; i < num; i++) {
		// num 본인을 제외한 약수의 총합
		if (num % i == 0)
			sum += i;
	}
	if (num == sum) return 1;
	// 총합이 num과 같을 때만 1
	else return 0;
}

main() {
	int r = 0;
	for (int i = 1; i <= 100; i++)
		if (isPerfectNum(i))
			r += i; // 1~100까지 i를 제외한 i의 약수의 총합이 i와 같은 수의 총합
	printf("%d", r);
}

// 답
// 이걸 시험장에서 다 더하고 있는게 맞는지, 꼼수 없는지 확인 필요
// 꼼수 없으면 현재 코드에 맞는 숫자 다 나열하기
// 1 ~ 100까지는 꽤 많이 나와서 1~100까지 총합, 1~100 중 약수가 1과 자신밖에 없는 수, 지금 문제의 경우는 걍 외우는게 나을 듯