print("Perform Arithmetic Functions With ease")
value_1=float(input('Enter N.o '))
value_2=float(input('Enter N.o '))
operation_sign=input("Ener Sign ") 
def Solution():
    def Addition():
        sum=value_1 + value_2
        print("Sum is " + str(sum))
    

    def Substraction():
        sum=value_1 - value_2
        print("Difference is " + str(sum))    
    
    
    def Division():
        sum=value_1 / value_2
        print("Quotient is " + str(sum))  
 
    
    def Multiplication():
        sum=value_1 * value_2
        print("Mulitiple is " + str(sum)) 
        
    if operation_sign=='+':
        Addition()
    elif operation_sign=="-":
        Substraction()
    elif operation_sign=='*':
        Multiplication()
    elif operation_sign=='/':
        Division()
    else:
        print('Input correct sign ')   
    Solution()      
Solution()

    
    
 


    
        
        

