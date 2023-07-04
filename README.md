# DailyWeatherSMS
Program that sends daily SMS message listing the weather conditions expected within next three hours. Utilizes Twilio, OpenWeatherMap API, and pythonanywhere.com for automation of script.
I use this program (along with environmental variables not listed in the mainweather.py file for private information) to automatically send my personal phone number an SMS message every day telling me the weather conditions I can expect where my college is located, Hoboken, NJ.
This program utilizes weather data from OpenWeatherMap's 5 day/3 hour API and translates that data into a message sent from a Twilio Client session using my Twilio account phone number. 
This program has been uploaded and configured using pythonanywhere.com to automate the sending of the message once a day without me having to run the program personally.
