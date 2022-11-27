import datetime
import time
import http.client
from datetime import datetime
from datetime import date
from datetime import timedelta


bdays = { 
            "Alice" :"11-29",
            "Bob"   :"06-12"
        }

anniversaries = { 
                    "Alice & Bob" :"06-12"
                }

def getEvents(events):
    today = str(date.today())
    in_two_days = str(date.today() + timedelta(days=2))
    year_today = today[0:5] # "XXXX-"
    year_in_two_days = in_two_days[0:5] # Needed in the case where the year changes 2 days from now
    events_today = []
    events_in_two_days = []
    for key in events:
        event_today = str(year_today + events[key])
        event_in_two_days = str(year_in_two_days + events[key]) 
        if (event_today == today):
            events_today.append(key)
        elif (event_in_two_days == in_two_days):
            events_in_two_days.append(key)
    events = [events_today, events_in_two_days]
    return events

def create_msg_today(event_arr, event_type, message):
    if (len(event_arr) > 0):
        message = message + "Today's " + event_type + ": "
        for i in range(0,len(event_arr)):
            message = message + "\n" + event_arr[i]
        message = message + "\n\n"
    return message

def create_msg_in_two_days(event_arr, event_type, message):
    if (len(event_arr) > 0):
        in_two_days = str(date.today() + timedelta(days=2))
        message = message + "Upcoming " + event_type
        message = message + " (" + in_two_days + "): "
        for i in range(0,len(event_arr)):
            message = message + "\n" + event_arr[i]
        message = message + "\n\n"
    return message

def create_msg():
    # Birthdays
    bday_kids = getEvents(bdays)
    bday_kids_today = bday_kids[0]
    bday_kids_in_two_days = bday_kids[1]
    # Anniversaries
    anniv_couples = getEvents(anniversaries)
    anniv_couples_today = anniv_couples[0]
    anniv_couples_in_two_days = anniv_couples[1]

    message = ""
    message = create_msg_today(bday_kids_today, "Birthdays", message)
    message = create_msg_today(anniv_couples_today, "Anniversaries", message)
    message = create_msg_in_two_days(bday_kids_in_two_days, "Birthdays", message)
    message = create_msg_in_two_days(anniv_couples_in_two_days, "Anniversaries", message)
    return message

def send(message):
    # your webhook URL
    webhookurl = "" # Put your discord channel webhook URL here

    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
  
    # get the connection and make the request
    connection = http.client.HTTPSConnection("discord.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })
  
    # get the response
    response = connection.getresponse()
    result = response.read()
  
    # return back to the calling function with the result
    return result.decode("utf-8")

def main():
    message = create_msg()
    if (message != ""):
        send(message)

def lambda_handler(event, context):
   main()

if __name__ == '__main__':
    main()