import pyttsx3

#initialize Text-to-Speech engine
engine = pyttsx3.init()

x = 9
int(x)

while x>1:
    # convert the text entered to speeech
    user_input= input("Type in what you want to say here: ")
    engine.say(user_input)

    # play the speech
    engine.runAndWait()

    # get details of speaking rate
    rate = engine.getProperty("rate")
    print(rate)
    if user_input.upper() == "OFF":
        print("Shutting down")
        x = 0

