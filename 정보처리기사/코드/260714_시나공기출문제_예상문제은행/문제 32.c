#include <stdio.h>
main( ) {
	int field[4][4] = { {0,1,0,1}, {0,0,0,1}, {1,1,1,0}, {0,1,1,1} };
	int mines[4][4] = { {0,0,0,0}, {0,0,0,0}, {0,0,0,0}, {0,0,0,0} };
	int w = 4, h = 4;
	for (int y = 0; y < h; y++) {
		for (int x = 0; x < w; x++) {
			if (field[y][x] == 0) continue;
			for (int j = y - 1; j <= y + 1; j++) { 
				for (int i = x - 1; i <= x + 1; i++) {
					if (chkover(w, h, j, i) == 1)
						mines[j][i] += 1;
				}
			}
		}
	}
}

int chkover(int w, int h, int j, int i) {
	// 즉 i,j 좌표가 필드(w,h)를 안벗어나는지 확인
	if (i >= 0 && i < w && j >= 0 && j < h) return 1;
	return 0;
}

// 이건 답이 뭐 따로 출력하는게 없어서
// for문 모두 돌았을 때 mines 값을 적어둠, 코드에 따라 mines가 올바르게 바뀌었는지를 확인할 것
// int mines[4][4] = { {1,1,3,2}, {3,4,5,3}, {3,5,6,4}, {3,5,5,3} }