public class Test {
	public static void main(String[] args) {
		int ary[][] = new int[3][5];
		int n = 1;
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 5; j++) {
			ary[i][j] = j * 3 + i + 1;
			// 1+0, 1+3, 1+6, 1+9, 1+12
			// 2+0, 2+3, 2+6, 2+9, 2+12
			// 3+0, 3+3, 3+6, 3+9, 3+12
			System.out.print(ary[i][j] + " ");
			}
			System.out.println();
		}
	}
}

// 답
// 1 4 7 10 13
// 2 5 8 11 14
// 3 6 9 12 15