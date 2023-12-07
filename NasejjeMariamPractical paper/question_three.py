#(i)
Age = int(input("Enter your age: "))

if Age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")

#(ii)
def grade_students(avg):
  if(avg>=90):
    print("Grade: A")
  elif(avg>=80<90):
    print("Grade: B")
  elif(avg>=70<80):
    print("Grade: C")
  elif(avg>=60<70):
    print("Grade: D")
  else:
     print("F")

#(iii)

#(iv)
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80<90):
    print("Grade: B")
elif(avg>=70<80):
    print("Grade: C")
elif(avg>=60<70):
    print("Grade: D")
else:
    print("invalid Input!")

#(v)
if(avg>=90):
    print("A:Excellent")
elif(avg>=80<90):
    print("B:Excellent")
elif(avg>=70<80):
    print("C:good")
elif(avg>=60<70):
    print("D:satisfactory")
else:
    print("F:Nedds improvement")

#(vi)
