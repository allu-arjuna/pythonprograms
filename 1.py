name=input("Enter student name: ")
usn=input("Enter Student USN: ")
m1=float(input("Enter the marks secured in Subject 1: "))
m2=float(input("Enter the marks secured in Subject 2: "))
m3=float(input("Enter the marks secured in Subject 3: "))
tm=m1+m2+m3
p=tm/3
print("Student Details:")
print("Name: ", name)
print("USN: ", usn)
print("Subject 1 Marks: ", m1)
print("Subject 2 Marks: ", m2)
print("Subject 3 Marks: ", m3)
print("Total Marks: ", tm)
print("Percentage: ", p)
if p>=35:
  print("You havee passed")
else:
  print("You have failed")
