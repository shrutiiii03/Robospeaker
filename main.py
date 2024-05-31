import pyttsx3 as py
engine=py.init()
engine.say("welcome to robospeaker which converts text to speech. Enter text to be spoken")
engine.runAndWait()
while True:
    x=input("enter text to be spoken")
    if x=='0':
      engine.say("bye bye friend thank you for using robospeaker")
      engine.runAndWait()
      break
    engine.say(x)
    engine.runAndWait()
    
      