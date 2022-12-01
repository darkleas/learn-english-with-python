import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from googletrans import Translator
#playsound 1.2.2
#googletrans 4.0.0rc1
#speechrecognition 3.8.1
#gTTS 2.3.0
r = sr.Recognizer()
translator = Translator()
def SpeakText(word):
    #we get the text that program will recite
    text=word
    print("it is founded! "+word)
    #program recite the text in the language that we gave
    obj = gTTS(text=text,lang='tr',slow=True)
    #save the text as a mp3 file
    obj.save("temporary.mp3")
    #play the file
    playsound('temporary.mp3')
    #remove the file to prevent having lots of not necessary mp3 files
    os.remove("temporary.mp3")
#this function convert the list to string data type
def listtostr(word):
    x = ""
    for i in word:
        x = x + (i + " ")
    return x
while(0.2):
    try:
        with sr.Microphone() as source2:
            audio2 = r.listen(source2)
            my_voice = r.recognize_google(audio2)
            #in this condition we check if the user wants to translate anything.
            #so, If we want to translate anything, we say copy at the end of the talk
            if my_voice.split()[-1] == "copy":
                #remove the copy word in the sentence in the next 3 lines of code
                my_voice = my_voice.split()
                my_voice.remove('copy')
                my_voice = listtostr(my_voice)
                print('looking for the meaning of '+my_voice)
                print("loading...")
                #we translate the thing we say in the code below. we can choice the language that we want to translate to
                translated = translator.translate(my_voice, dest='tr').text
                #the function that recite the translated text
                SpeakText(translated)
    except sr.UnknownValueError:
        print("unknown error occurred!")
        continue