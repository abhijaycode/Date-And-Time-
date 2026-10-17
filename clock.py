from datetime import datetime

now = datetime.now()

format1 = now.strftime("%Y-%m-%d %H:%M:%S IST %Y")
format2 = now.strftime("%Y/%m/%d %H:%M:%S")
format3 = now.strftime("%d-%m-%Y")
format4 = now.strftime("%H:%M:%S")


print("Current date and time in format 1:", format1)
print("Current date and time in (ISO format):", format2)
print("Current date in (date only):", format3)
print("Current time in (time only):", format4)
