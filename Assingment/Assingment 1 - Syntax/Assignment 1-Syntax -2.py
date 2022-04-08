def Prime_Detector(num):
    flag=True
    if type(num)==int:
        all_nums=range(2 , round(num**0.5+1))
        for i in all_nums:
            if num%i==0:
                flag=False
    
    
    
    if type(num) ==str :
        raise Exception ('the input is in wrong format')
    elif num==1:
        print('being a prime number or not is not known for number one')
    elif flag==True:
        print('the input is a prime number')
    else:
        print('the input is not a prime number')

Prime_Detector(12)