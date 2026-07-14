public class Main {
	public static void main(String[] args) {
		int sum = 0;
		try {
			// 무조건 일단 한번 실행
			func( );
		}
		catch (NullPointerException e) {
			// Exception 보다 하위의 예외인 NullPointerException이 잡혀서 실행
			sum = sum + 1;
		}
		catch (Exception e) {
			// 이미 위의 catch 문이 실행됐으므로 실행 X
			sum = sum + 10;
		}
		finally {
			// 무조건 마지막에 실행
			sum = sum + 100;
		}
		System.out.print(sum); // sum = 0 -> 1 -> 101
	}
	static void func( ) throws Exception {
		throw new NullPointerException( ); // null인 참조로 객체의 필드나 메서드 등에 접근할 때 발생
		// 즉, 이 함수는 그냥 실행되면 적힌 예외를 뱉는 함수임
	}
}

// 답
// 101