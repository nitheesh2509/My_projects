from bill_details import Bill, Roommate
from reports import PdfReport, FileShare

amount = float(input("Please enter the bill amount: "))
period = input("What is the bill period? 'Eg. Sept 2002': ")
the_bill = Bill(amount, period)
name_1 = input("What is your name?: ")
days_in_room_1 = int(input(f"How many days did {name_1} stay during the bill period: "))
name_2 = input("What is the other roommate's name?: ")
days_in_room_2 = int(input(f"How many days did {name_2} stay during the bill period: "))
roommate_1 = Roommate(name_1, days_in_room_1)
roommate_2 = Roommate(name_2, days_in_room_2)

print(f"{roommate_1.name} should pay for the room:", roommate_1.pays(the_bill, roommate2=roommate_2))
print(f"{roommate_2.name} should pay for the room:", roommate_2.pays(the_bill, roommate2=roommate_1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_path = pdf_report.generate(roommate1=roommate_1, roommate2=roommate_2, bill=the_bill)

file_sharer = FileShare(filepath=pdf_path)
file_sharer.share()