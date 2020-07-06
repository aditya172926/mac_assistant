#Start the virtual environment to run this program
import os
import speech_recognition as sr
from datetime import datetime

def application(name):
    if len(name)>1:
        name = ' '.join(name)
    else:
        name = str(name[0])
    command = 'open -a "{}"'.format(str(name))
    os.system(command)

keywords = ['application', 'folder', 'desktop', 'open']
print('Be very consize and strictly say what you want to do')
print('To open application say "open application WhatsApp"')    #This is fixed template to open an application. Do not change it
r = sr.Recognizer()

audio_spoken = ''
with sr.Microphone() as source:
    while audio_spoken != 'stop':
        print("Say Something")
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Title", "Say Something"))
        audio = r.listen(source)
        print('Time over')
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Title", "Time Over"))

        try:
            audio_spoken = r.recognize_google(audio)
            f = open('history.txt', 'a')
            f.write('\n\n')
            f.write(str(datetime.now()))
            f.write('\n')
            f.write(audio_spoken)
            f.close()

            spoken_keyword = set(audio_spoken.split()) & set(keywords)
            if 'application' in spoken_keyword:
                spoken_words = audio_spoken.split()
                application(spoken_words[2:])
            
        except:
            pass

# os.system('open "lib"')