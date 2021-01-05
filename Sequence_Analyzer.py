print("Enter the first 3 digits")
a=int(input("1"))
b=int(input("2"))
c=int(input("3"))
dr4=0
rr4=0
l=0
if 2*b==(a+c):
    print("the series is in AP")
    d=b-a
    print(c+d,"is the next term")
    dr4=c+d
elif b**2==(a*c):
    print("The series is in GP")
    d=b//a
    print(c*d,"is the next term")
    dr4=c*d
else:
    print("special series")
    l=int(input("Enter another number"))
    found=False
    while(found==False):
        d1=b-a
        d2=c-b
        d3=l-c
        dr=d2-d1
        dr2=d3-d2
        if dr==dr2:
            print("lw")
            dr4=l+(d3+dr2)
            print(dr4)
            break
        else:
            r1=b//a
            r2=c//b
            r3=l//c
            rr=r2//r1
            rr2=r3//r2
            if rr==rr2:
                print("Nw")
                rr4=l*(r3*rr2)
                print(rr4)
                break
            else:
                print("Invalid Sequence")
reschk=int(input("Let's Check, enter orignal final value"))
if dr4==0:
    dr4=rr4
print("Predicted Value",dr4)
d=abs(dr4-reschk)
percentage=(100-d)//100 *100
print("Accuracy",percentage,"%")
    