def studentdetails(homework, assessment, exam):
    total = homework + assessment + exam
    percentage = (total/175) * 100
    return percentage

name = input("Enter student name: ")

homework = int(input("Enter homework score:"))
if homework > 25:
    print("Invalid input")
    exit()
assessment = int(input("Enter assessment score: "))
if assessment > 50:
    print("Invalid input")
    exit()
exam = int(input("Enter Exam result: "))
if exam > 100:
    print("Invalid input")
    exit()

percentresult = studentdetails(homework, assessment, exam)

print(name + " achieved a total percentage of: " + str(percentresult) + "%")