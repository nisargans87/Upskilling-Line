//  Function calling by using pass by value type 
#include <stdio.h>
void increment (int num){
    num=num+1;
    printf("inside:%d\n",num);
}
int main() {
    int x=10;
    increment (x);
    printf("Outside:%d\n",x);
}
/* Output -
inside:11
Outside:10 */
  
