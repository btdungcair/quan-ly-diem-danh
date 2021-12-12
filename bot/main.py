from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

class ggmeet_bot:
    def __init__(self):
        self.bot = webdriver.Edge("D:/Datas/khac/quan/installer/edgedriver_win64/msedgedriver.exe")
    
    def login(self, email, password):
        url = "https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.113699780.238276641.1639299068-1599842929.1639299068&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        bot = self.bot
        bot.get(url)
        time.sleep(2)

        email_field = bot.find_element_by_id("identifierId")
        email_field.send_keys(email)

        next_button = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        next_button.click()
        time.sleep(2)

        password_field = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password_field.send_keys(password)

        next_button = bot.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        next_button.click()
        time.sleep(2)

    def join(self, meeting_url):
        bot = self.bot
        bot.get(meeting_url)
        time.sleep(2)
        dismiss_button = bot.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
        dismiss_button.click()

        keyboard.send('enter', do_press=True, do_release=True)

        turn_off_camera = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
        turn_off_camera.click()

        join_button = bot.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span")
        join_button.click()

if __name__ == "__main__":
    # email = input('Enter your email: ')
    # password = input('Enter your password: ')
    # meeting_url = input('Enter meeting url: ')
    obj = ggmeet_bot()
    # obj.login(email, password)
    # obj.join(meeting_url)
    obj.login("botpydiemdanh@gmail.com", "helloworld33")
    obj.join("https://meet.google.com/xhy-chek-myu")