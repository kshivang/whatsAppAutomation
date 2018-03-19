import pandas as pd
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Press enter after scanning the QR code')

message = "%E2%9C%A8%E2%9D%A4+Osho+Naman+%E2%9D%A4%E2%9C%A8%0D%0ALet%27s+listen+to+Osho%27s+timeless+wisdom%" \
          "21%0D%0AGet+the+FREE+Osho+Meditation+app%3A+Bliss+and+also+forward+and+Share+the+blessing+of+Osho+" \
          "with+all%21%F0%9F%99%8F%0D%0A%0D%0AEnjoy+lots+of+meditation+tracks+and+Osho%27s+talk+in+this+beautiful+" \
          "app.+%0D%0A%0D%0A%E0%A4%B8%E0%A5%81%E0%A4%A8%E0%A5%87+%E0%A4%93%E0%A4%B6%E0%A5%8B+%E0%A4%95%E0%A4%BE+" \
          "%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AD%E0%A5%81%E0%A4%A4+%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8+" \
          "%E0%A4%B8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%AB+Bliss+App+%E0%A4%AA%E0%A4%B0%E0%A5%A4%0D%0A%E0%A4%85%E0%A" \
          "4%AD%E0%A5%80+%E0%A4%AA%E0%A4%BE%E0%A4%8F%E0%A4%82+Bliss+App+%E0%A4%94%E0%A4%B0+%E0%A4%86%E0%A4%A8%E0%A4" \
          "%82%E0%A4%A6+%E0%A4%B2%E0%A5%87%E0%A4%82+%E0%A4%93%E0%A4%B6%E0%A5%8B+%E0%A4%95%E0%A5%87+%E0%A4%AA%E0%A4" \
          "%B0%E0%A4%AE+%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8+%E0%A4%95%E0%A4%BE%E0%A5%A4%0D%0A%0D%0A%F0%" \
          "9F%91%89+Link+%3A++bit.ly%2FOshoBliss++%F0%9F%91%88".replace("+", "%20")


def send_message_to_number(mobile_no):
    phone_no = "".join(mobile_no).replace("+", "").replace(" ", "") + '&text=' + message
    driver.get('https://api.whatsapp.com/send?phone=' + phone_no)
    time.sleep(1)
    while True:
        try:
            driver.find_element_by_id("action-button").click()
            break
        except Exception:
            try:
                driver.switch_to.alert.accept()
            except Exception:
                print("No alert found\n")
            print('No send button found\n')
            time.sleep(0.5)

    while True:
        try:
            driver.find_element_by_class_name('_2lkdt').click()
            break
        except Exception:
            print('No send button found\n')
            time.sleep(0.5)


def read_csv(csv_to_open):
    numbers = pd.read_csv(csv_to_open).values
    count = 1
    for number in numbers:
        print(count, " out of ", len(numbers), "\n")
        send_message_to_number(number)


def read_members_from_group():
    input("Press Enter after selecting a group: ")
    while True:
        try:
            text = driver.find_element_by_class_name("O90ur").text
            print("Found group bar")
            print(text)
            return text
        except Exception:
            print("No group bar found")
            time.sleep(0.5)


while True:
    whatToDo = input("CSV fileor q to quite or blank to send to Bliss_Team.csv: ")
    csvToOpen = 'Bliss_Team.csv'
    if whatToDo == "q":
        break
    # elif whatToDo == "a":
    #     read_members_from_group()
    elif whatToDo != "":
        csvToOpen = whatToDo
        read_csv(csvToOpen)
    else:
        read_csv(csvToOpen)
