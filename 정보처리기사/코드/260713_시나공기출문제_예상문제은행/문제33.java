class Rectangle {
	int x, y; // 2. x = 10, y = 10
	Rectangle(int x, int y) {
		this.x = x;
		this.y = y;
	}
	int getArea( ) {
		return x*y;
	}
}
class Square extends Rectangle {
	Square(int a) {
		super(a, a); // 1. 부모 생성자에 10, 10 매개변수 입력
	}
	int getSquareArea( ) {
		return x*y;
	}
}
public class Main {
	public static void main(String[] args) {
		Square sq = new Square(10);
		System.out.println(sq.getSquareArea( ));
	}
}

// 답
// 100