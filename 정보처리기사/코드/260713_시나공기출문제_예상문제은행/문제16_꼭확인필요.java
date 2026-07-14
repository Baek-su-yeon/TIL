public class Problem {
	public static void main(String[] args){
		int a, b, c, hap;
		a = b = c = 2;
		hap = ++a | b-- & c--;
		// | 과 &는 비트 비교연산자로 우선순위가 꽤 낮음
		// 근데 b--, c--의 --가 해당 실행문의 모든 연산 끝나고 실행으로 알고있는데 나중에 다시 이해할 것
		// ++a | b-- -> 3 | 2 -> 11 | 10 -> 11
		// 11 & 2 -> 11 & 11 -> 11 -> 3 (10진수)
		// 이후 b와 c는 --로 인해 1로 변경
		System.out.printf("%d %d %d %d", hap, a, b, c);

		// 답
		// 3 3 1 1
	}
}