public class Test {
	public static void main(String[] args) {
		String str = "ITISTESTSTRING";
		String[] result = str.split("T");
		// T를 기준으로 str을 나눠서 배열에 저장
		// result = [[I],[IS],[ES],[S],[RING]]
		System.out.print(result[3]);
	}
}

// 답
// S