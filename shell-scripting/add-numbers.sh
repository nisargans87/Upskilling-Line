# Shell Script to print sum of assigned values to variables 
#!/bin/bash
# Assign values
num1=25
num2=15
# Add numbers
sum=$((num1 + num2))
# Print result
echo "Sum is: $sum"


# Shell Script to print sum of user given  values 
#!/bin/bash
# Take input from user
echo "Enter first number:"
read num1
echo "Enter second number:"
read num2
# Addition
sum=$((num1 + num2))
# Display result
echo "Sum is: $sum"
