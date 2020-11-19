
import time
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
def main():

    name= input("Enter the name you person : ")

    msg= input("Enter your masssage here : ")

    msg1=input('Next mesg or Leave blank : ')

    count=int(input(('The no of repeated time you message;  ')))
    user= driver.find_element_by_xpath(('//span[@title="{}"]'.format(name)))
    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")


    # for msg

    def repeatition():

        for i in range(count):
            msg_box.send_keys(f"{i+1} . {msg}")
            button= driver.find_element_by_xpath('//button[@class ="_1U1xa"]')
            button.click()
            print(i,'no. of times message sended')
    if len(msg)>1:
        repeatition()
    else:
        exit()

        # for msg1 


    def repeatition1():



        for i in range(count):
            msg_box.send_keys(f"{i+1} . {msg1}")
            button= driver.find_element_by_xpath('//button[@class ="_1U1xa"]')
            button.click()
            print(i,'no. of times message sended')
    if len(msg1)>1:
        time.sleep(20)
        repeatition1()
    else:
        exit()


    user = input('Do you want to continue: yes or no  :  ')

    #for code repeatition
    if user == 'yes' or user =='Yes':
        main()

    else:
        exit()

main()




