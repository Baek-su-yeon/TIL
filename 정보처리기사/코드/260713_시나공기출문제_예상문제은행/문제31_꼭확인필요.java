public class Test {
	public static void main(String[] args) {
		String str1 = "Programming";
		String str2 = "Programming";
		String str3 = new String("Programming");
		// ==: 주소가 동일한가
		System.out.println(str1==str2); // str2 할당 시 str2 = str1 이었으면 true 일 듯..?
		System.out.println(str1==str3);
		// equals: 값이 동일한가
		System.out.println(str1.equals(str3));
		System.out.println(str2.equals(str3));
	}
}

// 답
// false
// false
// true
// true