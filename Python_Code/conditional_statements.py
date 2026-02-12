# Usage of conditional statements if..else to find out given year is leap year or not
year = int(input("Enter year to find whether it is leap year or not :  "))  
if (year % 400== 0) or (year % 4 == 0 and year % 100 != 0) :
    print("Given year , " , year, " is a leap year ")
else :
    print("Given year , " , year ,"is not a leap year " )
  
# Output 
''' Enter year to find whether it is leap year or not :  1996
Given year , 1996 is a leap year '''
''' Enter year to find whether it is leap year or not :  2026
Given year , 2026 is a  not leap year '''

# Usage of if..elif..else by taking the traffic colors from user and to predict the colors ' 
print("---- Traffic Guidelines ----")
traffic = str(input("Enter the color to know the meaning : " ))
if traffic=="green":
    print("Move !")
elif traffic=="red" :
    print("Stop ! wait for another signal ")
elif traffic=="yellow":
    print(" Get ready to go ! ")
else :
    print("Invalid ! ")
    
 ''' Output   
---- Traffic Guidelines ----
Enter the color to know the meaning : green 
Move ! '''
---- Traffic Guidelines ----
Enter the color to know the meaning : yellow
Get ready to go ! '''
---- Traffic Guidelines ----
Enter the color to know the meaning : blue
Invalid  ! '''




