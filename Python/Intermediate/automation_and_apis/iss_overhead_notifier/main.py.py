import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 40.7648
MY_LONG = -73.9808

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() 
    data = response.json()

    ISS_latitude = float(data["iss_position"]["latitude"])
    ISS_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT-5 <= ISS_latitude <= MY_LAT+5 and MY_LONG-5 <= ISS_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT, 
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Indian/Mauritius",
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset= int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:    
        MY_EMAIL = "aaron@gmail.com"
        MY_PASS = "vnoewirwiroiwer"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=MY_PASS)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS Near You\n\nLook UP"
            )