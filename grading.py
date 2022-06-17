#(A:70-100),B:(60-69),C(50-59),D(40-49),E(0-39)
# program to computing and display grading of students 50
marks = float(input("Enter the marks"))
if marks<=39:
    print("Score: ",marks," ""Grade: E")
elif marks <=49:
    print("Score: ",marks," ""Grade: D")

elif marks <=59:
    print("Score: ",marks," ""Grade: C")
elif marks <=69:
    print("Score: ",marks," ""Grade:B")
else:
    print("Score: ",marks," ""Grade:A")
