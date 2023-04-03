import PySimpleGUI as sg
import pyttsx3

ENGINE_VARIABLE_SO_REPLACE = pyttsx3.init()
VOICE_VARIABLE_SO_REPLACE =ENGINE_VARIABLE_SO_REPLACE.getProperty("voices")


layout =[[sg.Text("select the type of voice:",text_color="blue", background_color="green" ,),sg.Radio("male","RADIO1",default="true",key="male",
background_color="red",) ,sg.Radio("female","RADIO1",key='female',background_color="red")],
 
 
 
 [sg.Text("enter text to speak:",text_color="white",background_color="purple",)],
 [sg.InputText(key="input"),sg.Button("speak",button_color="orange")],

      ]
                                     

Window =sg.Window("CHOOSE YOUR APPLICATION NAME",layout,background_color="purple")
while True :
    event, values=Window.read()
    if event ==sg.WINDOW_CLOSED:
      break
    elif event =="speak":
      text=values["input"]
if values ["male"]:
          ENGINE_VARIABLE_SO_REPLACE.setProperty("voice",VOICE_VARIABLE_SO_REPLACE[0].id)
elif   values ["female"]:
  ENGINE_VARIABLE_SO_REPLACE.setProperty("voice",VOICE_VARIABLE_SO_REPLACE[1].id)

  ENGINE_VARIABLE_SO_REPLACE.say(text)
  ENGINE_VARIABLE_SO_REPLACE.runAndWait()

  Window.close()

