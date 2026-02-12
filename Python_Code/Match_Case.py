''' Match Case demonstration ( python3.10 )
 Program consisting of Match Case , which checks exact match between the entered email, password with already set email and password respectively '''

enter_email=str(input("Enter your registered email id --  "))
enter_password = str(input("Enter password -- "))
set_password = "qrty65₹N"
set_email = "nisargans011@gmail.com"
match enter_password , enter_email :
    case  "qrty65₹N","nisargans011@gmail.com" :
        print("Login Successfully !")
    case _ :
        print(" Invalid Password or email !, Try Again ")
      # code ends here 
      
