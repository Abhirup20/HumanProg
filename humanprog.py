import pyttsx3
import os

pyttsx3.speak("Welcome to my tools")
print("\n Welcome to my tools")

while True:
  print("\n Chat with me your requirements : "  , end='')
  p = input()
  p=p.lower()
  
  if (("not "  in p) or ("don't" in p) or ("no" in p)) and ("nothing" not in p) and ("notepad" not in p) :
    pyttsx3.speak("Alright, as you say.")
    print("Alright, as you say.")

  elif (("search" in p) or ("find" in p) or ("look" in p) or ("browse" in p))  and (("internet" in p) or ("google" in p))  :
    pyttsx3.speak("Opening google search engine")
    os.system("firefox  google.com")

  elif (("run" in p) or ("open" in p) or ("execute" in p))  and (("firefox" in p) or ("browser" in p))  :
    pyttsx3.speak("Opening firefox web browser")
    os.system("firefox")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or (("text" in p) and ("editor" in p)))  :
    pyttsx3.speak("Opening notepad")
    os.system("notepad")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and ("player" in p) and ("media" in p):
    pyttsx3.speak("Opening windows media player")
    os.system("wmplayer")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and ("paint" in p)  :
    pyttsx3.speak("Opening MS paint")
    os.system("mspaint")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and ("word" in p)  :
    pyttsx3.speak("Opening MS word")
    os.system("winword")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and ("powerpoint" in p)  :
    pyttsx3.speak("Opening MS powerpoint")
    os.system("powerpnt")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and (("excel" in p) or (("spreadsheet" in p) and (("program" in p) or ("editor" in p))))  :
    pyttsx3.speak("Opening MS excel")
    os.system("excel")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and ("calculator" in p)  :
    pyttsx3.speak("Opening calculator")
    os.system("calc")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and (("virtual" in p) or ("on-screen")) and ("keyboard" in p)  :
    pyttsx3.speak("Opening on-screen keyboard")
    os.system("osk")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and (((("adobe" in p) or ("pdf" in p) or ("acrobat" in p)) and ("reader" in p)) or (("adobe" in p) and ("acrobat" in p)))  :
    pyttsx3.speak("Opening adobe acrobat reader")
    os.system("acrord32")

  elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and (("photo" in p) and ("editor" in p)) or ("photoshop" in p)  :
    pyttsx3.speak("Opening adobe photoshop")
    os.system("photoshop")

  elif  ("exit" in p)  or ("quit" in p)  or ("nothing" in p)  or ("stop" in p) or ("bye" in p):
    pyttsx3.speak("Goodbye")
    print("Goodbye.....")
    break

  else:
    pyttsx3.speak("don't support")
    print("don't support")


