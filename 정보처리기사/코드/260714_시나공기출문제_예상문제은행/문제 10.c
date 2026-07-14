#include <stdio.h>
#include <ctype.h>

int main( ) {
	char *p = "It is 8";
	char result[100];
	int i;
	for(i = 0; p[i] != '\0'; i++) {
		if(isupper(p[i]))
			result[i] = (p[i] - 'A'+ 5) % 25 + 'A';
			// ('I' - 'A' + 5) % 25 + 'A' = 13 + 'A' = N
		else if(islower(p[i]))
			result[i] = (p[i] - 'a'+ 10) % 26 + 'a';
			// ('t' - 'a' + 10) % 26 + 'a' = 3 + 'a' = d 
			// ('i' - 'a' + 10) % 26 + 'a' = 18 + 'a' = s 
			// ('s' - 'a' + 10) % 26 + 'a' = 2 + 'a' = c 
		else if(isdigit(p[i]))
			result[i] = (p[i] - '0'+ 3) % 10 + '0';
			// ('8' - '0' + 3) % 10 + '0' = 1 + '0' = 1 
		else if(!(isupper(p[i]) || islower(p[i]) || isdigit(p[i])))
			result[i] = p[i];
	}
	result[i] = '\0';
	printf("변환된 문자열 : %s\n", result);
	return 0;
}

// 답
// Nd sc 1