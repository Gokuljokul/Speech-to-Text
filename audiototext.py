import speech_recognition as sr
import moviepy.editor as mp

filename = 'hello'

clip = mp.VideoFileClip(filename + ".mp4")
clip.audio.write_audiofile(filename + ".wav")
# clip.audio.write_audiofile("video11.wav", 44100, 2, 2000,"pcm_s32le")
r = sr.Recognizer()


with sr.AudioFile(filename + '.wav') as source:
    audio_text = r.listen(source)
    audio = r.listen(source, phrase_time_limit=3)

    audio = r.listen(source, 0, None)
    try:
        text = r.recognize_google(audio_text)
        timeouttext = r.recognize_google(audio)
        
        print('Converting audio transcripts into text ...')
        print(text)
        print("timeouttext")
        print(timeouttext)
    except e as error:
         print('Sorry.. run again...')
         print(error)
         
         
         

