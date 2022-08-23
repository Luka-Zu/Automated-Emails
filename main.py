import smtplib
import time
import pandas
from news import NewsFeed
import datetime


while True:
    if datetime.datetime.now().hour == 23 and datetime.datetime.now().minute == 59:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():

            date_string = datetime.datetime.now().strftime('%y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=date_string,
                                 to_date=date_string)

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(user="zukhbaialuka0@gmail.com", password="incorrect_password")

            message = f"Hi {row['name']}\n" \
                      f"See today's news about {row['interest']}" \
                      f"{news_feed.get()}"
                # .replace(u"\u2018", "'").replace(u"\u2013", "'").replace(u"\u2019", "'").replace(
                # u"\u2014", "'").replace(u"\u2015", "'").replace(u"\u2020", "'").replace(u"\u201c", "'").replace(u"\u201d", "'")

            server.sendmail(from_addr="zukhbaialuka0@gmail.com",
                            to_addrs=row['email'],
                            msg=message)
            server.quit()
        time.sleep(60)

# FUCK yagmail library !
