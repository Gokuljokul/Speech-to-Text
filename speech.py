import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search whatsapp : search whatsapp]')
    print('speak now')
    audio = r3.listen(source)
    
if 'number' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://wa.me/+91'
    with sr.Microphone() as source:
        print ('search your query')
        audio = r2.listen(source)
        
        try:
            get = r2.recognize_google(audio)
            get1 = get.replace(" ","")
            print(get1)
            print(url+get1)
            wb.get().open_new(url+get1)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))