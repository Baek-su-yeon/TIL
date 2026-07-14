public class Test {
	public static void main(String[] args) {
		int i = 0, c = 0;
		while (i < 10) {
			i++;
			c *= i; // c의 초기값이 0이라서 i 값이 달라지던 말던 곱하면 0임
		}
		System.out.println(c);
	}
}

// 답
// 0