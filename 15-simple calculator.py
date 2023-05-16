operation=input("yapmak istediginiz islem(+,-,*,/): ")

num1=float(input("bir sayi giriniz: "))
num2=float(input("bir sayı giriniz: "))

if operation=="+" :
    print(num1, "+", num2, "=", num2 + num1)
elif operation=="-" :
    print(num1,"-",num2,"=",num1-num2)
elif operation=="*":
    print(num1,"*",num2,"=",num2*num1)
elif operation=="/":
    print(num1,"/",num2,"=",num1/num2)
else :
    print("lütfen bir islem seciniz")


#comment