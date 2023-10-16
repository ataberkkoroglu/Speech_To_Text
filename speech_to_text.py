import os

import speech_recognition as sr
os.chdir("C://Users/Asus/Desktop")
x=sr.Recognizer()

y=0
while 1:
    try:
        with sr.Microphone() as source:
            audio=x.listen(source)
            voice=x.recognize_google(audio,language="tr-TR")
            while 1:
               if y==0:
                exist = os.access("speech.txt", os.F_OK)
                if (exist!=1):
                    break
               else:
                   exist = os.access(f"speech{y}.txt", os.F_OK)
                   if (exist != 1):
                       break
               y+=1
            if (y!=0):
             with open(f"speech{y}.txt", "a") as file:
                    file.write(voice)
            else:
                with open(f"speech.txt", "a") as file:
                    file.write(voice)


            print(audio)

    except:
        raise ValueError("Timeout")