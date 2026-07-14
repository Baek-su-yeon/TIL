public class Main {
	public static void main(String[ ] args) {
		new Child( );
		System.out.println(Parent.total);
	}
}
class Parent {
	static int total = 0; // 4. 0 -> 2 -> 6
	int v = 1; // 3. 1 -> 2
	public Parent( ) {
		// 2. 그래서 new Child()후 가장 먼저 실행됨
		total += ++v;
		show( ); // 5. 오버라이딩된 메서드로, 실행 시 실제 객체 기준으로 실행됨
	}
	public void show( ) {
		total += total;
	}
}
class Child extends Parent {
	int v = 10; // 8. 10 -> 12
	public Child( ) {
		// 1. new child()로 인해 생성자 실행되는데
		// 1. java는 자식 클래스의 생성자 실행 시 가장 먼저 super()가 명시되어 있지 않아도 자동으로 실행
		// 7. 부모 생성자 끝나면 이제 실행
		v += 2;
		total += v++; // 9. 6 -> 18, v = 12 -> 13
		show( );
		}
	@Override
	public void show( ) {
		// 6. total = 2 + (2 * 2) = 6
		// 10. total = 18 + (18 * 2) = 36 + 18 = 54
		total += total * 2;
	}
}

// 답
// 54