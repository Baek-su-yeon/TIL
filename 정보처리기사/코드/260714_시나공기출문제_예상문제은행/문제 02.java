class Parent { 
	void show( ) { System.out.println("parent"); }
}
class Child extends Parent { 
	void show( ) {  System.out.println("child"); }
}
public class Test {
	public static void main(String[ ] args) {
		Parent pa = new Child( ); // 선언: Parent, 실제 객체: Child
		pa.show( );
		// show는 Child에 오버라이딩되어있음
		// 컴파일 시에는 Parent의 show 함수가 선택되나
		// 실제 실행 시에는 오버라이딩된 Child의 show 함수 실행
	}
}

// 답
// child