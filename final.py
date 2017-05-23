from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser
import time
import pyautogui
import random
import thread
import sqlite3


def speak(audioString):	  #speak function to save user's audio
    print(audioString)
    tts = gTTS(text=audioString, lang="en")
    tts.save("audio.mp3")
    os.startfile("audio.mp3")

def speak_database(audioString):   #speak function to save user's audio
    print(audioString)
    tts = gTTS(text=audioString, lang="en")
    tts.save("audio_db.mp3")
    os.startfile("audio_db.mp3")	
	

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
	audio = r.listen(source)
 
    # Speech recognition performed
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
     
    return data

def myvoice(audio):
	if "play me a song" in audio or "play me the song" in audio:
		x=random.choice(os.listdir("C:/Users/CLi NinJa/Desktop/Python Project/fav/"))
		os.startfile("C:/Users/CLi NinJa/Desktop/Python Project/fav/" + x)
		
	if "how are you" in audio or "how r u" in audio:
		speak("The teachers taking this presentation are making me nervous")
		time.sleep(4)
		data=recordAudio()
		if "can i help" in data or "can a help" in data or "kan i help" in data or "kan i helped" in data:
			speak("just shut me down please")
		
	if "time" in audio or "time" in audio :
		speak(time.ctime())
		
	if "where is" in audio or "where in" in audio:
		data = audio.split(" ")
		x=[str(item) for item in data]	
		location = x[2:]
		loc= " ".join(location)
		speak("Let me check where " + loc +" is.")
		webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s").open("https://www.google.co.in/maps/place/"+loc)
	
	if "search" in audio:
		data = audio.split(" ")
		x=[str(item) for item in data]		
		google = x[1:]
		string= " ".join(google)
		print string
		webbrowser.get("C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s").open("www.google.co.uk/search?hl=en&q="+string)
		
	if "text" in audio or 'txt' in audio or "message" in audio:
		speak_database("Name the person")
		time.sleep(4)
		#data=recordAudio()
		data='teacher'
		print data
		speak_database("Searching for the person " + data)
		time.sleep(3)
		x=conn.execute("SELECT mobile FROM FRIENDS WHERE name=?",(data,))
		for i in x:
			mobile_no= i[0]
		x=str(mobile_no)
		speak_database("What's your text")
		time.sleep(4)
		#data=recordAudio()
		data='Presentation'
		speak_database("You said " + data + ". Are you sure you want to send this?")
		b=int(raw_input("press 1 for yes else any key to exit"))
		if(b==1):
			os.startfile("C:/Users/CLi NinJa/Desktop/Python Project/way2sms.pyc")
			time.sleep(2)
			pyautogui.typewrite(x)
			pyautogui.press('enter')
			pyautogui.typewrite(data)
			
	
			
	if "lets play" in audio:
		pyautogui.keyDown('fn')
		pyautogui.press('2')
		pyautogui.keyUp('fn')
		time.sleep(1)
		os.startfile("D:\cod\cod4\Call of Duty Modern Warfare\iw3mp.exe")
	
	if "make a list" in audio or "make a lift" in audio or "make list" in audio:
		speak("Name the list")
		data_list=recordAudio()
		time.sleep(2)
		speak("Creating list " + data_list)
		data_list= []
		time.sleep(2)	
		speak("Add items")
		for i in range(10):
			i=recordAudio()
			data_list.append(i)
			if(i== 'stop'):
				break
		print data_list			
	
	if "new email" in audio or "new e mail" in audio:
		os.startfile("C:/Windows/system32/cmd.exe")
		time.sleep(2)
		pyautogui.typewrite("mailcheck.py")
		pyautogui.press('enter')
	
speak("Welcome")
time.sleep(1)
def server_run_http():
	os.system("start /wait cmd /c python -m SimpleHTTPServer 8080")
thread.start_new_thread(server_run_http ,())
time.sleep(2)

conn = sqlite3.connect('test.db')


#data=recordAudio()
data="message"
myvoice(data)
	
	
	
	
	
	
	
	

