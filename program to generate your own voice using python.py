import gtts
import playsound
sound = input("enter a text for speech: ")
m = gtts.gTTS(sound,lang="en")
m.save("s.mp3")
playsound.playsound(s.mp3)