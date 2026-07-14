class P {
	public int calc(int n) {
		if (n <= 1) return n;
		return calc(n - 1) + calc(n - 2);
	}
}
class C extends P {
	public int calc(int n) {
		if (n <= 1) return n;
		return calc(n - 1) + calc(n - 3);
		// calc(6) + calc(4)
		// = calc(5) + calc(3) + calc(3) + calc(1)
		// = calc(4) + calc(2) + calc(2) + calc(0) + calc(2) + calc(0) + 1
		// = 1 + 0 + 0 + 0 + 0 + 0 + 1 = 2
	}
}
public class Test {
	public static void main(String[] args) {
		P obj = new C();
		System.out.print(obj.calc(7));
	}
}

// 답
// 2