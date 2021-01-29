import speech_recognition as speech
import pyttsx3
import wikipedia
import datetime
import pyjokes
import sys

listener = speech.Recognizer()
personal_assistant = pyttsx3.init()
personal_assistant.say("Virtual assistant awaiting your commands")
personal_assistant.runAndWait()
stop = False

def main():
  open_mic()

def open_mic():
  command = ""
  end_session = "end session"
  while True:
    try:
      with speech.Microphone() as source:
        command = get_command(source)
        if not command:
          print(f"Quiting virtual personal assistant")
          break
        #
        key = "pa"
        key = ""
        print(f"Command is: {command}")
        #
        if key in command or "p a" in command:
          words = command.replace(key, "", 1)
          try:
            if not do_something(words):
              message = "Command not found"
              talk(message)
            else:
              talk(f"Please speak a command in 3 seconds")
          except:
            talk(f"Sorry, poor internet connection")
            talk(f"Please say a command again in 3 seconds")
    except:
      print(f"Error, something went wrong.\n")
      input_str = str(input("To quit press q: ")).lower()
      if input_str == "q":
        break

def get_command(source):
  print(f"Virtual Assistant is listening...\n")
  continue_recording = True
  while continue_recording:
    try:
      voice = listener.listen(source, phrase_time_limit=20)
      command = listener.recognize_google(voice)
      command = command.lower()
      if "end session" in command:
        quit()
        return False
      continue_recording = False
    except:
      message = f"Pardon, did not get what you just said."
      personal_assistant.say(message)
      personal_assistant.say("Please try again in 3 seconds")
      personal_assistant.runAndWait()
    #
  return command

def quit(command = f"Ending session now, thanks for your time"):
  personal_assistant.say(command)
  personal_assistant.runAndWait()

def talk(words):
  personal_assistant.say(words)
  personal_assistant.runAndWait()

def do_something(words):
  list_of_commands = {
    "time": tell_me,
    "who is": wiki,
    "what is": wiki,
    "joke": joke
  }
  test = False
  #
  for command in list_of_commands.keys():
    if command in words:
      test = list_of_commands[command](words)
      break
  #
  return test

def joke(words):
  talk(pyjokes.get_joke())
  return True

def wiki(words):
  list_of_commands = {
    "who is": wiki,
    "what is": wiki,
  }
  for command in list_of_commands.keys():
    if command in words:
      search_query = words.replace(command, "")
      info = wikipedia.summary(search_query, 1)
      talk(f"The summary of {search_query} is {info}")
      break
  return True

def tell_me(words):
  time_message =  datetime.datetime.now().strftime("%I:%M %p")
  talk(f"The time is {time_message}")
  return True

if __name__ == "__main__":
  main()