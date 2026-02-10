// Program to take user input and display it 
// Program - 1
# include <stdio.h>
int main() {
    char name[50];
    printf("What is your name ? \n ");
    scanf("%s", name );
    printf("Hello ! %s",name);
    return 0;
}


// Program to display sum of two digits by taking two numbers as user input 
# include <stdio.h>
int main(){
int num1 , num2 , sum ;
    printf("Enter first number: \n ");
    scanf("%d", &num1 );
    printf("Enter second number: \n");
    scanf("%d", &num2);
    sum = num1 + num2 ;
    printf("Sum of %d and %d is = %d " , num1, num2 , sum );
}




