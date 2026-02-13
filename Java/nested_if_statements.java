// Use any editor to run 
// Give input in the bool datatype as mentioned 
// Filename and class name is CheckDetails 

import java.util.Scanner;
class CheckDetails {
    public static void main(String[] args) {
    Scanner scr = new Scanner(System.in);
    System.out.println(" WaTer Pool , Mysuru ");
    System.out.println(" Hello Swimmer !! Welcome ");
    System.out.println("******[NOTE:PLEASE TAKE THIS TEST]*******");
    System.out.println("Do you suffered any fever from last 1 week ? *(type true or false)*");
    boolean answer = scr.nextBoolean();
    if( answer==true){
        System.out.println("Kindly take the temperature  test in the inside block !!");
      } else if(answer==false){
           System.out.println("You can move to ticket counter for single test ");
      }
      System.out.println("Enter a deducted  temperature - ");
    float temperature = scr.nextFloat();
        if(temperature < 32.0 ){
        System.out.println("      You can swim,Collect your ticket from VM"); 
       System.out.println("---Swim with safety--- ");
        }else{
            System.out.println("Oops ! You can't swim now, Get well soon. ");
        }
    }
}
// code ends here 
