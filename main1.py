# prompt for audio input
# assign audio input to a variable
# compare sounds in variable to sounds available and print out the characters

# first of all we have to know the microphe devices available on our device
# this imports the speech_recgnition package
import speech_recognition as s_r

# this prints the version of speech_recognition
print(s_r.__version__)

# this line of code is to return all the microphone devices attached to your pc
print(s_r.Microphone.list_microphone_names())

# this select's the working microphone
my_mic = s_r.Microphone(device_index=1)

# to recognize input from the microphone you have to use a recognizer class.
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)

# now to capture audio from the microphone
with my_mic as source:
    print("Speak now please! ")
    audio = r.listen(source)

# now to convert the the sound taken from the microphone into text
print(r.recognize_google(audio))