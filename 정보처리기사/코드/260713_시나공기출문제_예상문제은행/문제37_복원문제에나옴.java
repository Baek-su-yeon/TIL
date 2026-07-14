// enum: 지정된 데이터형만 쓸 수 있는 자료형
enum Tri {
	A("A"), B("AB"), C("ABC"); // Tri에서 사용할 수 있는 데이터형 A, B, C
	private String code;
		Tri(String code) {
	this.code = code; // Tri.A.code = "A", Tri.B.code = "AB", Tri.C.code = "ABC"
	}
	public String code( ) {
		return code;
	}
}
public class Main {
	public static void main(String[] args) {
		Tri t = Tri.values( )[Tri.A.name( ).length( )];
		// Tri.values(): enum Tri의 데이터들의 배열 출력 = [Tri.A, Tri.B, Tri.C]
		// Tri.A.name(): A의 이름 자체 "A" 출력
		// 즉, Tri.values()[1] = t = Tri.B
		System.out.print(t.code( )); // Tri.B.code = "AB"
	}
}

// 답
// AB