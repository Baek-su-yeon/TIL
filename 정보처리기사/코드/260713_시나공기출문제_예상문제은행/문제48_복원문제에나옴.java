public class Main{
	static String[] x = new String[3];
	static void func(String[] x, int y) {
		for(int i = 1; i < y; i++) {
			if(x[i-1].equals(x[i])) {
				// x[0]과x[1] 그리고 x[1]과x[2]의 값이 같은지? 주소는 상관 없음
				System.out.print("O");
			}
			else {
				System.out.print("N");
			}
		}
		for (String z : x) {
			// x 배열 순차적으로 뽑아서 출력해라
			System.out.print(z);
		}
	}
	public static void main(String[] args) {
		x[0] = "A";
		x[1] = "A";
		x[2] = new String("A");
		func(x, 3);
	}
}

// 답
// OOAAA