#Some manipulation using dates and times using the datetime class
import datetime

currentDate = datetime.date.today()

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
print(currentDate.ctime())

#strftime.org to get all of the operators
print(currentDate.strftime('%d %b, %Y'))

#a quick example of using it
print(currentDate.strftime('Please attend the special event on %b %d in the year %Y'))

# birthday = input("What is your birthday? (mm/dd/yyyy) ")
# birthDate = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
# print(birthDate)

# difference = currentDate - birthDate
# print(difference.days)


currentTime = datetime.datetime.now()
print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

print (datetime.datetime.strftime(currentTime, '%H:%M %p'))