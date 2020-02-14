todays_years =input("1. What year is it?: " )
todays_month =input("2. What month is it? Write full month, first letter capitalized. ")
todays_day = input("3. What day of the month is this month? Just type the number. ")

print("Today is " + todays_month + " " + todays_day + "," + " " + todays_years + ".")
year = input("4. What year were you born?: ")
month = input("5. What month were you born?: ")
day= input("6. What day of the month were you born: ")
print("You were born " + month + " " + day + "," + " " + year + ".")


month_dictionary = {'January': 1, 'February': '2', 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
#age = 2019- int(year)
#print("You are " + str(age) + " " + "years old, as of Dec 2019. ")
birth_month = month_dictionary[month]
birth_month = int(birth_month)
todays_month = month_dictionary[todays_month]
todays_month = int(todays_month)
new_month_age = 12 -int(birth_month) + int(todays_month)
new_year_age_notyet = int(todays_years) -1 -int(year)
new_year_age = int(todays_years) -int(year)
if birth_month > todays_month:
    print("You haven't had a birthday yet this year :(")
    print("You are " + str(new_year_age_notyet) + " "+ "years old and" + " " + str(new_month_age) + " " + "months.")
elif birth_month == todays_month and todays_day == day:
    print("Happy Birthday! You are " + str(new_year_age) + " " + "years old today!")
elif birth_month == todays_month and todays_day > day:
    print("You are " + str(new_year_age) + " " + "years old. Happy Belated Birthday!")
elif birth_month == todays_month and todays_day < day:
    print("You are " + str(new_year_age_notyet) + " " + "years old. Your birthday is coming up soon!")
elif birth_month < todays_month:
    print ("It seems that your birthday has already passed, Happy Belated. You are " + " " + str(new_year_age) + " " + " years old and"
           + str(new_month_age) + " " +  "months.")

#print(birth_month)
#print(todays_month)
#print(str(new_month_age))
#print(new_year_age)