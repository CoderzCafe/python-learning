import datetime

print("Now: " +str(datetime.datetime.now()))

x = datetime.datetime.now()

print("Year: " +str(x.year))

print(x.strftime("%A / %B / %C"))
print("\nDay: " +str(x.strftime("%A")))
print("Month: " +str(x.strftime("%B")))
print("Year: " +str(x.strftime("%C"))+"\n")

print(x.strftime("%c"))
print("Date: ", x.strftime("%d"))
print("Month: ", x.strftime("%m"))
print("Year: ", x.strftime("%y"))
print()