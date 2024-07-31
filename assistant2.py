import personal_assistant_api as ast
import datetime
import os
import wolframalpha
import wikipedia
import webbrowser

#wolfram id
wolfram_appid="TG33P5-7XJGEG6PT5"


#name of user
user_name=""


def start_conversation():
    global user_name
    #get username till theare is no error
    ast.speak("what is your name HUMAN?")
    while True:
        user_name=ast.getAudio()
        if user_name!="bad input":
            break

    #find approtiation greeting
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        ast.speak("hello good morning "+user_name)
    elif hour>=12 and hour<18:
        ast.speak("hello good afternoon "+user_name)
    else:
        ast.speak("hello good eavening "+user_name)
    ast.speak("i am your assistant and my name is "+ast.myAssistantName)


#function personal assistant can do
def whatcanido():
    ast.speak("Hello "+user_name)
    ast.speak("My name is "+ast.myAssistantName)
    ast.speak("I can tell you current time and date")
    ast.speak("I can search the web for you. keyword : search")
    ast.speak("I will answer your query. keyword:query")
    ast.speak("I can shutdown your system for you")
    ast.speak("I hope i can be a great help to you")


def querywolfram(user_input):
    #use the same apiid that we have generated earlier
    client=wolframalpha.Client(wolfram_appid)
    res=client.query(user_input)
    try:
        ast.speak(next(res.results).text)
        
    except StopIteration:
        queryWikipedia(user_input)

def queryWikipedia(user_input):
    try:
        results=wikipedia.summary(user_input,sentences=2)
        ast.speak("according to wikipedia")
        ast.speak(results)
    except:
        ast.speak("sorry i dont have an information about this")
        ast.speak("i will do a google serch for you")
        queryGoogle(user_input)

def queryGoogle(user_input):
    webbrowser.open_new_tab(user_input)
    


#start
start_conversation()

while True:
    repeat=input("do you have more")
    if repeat=="no":
        break
    ast.speak("what can i do for you")
    user_input=ast.getAudio().lower()
    if user_input=="bad input":#if error
        continue
    if "thank you" in user_input or "thanks" in user_input:
        ast.speak("you are welcome "+user_name+".")

    if "exit" in user_input or "bye" in user_input or "sleep" in user_input:
        ast.speak("bye "+user_name)
        break
    elif "who are you" in user_input or "how can you help" in user_input or "what can you do" in user_input:    
        whatcanido()

    elif "who made you" in user_input or "who created you" in user_input:
        ast.speak("Priyanshul made me")
    elif "time" in user_input:
        str_time=datetime.datetime.now().strftime("%H:%M:%S")
        ast.speak("Time is "+str_time)

    elif "date" in user_input:
        ast.speak("today is "+str(datetime.date.today()))

    elif "shutdown" in user_input or "shut down" in user_input:
        ast.speak("Your pc will shut down in 30 seconds make sure you save and exit all application")
        os.system('shutdown /s /t 1')
        break
    elif "search" in user_input:
        queryGoogle(user_input)
        
    elif "query" in user_input:
        ast.speak("ask me ")
        user_input=ast.getAudio().lower()
        querywolfram(user_input)








        
        
