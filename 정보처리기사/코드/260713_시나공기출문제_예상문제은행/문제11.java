public class Problem {
	public static void main(String[] args) {
		int j, k, L, result;
		j = 10;
		k = 20;
		L = 30;
		result = j < k ? k++ : --L; // j가 k보다 작으면 k++ 실행 후 할당, 아니면 --L 실행 후 할당
		System.out.printf("%d %d %d\n", result, k, L);
	}
}

// 답
// 21 21 30