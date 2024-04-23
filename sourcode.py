import requests
import time
import pycountry

ap = input("Enter API Key: ")

def guess():
    a = requests.get('https://ipinfo.io/json?token='+ ap)
    a = a.json()
    cit = a['city']
    cou_code = a['country']
    cou = pycountry.countries.get(alpha_2=cou_code).name
    inp = input("What is your favourite colour?: ")
    x = input("Which is better dog or cat?: ")
    y = input("Which is better in the wild, a lion or a tiger?: ")
    print("Thinking hard")
    print("Searching the air for your location...")
    time.sleep(3)
    print("Successful")
    while True:
        print("Your country is", cou, "and your city is", cit)
        cv = input("Press e to exit: ")
        if cv.lower() == 'e':
            break


guess()
