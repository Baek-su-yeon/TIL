class Static {
	public int a = 20;
	static int b = 0;
}

public class Test {
	public static void main(String[] args) {
		int a = 10;
		Static.b = a; // 접근이 되나? 오류나는 코드를 주지는 않길래 바뀌었다 치고,,,
		Static st = new Static(); // 새로운 객체 생성
		System.out.println(Static.b++);
		System.out.println(st.b);
		System.out.println(a);
		System.out.print(st.a);
	}
}

// 답
// 10
// 11
// 10
// 20