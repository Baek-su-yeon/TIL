public class Main {
	public static void main(String[ ] args) {
		int a = 5, b = 0;
		try {
			System.out.print(a/b); // 5 / 0 이므로 계산 불가
		}
		catch(ArithmeticException e){
			// ArithmeticException: 계산 오류
			System.out.print("출력1");
		}
		catch(ArrayIndexOutOfBoundsException e) {
			// ArrayIndexOutOfBoundsException: 배열 범위 초과 오류
			System.out.print("출력2");
		}
		catch(NumberFormatException e) {
			// NumberFormatException: 숫자 변환 불가한 형태일 때 발생하는 오류
			System.out.print("출력3");
		}
		catch(Exception e) {
			System.out.print("출력4");
		}
		finally {
			System.out.print("출력5");
		}
	}
}

// 답
// 출력1출력5