public class Problem {
	public static void main(String[] args) {
		int a, b = 10;
		a = 20 % 11 / 3 * 5 - b;
		// 연산자 우선순위 따지는 문제인데 우선순위 까먹은 듯 일단 걍 품
		// java / 연산은 연산 후 실수형으로 안바뀌는지 확인 필요
		// 20 % 11 = 9 / 3 = 3 * 5 = 15 - 10 = 5
		System.out.printf("%d\n", a);
	}
}

// 답
// 5