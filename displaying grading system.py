#program to display a gradind system
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
avg=(sub1+sub2+sub3)/3
if(avg>=70)and(avg<=100):
    print("Grade: A")
elif(avg>=60)and(avg<=69):
    print("Grade: B")
elif(avg>=50)and(avg<=59):
    print("Grade: C")
elif(avg>=40)and(avg<=49):
    print("Grade: D")
else:
    print("Grade: Fall")