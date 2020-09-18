from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3

chatbot = ChatBot("Roberto")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Roberto",
    "Why is your name Roberto?",
    "That is what my creator named me",
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

r = sr.Recognizer()
engine = pyttsx3.init()



while True:
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)


        try:
            
            # convert speech to text
            text = r.recognize_google(audio_data)
            response = chatbot.get_response(text)

            message = "You: {}".format(text)   
            r_response = "Roberto: {}".format(response)

            print(message)
            print(r_response)
    
            engine.say(response)
            engine.runAndWait()    
            print()
        except:
            continue
