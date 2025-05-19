a = float(input("Enter the coefficient of x²:- "))
b = float(input("Enter the coefficient of x:- "))
c = float(input("Enter the coefficient of 1:- "))
print ("Your quadratic equation is:")
print (str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0")

dis = b*b - 4*a*c
print ("")
if dis > 0:
    print ("The roots are two distinct real numbers.")
elif dis == 0:
    print ("This equation has only one root.")
else:
    print ("The roots of this equation are non-real complex numbers.")

if dis >= 0:
    alpha = str((-1*b + dis**0.5) / (2*a))
    beta = str((-1*b - dis**0.5) / (2*a))
    print ("")
    print ("The roots of the equation are " + alpha + " & " + beta)