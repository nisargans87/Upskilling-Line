# Declaration of Function and Calling Function without passing an arguments 
# Simple Function usage 1 
def FunctionCreation():
    print("Learnt , Applied and now Learning ! ")
FunctionCreation()
# indentation matters here too  
''' Output - Learnt , Applied and now Learning ! '''
def FunctionCreation():
    print("Learnt , Applied and now Learning ! ")
    FunctionCreation()
  ''' Displays Blank Screen '''

# Simple Function usage  2
def A():
    print("First  Letter of the Alphabet is " , A)
    print(type(A),id(A))
A()
''' Output - First  Letter of the Alphabet is  <function A at 0x7904114bc220>
<class 'function'> 133058377007648 '''


# Simple function usage 3
def NumberCheck ():
    num=int(input("Enter a number : "))
    if num%2==0 :
        print("The number is even i.e " , num )
    else :
        print("The number is odd i.e", num)
        print(type(num),type(NumberCheck),type(print),type(input))
NumberCheck()
''' Output - '''

# Simple function usage 4 
def ListCheck ():
    collection = [11,22,33,44]
    print("The collection of number in the list is ", collection)
    print(type(collection))
ListCheck()


