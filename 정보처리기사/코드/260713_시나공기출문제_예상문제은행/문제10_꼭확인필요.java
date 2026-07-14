public class Problem {
	public static void main(String[] args) {
		int a = 035, b = 0x35, c = 35;
		// a는 8진수 or 16진수
		// b는 16진수
		// c는 10진수
		System.out.printf("%d\n", a);
		// 까먹음 나중에 답보고 외워라
		// 8진수면 3 * 8 + 5 * 1 = 24 + 5 = 29
		// 16진수면 아래랑 동일
		System.out.printf("%d\n", b);
		// 0x35 = 3 * 16 + 5 * 1 = 48 + 5  = 53
		System.out.printf("%d\n", c);
		// 10진수 35 그대로 출력
	}
}

// 답
// 8진수나 16진수 둘 중 하나 출력
// 53
// 35
