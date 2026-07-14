public class Main {
	public static class BO {
		public int v;
		public BO(int v) {
			this.v = v;
		}
	}
	public static void main(String[] args) {
		BO a = new BO(1); // a.v = 1
		BO b = new BO(2); // b.v = 2 -> 3
		BO c = new BO(3); // c.v = 3
		BO[] arr = {a, b, c};
		BO t = arr[0]; // t = a
		arr[0] = arr[2]; // arr = {a,b,c} -> {c,b,c}
		arr[2] = t; // {c,b,c} -> {c,b,a}
		arr[1].v = arr[0].v; // b.v = c.v = 3
		System.out.println(a.v + "a" + b.v + "b" + c.v);
	}
}

// 답
// 1a3b3