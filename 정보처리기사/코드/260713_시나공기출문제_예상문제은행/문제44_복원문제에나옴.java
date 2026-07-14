interface Number {
	int sum(int[] a, boolean odd);
}
public class Test {
	public static void main(String[] args) {
		int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		OENumber OE = new OENumber( );
		System.out.print(OE.sum(a, true) + ", " + OE.sum(a, false));
	}
}
class OENumber implements Number {
	public int sum(int[] a, boolean odd) {
		int result = 0;
		for (int i = 0; i < a.length; i++) {
			if ((odd && a[i] % 2 != 0) || (!odd && a[i] % 2 == 0)) {
				// odd = true면 a 배열의 홀수 인덱스만 더하기
				// odd = false면 a 배열의 짝수 인덱스만 더하기
				result += a[i];
			}
		}
		return result;
	}
}

// 답
// 20, 25