from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

input('Press enter after scanning the QR code')


def send_message(message):
    if message == "":
        # driver.find_element_by_class_name('_2bXVy').click()
        driver.find_element_by_class_name('_2bXVy').send_keys(Keys.COMMAND, 'v')          # Paste from clipboard
        # driver.find_element_by_class_name('_2lkdt').click()                               # Click on send button
    else:
        driver.find_element_by_class_name('_2bXVy').send_keys(message)                    # Type message
        driver.find_element_by_class_name('_2lkdt').click()                               # Click on send button



def send_message_to_user(user_name, message):
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name)).click()   # Open $user_name message thread
    send_message(message)


def group_info_click(group_name):
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(group_name)).click()  # Open $group_name message thread
    driver.find_element_by_class_name("_3AwwN").click()                               # Open group info
    time.sleep(2)


def group_members(group_name):
    group_info_click(group_name)
    members = driver.find_element_by_class_name("_2sNbV").find_elements_by_xpath('//div[@class="_2EXPL _3xj48"]')
    return members


def pm_group_message(group_name, message):
    members = group_members(group_name)
    members_count = len(members)
    # admin = members[members_count - 1]
    # try:
    #     if admin.find_element_by_class_name("_3Bxar") is not None:
    #         print("You are admin of this group\n")
    #         members_count = members_count - 2
    #         del(members[1])
    #         del(members[0])
    # except Exception:
    #     print("You are not admin of this group\n")

    print('Groups members count: ', len(members))
    print('Clicking Member ', 0)
    members[0].click()
    send_message(message)
    memberAt = 1
    # for memberAt in range(1, members_count - 1):
    while memberAt < members_count - 1:
        try:
            members = group_members(groupName)
            print('Clicking Member ', memberAt)
            members[memberAt].click()
            send_message(message)
            memberAt = memberAt + 1
        except Exception:
            print("Error occured")


def find_currently_selected_group_name():
    title = driver.find_element_by_class_name("_1GX8_").find_element_by_class_name("_1wjpf").get_attribute("title")
    try :
        print("Title is:",  title)
    except Exception:
        print("Title has non ascii characters")
    return title


newline = '                                                                         ' \
          '                                                                                '
blankline = '*'

while True:
    whatToDo = input('Choose 1 or 2 or 3 or q, then Enter\n'
                     '1) Send message to individual user or group\n'
                     '2) Send message to every member of group\n'
                     '3) Send message to every member of group with GUI input\n'
                     'q) Quite\n')
    if whatToDo == '1':
        name = input('Enter User or Group name: ')
        msg = input('Message: ')
        send_message_to_user(name, msg)
    elif whatToDo == '2':
        groupName = input('Enter Group name: ')
        msg = input('Message: ')
        pm_group_message(groupName, msg)
    elif whatToDo == '3':
        msg = ''
        # msg = "Osho Naman" + newline\
        #  + blankline + newline\
        #  + "Let's listen to Osho's timeless wisdom!" + newline\
        #  + "Get the FREE Osho Meditation app: Bliss and also forward and Share the blessing of Osho with all!" + newline\
        #  + blankline + newline\
        #  + "Enjoy lots of meditation tracks and Osho's talk in this beautiful app." + newline\
        #  + blankline + newline\
        #  + "सुने ओशो का अध्भुत ज्ञान सिर्फ Bliss App पर।" + newline\
        #  + "अभी पाएं Bliss App और आनंद लें ओशो के परम ज्ञान का।" + newline\
        #  + blankline + newline\
        #  + "=> Link :  bit.ly/OshoBliss <="
        # msg = input("Type message or leave blank to paste from clipboard: ")

        while True:
            nowWhat = input("Press Enter after selecting group to continue or q to quite:")
            if nowWhat == '':
                groupName = find_currently_selected_group_name()
                if groupName != "":
                    pm_group_message(groupName, msg)
                else:
                    print("Enter reading groupName")
            elif nowWhat == 'q':
                break
            else:
                print("Invalid Input\n")
    elif whatToDo == 'q':
        exit()
    else:
        print("Invalid Input\n")

