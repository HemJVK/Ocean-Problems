def grading_system(marks: [int],no_of_subjects: int) -> str:
    summation: int = 0
    for i in range(no_of_subjects):
        summation += marks[i]
    avg: float = summation/no_of_subjects
    if avg >= 90:
        return 'A'
    elif avg < 90 and avg >= 80:
        return 'B'
    elif avg < 80 and avg >= 70:
        return 'C'
    elif avg < 70 and avg >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    no_of_subjects: int = int(input("enter no of subjects: "))
    marks: int = []
    print("enter marks:",end=' ')
    for i in range(0,no_of_subjects):
        subject = int(input())
        marks.append(subject)
    
    print(f"Grade: {grading_system(marks,no_of_subjects)}")