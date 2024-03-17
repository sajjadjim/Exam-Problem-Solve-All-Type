
def calculate_waiver(semester_fee , cgpa):
    if cgpa >= 3.50 :
        waiver = 20
    elif 3.50 > cgpa >=3.00 :
        waiver = 10
    else:
        waiver = 5

    totall_waiver = (semester_fee * waiver) / 100
    return  totall_waiver


semester_fee = float(input("Enter your semester fee :"))
cgpa =float(input("Enter your CGPA :"))
total_waiver=calculate_waiver(semester_fee,cgpa)
print(f"Totall waiver -> {total_waiver} taka")
