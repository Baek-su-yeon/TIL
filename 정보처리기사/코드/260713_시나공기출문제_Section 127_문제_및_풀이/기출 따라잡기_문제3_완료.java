public class Main {
	static interface F {
		// F 타입의 객체를 만들려면 apply(int x)를 구현해야 한다는 약속
		int apply(int x) throws Exception;
	}
	public static int run(F f) {
		// F 형을 매개변수로 입력받으면 f.apply(3)을 실행
		// 예외가 발생할 경우 7 출력
		try {
			return f.apply(3);
		} catch (Exception e) {
			return 7;
		}
	}
	public static void main(String[] args) {
		// 인터페이스 F의 메서드 apply를 java 람다식으로 표현한 것
		// java 람다식 기본 문법은 (매개변수) -> {실행식}
		// 즉, apply에 매개변수가 입력되었을 때 2보다 크면 예외처리, 아니면 *2
		F f = (x) -> {
			if (x > 2) {
				throw new Exception( );
			}
			return x * 2;
		};
		System.out.print(run(f) + run((int n) -> n + 9));
		// run(f): f.apply(3) -> 3 > 2 이므로 Exception() throw -> 7
		// (int n) -> n + 9): run 함수가 매개변수로 받을 새로운 F 객체를 만들어 전달
		// run((int n) -> n + 9): f.apply(3) -> 3 + 9 > 12
		// 7 + 12 = 19
	}
}

// 답
// 19