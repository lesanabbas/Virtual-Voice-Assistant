import sys
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import time
import wikipedia  # pip install wikipedia
import webbrowser
import random
import os
import smtplib
import pyautogui as pg
import pywhatkit
import requests
import platform
from gnewsclient import gnewsclient
import clipboard
import psutil
import time as tt
import cv2
# from nltk.tokenize import word_tokenize
from keyboard import press
from keyboard import write
from keyboard import press_and_release
import sys
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from FridayGUI import Ui_Gui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 190)
engine.setProperty('volume', 1.0)
engine.setProperty("languages", 'en')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    elif hour >= 17 and hour < 22:
        speak("Good Evening")

    else:
        speak("Good Night!")

    speak("I am Friday Sir. I am ready to take command")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskException()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            r.energy_threshold = 9000
            r.dynamic_energy_threshold = True
            audio = r.listen(source)

        try:
            print("Recognizing...")
            q = r.recognize_google(audio, language='en-IN')
            print(f"User said: {q}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return q

    def account_info(self):
        with open('account_info.txt', 'r') as f:
            info = f.read().split()
            email = info[0]
            password = info[1]
        return email, password

    def sendWhatsappMessage(self, phone_no, msg):
        Message = msg
        webbrowser.open('https://web.whatsapp.com/send?phone=' +
                        phone_no+'&text='+Message)
        time.sleep(15)
        pg.pg.click(x=1780, y=981)

    def date(self):
        m = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak(date)
        speak(f" of  {m[month-1]}")
        speak(year)

    def news(self):
        speak("what topic you need the news about")
        Topic = self.takeCommand()

        client = gnewsclient.NewsClient(
            language='english', location='india', topic=Topic, max_results=3)
        news_list = client.get_news()

        for news in news_list:
            print("Title : ", news['title'])
            speak(news['title'])
            print("Link : ", news['link'])
            print("")

        speak("that's it for now I'will update you in some time")

    def selectedText2Speech(self):
        pg.press('Ctrl+c')
        text = clipboard.paste()
        print(text)
        speak(text)

    def closeTask(self):
        try:
            os.system('TASKKILL /F /IM chrome.exe')

        except Exception as e:
            print(e)

    def closecode(self):
        try:
            os.system('TASKKILL /F /IM code.exe')

        except Exception as e:
            print(e)

    def closecode(self):
        try:
            os.system('TASKKILL /F /IM code.exe')

        except Exception as e:
            print(e)
            
    def close_yourself(self):
        exit()

    def close_music(self):
        try:
            os.sytem('TASKKILL /F /M groove Music.exe')
        except Exception as e:
            print(e)

    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('raik12456@gmail.com', 'qwertyuiopcar')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()

    def screenshot(self):
        name_img = tt.time()
        name_img = 'C:\\Users\\Abbas\\OneDrive\\Pictures\\Screenshots\\Screenshots{}.png'.format(
            name_img)
        img = pg.screenshot(name_img)
        speak("done sir!")
        img.show()

    def info(self):
        my_system = platform.uname()

        print(f"System: {my_system.system}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")

        speak(f"System: {my_system.system}")
        speak(f"Machine: {my_system.machine}")
        speak(f"Processor: {my_system.processor}")

    def shutdown(self):
        speak("I'm going to shutdown system")
        os.system('shutdown /s /t 10')

    def restart(self):
        speak("I'm going to restart system")
        os.system("shutdown /r /t 1")

    def batteryinfo(self, seconds):
        minutes, secconds = divmod(seconds, 60)
        hour, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hour, minutes, secconds)
    
    def checkInternetConnection(self):
        url = 'https://www.google.co.in'
        try:
            request = requests.get(url, timeout=3)
            return True
        except (requests.ConnectionError, requests.Timeout) as e:
            return False
        

    def TaskException(self):

        wishMe()
        while True:
            self.q = self.takeCommand().lower()
            print(self.q)
           
            if 'wikipedia' in self.q:
                try:
                    speak('Searching Wikipedia...')
                    self.q = self.q.replace("wikipedia", "")
                    results = wikipedia.summary(self.q, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak(f'Sorry sir I am not able to find {self.q}')

            elif 'youtube' in self.q:
                speak('why not sir')
                speak("What should I search for on youtube")
                topic = self.takeCommand()
                pywhatkit.playonyt(topic)
                
            elif 'open camera' in self.q:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'instagram' in self.q or 'insta' in self.q:
                speak("Wait Sir, let me check")
                email, password = self.account_info()
                options = Options()
                # options.add_argument("start-maximized")
                driver = webdriver.Chrome(options=options)

                driver.get("https://www.instagram.com/accounts/login/")

                email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'


                password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
                login_xpath = '//*[@id="loginForm"]/div/div[3]'

                not_now_xpath = '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button'
                not_now_notfication = '/html/body/div[5]/div/div/div/div[3]/button[2]'
                message_count_xpath = '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div'

                time.sleep(3)

                driver.find_element_by_xpath(email_xpath).send_keys(email)
                driver.find_element_by_xpath(password_xpath).send_keys(password)
                driver.find_element_by_xpath(login_xpath).click()
                time.sleep(3)
                driver.find_element_by_xpath(not_now_xpath).click()
                time.sleep(3)
                driver.find_element_by_xpath(not_now_notfication).click()
                time.sleep(2)
                count = driver.find_element_by_xpath(message_count_xpath).text
                speak(f"Sir you have {count} messages on instagram")

            elif 'google' in self.q:
                speak('What you want to search sir')
                search = self.takeCommand()
                if(search == 'leave it'):
                    speak('no problem sir')
                else:
                    webbrowser.open(f"https://www.google.com/search?q={search}")
                    speak(f'sure sir here is a {search}')
                    
            elif 'where i am' in self.q or 'where we are' in self.q:
                speak("wait sir, let me check")
                try:
                    ip_add = requests.get('https://api.ipify.org/')
                    geo_requests = requests.get('https://get.geojs.io/v1/ip/geo/'+ip_add.text+'.json')
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f'sir I not sure but, I think we are in {city} city of {country} country')
                except Exception as e:
                    print(e)
                    speak('Sorry sir, Due to network issue I am not able to find where we are.')
                    
            elif 'thanks' in self.q or 'thank you' in self.q:
                speak('thanks sir, hava a good day.')
                
            elif 'hello' in self.q or 'wake up' in self.q:
                speak('Hello sir, what can I help you')
                
            elif 'who are you' in self.q or 'about you' in self.q or 'introduce' in self.q:
                speak("Wait Sir")
                speak("let me introduce myself")
                speak("I am Brian the virtual voice assistant")
                speak("I am here to assist you with a variety of task as best I can")
                
            elif 'internet speed' in self.q:
                import speedtest
                speak("wait sir let me check")
                speed = speedtest.Speedtest()
                downloadSpeed = speed.download() / 1048576
                uploadSpeed = speed.upload() / 1048576
                Ping = round(speed.results.ping)
                speak(f"Sir we have {round(downloadSpeed)} Mb per second downloading speed and {round(uploadSpeed)} Mb per second uploading speed")
                speak(f"and {Ping} ping")

            elif 'battery' in self.q:
                battery = psutil.sensors_battery()
                speak(f"Battery percentage is {battery.percent}")
                battery_left = self.batteryinfo(battery.secsleft)
                speak(f"Sir, the remaining time is {battery_left[0:1]} hour {battery_left[2:4]} minutes{battery_left[5:6]} seconds")
                if battery.power_plugged == False:
                    if battery.percent < 30:
                        speak("Battery power is low may I suggest you charge it soon sir")
                    elif battery.percent < 20:
                        speak("Battery power is too low I highly recommend you plugged in.")
                    
                print("Battery left : ", self.batteryinfo(battery.secsleft))


            elif 'new tab' in self.q:
                speak('sure sir')
                press_and_release('Ctrl + t')

            elif 'close tab' in self.q:
                speak('sure sir')
                press_and_release('Ctrl + w')
                
            elif 'close window' in self.q:
                speak('sure sir')
                press_and_release('Alt + F4')
                
            elif 'close yourself' in self.q:
                speak('sure sir')
                self.close_yourself()
                sys.exit(app.exec_())
                
            elif 'open cmd' in self.q:
                subprocess.Popen("cmd.exe")
                
            elif 'open download' in self.q:
                subprocess.Popen(r'explorer /select,"C:\Users\Abbas\Downloads\"')
                
            elif 'open documents' in self.q:
                subprocess.Popen(r'explorer /select,"C:\Users\Abbas\OneDrive\Documents\XuanZhi"')
                
            elif 'open notepad' in self.q:
                subprocess.Popen("C:\\Windows\\notepad.exe")
                
                
            elif 'bluetooth' in self.q:
                speak('sure sir')
                pg.click(x=1875, y=1066)
                time.sleep(1)
                pg.click(x=1712, y=666)
                time.sleep(0.5)
                pg.click(x=1883, y=1056)

            elif 'wi-fi' in self.q:
                speak('sure sir')
                pg.click(x=1689, y=1059)
                time.sleep(1)
                pg.click(x=1518, y=980)

            elif 'system information' in self.q or 'system info' in self.q:
                self.info()

            elif 'shutdown' in self.q:
                self.shutdown()  

            elif 'restart' in self.q:
                self.restart()   


            elif 'play music' in self.q:
                music_dir = 'E:\\Music'
                speak('sure sir')
                try:
                    songs = os.listdir(music_dir)
                    for i in range(len(songs)):
                        print(i ,songs[i])
                    
                    n = random.randint(0, len(songs))   
                    print(n)
                    print(songs[n])
                    os.startfile(os.path.join(music_dir,songs[n]))
                    
                except:
                    speak("I can't find any song")
                

            elif "time" in self.q:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                strTime = strTime.split(":")
                if(int(strTime[0]) > 12):
                    strTime[0] = int(strTime[0])-12 
                speak(f"Sir, the time is {strTime[0]} hour {strTime[1]} minutes{strTime[2]} seconds")

            elif "date" in self.q:
                self.date()

            elif "weather" in self.q:
                apiKey = '358477c69ebfdce75bb1773bdc77e6fc'
                url = f'https://api.openweathermap.org/data/2.5/weather?q=Lucknow&appid={apiKey}'
                res = requests.get(url)
                data = res.json()
                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                city = data['name']
                desc = data['weather'][0]['description']
                temp = round(temp - 273.15)
                print(weather)
                print(temp)
                print(desc)
                print(city)
                speak(f'Temperature : {temp} degree celcius')
                speak(f'And todays weather in {city} is {weather}')

            elif "read" in self.q:
                self.selectedText2Speech()

            elif "screenshot" in self.q:
                self.screenshot()

            elif 'open code' in self.q:
                codePath = "D:\\Program Files (x86)\\Microsoft VS Code\\bin\\code.cmd"
                os.startfile(codePath)

            elif 'close code' in self.q:
                speak('sure sir')
                self.closecode()

            elif 'news' in self.q:
                self.news()

            elif 'whatsapp' in self.q:
                user_name = {
                    'clipboard' : '+91 9451184960',
                    'Mirza' : '+91 89579 24952',
                    'Naveed Khan' : '+91 91150 40459',
                }
                try:
                    speak("To whom you want to send the whatsapp message ?")
                    name = self.takeCommand()
                    phone_no = user_name[name]
                    speak("what you want to say ?")
                    mess = self.takeCommand()
                    self.sendWhatsappMessage(phone_no, mess)
                    speak("message has been send sir.")
                except Exception as e:
                    print(e)
                    speak("I'm unable to send message")

            elif "remember" and "that" in self.q:
                speak("what should I remember ?")
                data = self.takeCommand()
                speak(f"you said me to remember that {data}")
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif "do you know anything" in self.q:
                remember = open('data.txt', 'r')
                speak(f'you told me to remember that '+remember.read())
                

            elif 'email' in self.q:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "dewowo3805@fxseller.com"    
                    self.sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")
   

startExecution = MainThread()
         

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Gui()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\Abbas\\OneDrive\\Desktop\\Brian Voice Assistant\\assets\\favicon.ico"))
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.label.setPixmap(QtGui.QPixmap("C:\\Users\\Abbas\\OneDrive\\Desktop\\Brian Voice Assistant\\assets\\bg-img.jpg"))
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\Abbas\\OneDrive\\Desktop\\Brian Voice Assistant\\assets\\center.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        curr_time = QTime.currentTime()
        curr_date = QDate.currentDate()
        label_time = curr_time.toString('hh:mm:ss')
        label_date = curr_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

        
app = QApplication(sys.argv)
Gui = Main()
Gui.show()
sys.exit(app.exec_())