def calculater(number1,number2,option):
    if option==1:
        result= number1 + number2
        return result
    elif option==2:
        result= number1 * number2
        return result 
    elif option==3:
        result= number1 - number2
        return result 
    elif option==4:
        
        while number2==0:
            number2=raw_input("undefined, so please enter the second number again: ")
            number2=int(number2)
        result= number1 / number2
        return result

flag=1 
          
while  flag==1:   
     first_number = raw_input("enter the first number: ") 
     second_number =raw_input("enter the second number: ") 
     print("choose (1) for addition, (2) for multiplication ,(3) for subtraction,(4) for divition")
     selection =raw_input("enter your choice: ") 
     first_number=float(first_number) 
     second_number=float(second_number)  
     selection=int(selection)
     print("the result is: ")
     print(calculater(first_number,second_number,selection))
     flag2=raw_input("do you want to select another option for the same input??enter (1) for YSE or enter (0) for NO: ")
     flag2=int(flag2)
     
     while flag2==1:
        print("choose (1) for addition, (2) for multiplication ,(3) for subtraction,(4) for divition")
        selection =raw_input("enter your choice: ")
        selection=int(selection)
        print(calculater(first_number,second_number,selection))
        flag2=raw_input("if you want to choose another option enter (1) else enter (0): ")
        flag2=int(flag2)
        
     flag=raw_input("if you want to calculate other numbers enter (1) else enter (0): ")
     flag=int(flag)
 

   