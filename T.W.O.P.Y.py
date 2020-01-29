import pyttsx3 
import speech_recognition   
import datetime
import wikipedia 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)   


def Goverbal(audio): 
    engine.say(audio)
    engine.runAndWait()
    

def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Goverbal("Good Morning!")

    elif hour>=12 and hour<18:
        Goverbal("Good Afternoon!")   

    else:
        Goverbal("Good Evening!")  

    Goverbal("I am TWO PY .")       

def Input():


    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        Goverbal("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        Goverbal("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        Goverbal("Sorry i didn't quite catch that")  
        return "None"
    return query


if __name__ == "__main__":
    Greet()
    while True:
    # if 1:
        query = Input().lower()

        
        if 'wikipedia' in query:
            if query == 'wikipedia':
                Goverbal('Please ask your question ....')
                Input()
                continue
            else:
                Goverbal('traversing through the wide collections of wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                Goverbal("According to Wiki")
                print(results)
                Goverbal(results)
        elif 'whatsapp' in query:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://web.whatsapp.com/')
            Goverbal('Enter the name of user or group : ')
            name = Input()
            Goverbal('Enter your message : ')
            msg = Input() 
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()

            msg_box = driver.find_element_by_class_name('_3u328')

            for i in range(0):
               msg_box.send_keys(msg)
               button = driver.find_element_by_class_name('hnQHL')
               button.click()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Goverbal(f" the time is {strTime}")

        elif 'shutdown' in query:
            import os 
            Goverbal("Do you wish to shutdown your computer ? ")
            shutdown = Input() 
  
            if shutdown == 'no': 
                exit() 
            else: 
                Goverbal('ok bye')
                os.system("shutdown /s /t 1")

       
        elif 'open youtube' in query:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://www.youtube.com/')
            break
        elif 'open google' in query:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://www.google.com/')
            break

        elif 'alarm' in query:
            from pygame import mixer
            import time

            def sound():
                mixer.init()
                mixer.music.load("D:\Downloads\Wecker-sound.mp3")
    
            def alarm():
                
                Goverbal("Enter the hour")
                hr=int(Input())
                Goverbal("Enter the minute")
                mn=int(Input())
                

                n=5  

                print("Alarm set for",str(hr),":",str(mn))
                while True:
                    if time.localtime().tm_hour==hr and time.localtime().tm_min==mn :
                        print("Wake up") 
                        break
    
        
                while n>0:
                    mixer.music.play()
                    time.sleep(2)

                snz=Input()
                if snz=='Stop':
                    n=3
                    time.sleep(100)
                    while n>0:
                        mixer.music.play()
                        time.sleep(2)
                else:
                    exit()
            sound()
            alarm()
           
            


if 'bye' or 'goodbye' or 'quit' or 'exit' in query:
    Goverbal('See You Later!')
    

   


