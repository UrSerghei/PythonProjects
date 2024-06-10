import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL_GMAIL = "test.python@gmail.com"
PASSWORD_MY_EMAIL_GMAIL = "pubmhokg"
MY_EMAIL_YAHOO = "test.python@yahoo.com"

PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
month_1 = now.month
day_1 = now.day

# check date from csv

df = pandas.read_csv("birthdays.csv")
df_dict = df.to_dict('records')
for value in df_dict:
    month_2 = value["month"]
    day_2 = value["day"]
    # if today is your birthday
    letters = []
    if month_1 == month_2 and day_1 == day_2:
        with open("letter_templates/letter_1.txt") as letter1:
            letter1_read = letter1.read()
            letters.append(letter1_read)
        with open("letter_templates/letter_2.txt") as letter2:
            letter2_read = letter2.read()
            letters.append(letter2_read)
        with open("letter_templates/letter_3.txt") as letter3:
            letter3_read = letter3.read()
            letters.append(letter3_read)
        letter_contents = random.choice(letters)
        strip_name = value["name"]
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"{strip_name}.birthday.txt", "r") as completed_letter:
            final_txt = completed_letter.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL_GMAIL, password=PASSWORD_MY_EMAIL_GMAIL)
            connection.sendmail(from_addr=MY_EMAIL_GMAIL,
                                to_addrs=value["email"],
                                msg=f"Subject:Birthday Card\n\n{final_txt}")
