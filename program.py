#Start the virtual environment to run this program
import os
import speech_recognition as sr
from datetime import datetime
from selenium import webdriver

print('=============================================================\n\n')
print('\t\tRules to follow while giving commands')
print('\n1) To open application:- "Open Application <application name>')
print('\n2) To perform a google search:- "Search web for <anything>"')
print('\n3) To perform google search for images:- "Search web for images of <anything>"')
print('\n\nThere is no time limit, speak when you are prompted.')
print('Use headphone for better results')
print('\n\n')
def application(name):
    if len(name)>1:
        name = ' '.join(name)
    else:
        name = str(name[0])
    command = 'open -a "{}"'.format(str(name))
    os.system(command)

def search_web(searchtype, query):
    driver = webdriver.Chrome()
    driver.maximize_window()
    if searchtype != 'image':
        search_results = 'https://www.google.com/search?q='+query+'&rlz=1C5CHFA_enUS860US860&oq=washing&aqs=chrome.0.0j69i57j46j0j69i60j69i65j69i60l2.2604j0j7&sourceid=chrome&ie=UTF-8'
        driver.get(search_results)
    else:
        image_search = 'https://www.google.com/search?q='+query+'&rlz=1C5CHFA_enUS860US860&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqg__ehr3qAhUZyjgGHbcJDrgQ_AUoAXoECAwQAw&biw=1440&bih=788'
        driver.get(image_search)

keywords = ['application', 'folder', 'desktop', 'open']
web_search = ['search', 'web']

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

            spoken_keyword1 = set(audio_spoken.split()) & set(keywords)
            spoken_keyword2 = set(audio_spoken.split()) & set(web_search)

            if 'application' in spoken_keyword1:
                spoken_words = audio_spoken.split()
                application(spoken_words[2:])
            if 'search' in spoken_keyword2 and 'web' in spoken_keyword2:
                spoken_words = audio_spoken.split()
                #search web for images of ----
                if 'image' in spoken_words or 'images' in spoken_words:
                    searchtype = 'image'
                    to_search = spoken_words[4:]
                    query = '+'.join(to_search)
                    print(query)
                    search_web(searchtype, query)
                else:
                    searchtype = 'link'
                    to_search = spoken_words[4:]
                    query = '+'.join(to_search)
                    print(query)
                    search_web(searchtype, query)
        except:
            pass

# os.system('open "lib"')