#include <stdio.h>
int main() {
    int marks[3][3]={
    {85,90,78},
    {78,94,95},
    {56,78,34}
};
printf("students marks table\n");
printf("----------\n");
printf("Students|Sub1|Sub2|Sub3|\n");
printf("-----------\n");
for(int i=0;i<3;i++){
    printf("S%d |", i+1);
  for (int j=0;j<3;j++){
    printf("%d |",marks[i][j]);
  }
  printf("\n");
}
printf("--------------\n");
return 0;
  }

/* Output 
Students marks table
----------
Students|Sub1|Sub2|Sub3|
-----------
S1 |85 |90 |78 |
S2 |78 |94 |95 |
S3 |56 |78 |34 |
-------------- */
      


