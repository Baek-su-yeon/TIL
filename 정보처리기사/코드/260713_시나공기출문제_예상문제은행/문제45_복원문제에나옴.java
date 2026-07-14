public class Test {
	public static String rf(String str, int index, boolean[] seen) {
		if(index < 0) return "";
		char c = str.charAt(index); // str배열에서 index 글자 뽑기
		String result = rf(str, index-1, seen);
		if(!seen[c]) {
			// 즉, 재귀함수 실행하면서 나왔던 문자면 출력 안한다
			// 중복된 글자 다 빠지고 출력될 것임
			seen[c] = true;
			return c + result;
		}
		return result;
	}
	public static void main(String[] args) {
		String str = "abacabcd";
		int len = str.length( ); // 8
		boolean[] seen = new boolean[256];
		System.out.print(rf(str, len-1, seen));
	}
}

// 답
// abcd