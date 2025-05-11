#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>  // for malloc


int main() {
    char* hello = (char*)malloc(20);
    if (hello == NULL) {
        printf("malloc failed\n");
        return 1;
    }

    printf("Heap: %p\n", hello);
    getch();
    free(hello);
    return 0;
}
