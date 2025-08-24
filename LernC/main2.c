#include <stdio.h>

int main() {
    
    int a, b;
    char op;

    printf ("enter ? +-*/ ? ");
    scanf ("%d %c %d", &a , &op , &b);

    if (op == '+'){
        printf("thiss %d \n", a + b);
    }
    else if (op == '-'){
        printf("this %d \n", a - b);
    }
    else if (op == '*'){
        printf("thiss %d \n", a * b);
    }
    else if (op == '/'){
        printf("thiss %d /n", a / b);
    }
    else{
        printf ("what?");
    }
    return 0;  // โปรแกรมสิ้นสุด
}
