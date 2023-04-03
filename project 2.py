import PySimpleGUI as sg
import pyttsx3

Source_Engine = pyttsx3.init()
Speech_Source_Engine =Source_Engine.getProperty("voices")


layout =[[sg.Text("Choose preferred voice type:",text_color="white", background_color="blue" ,),sg.Radio("Male","RADIO1",default="true",key="Masculine",
background_color="white",) ,sg.Radio("Female","RADIO1",key='Feminine',background_color="white")],
 
 
 
 [sg.Text("Input a text to Speak:",text_color="blue",background_color="white",)],
 [sg.InputText(key="input text"),sg.Button("speak",button_color="black")],

      ]
                                     

Window =sg.Window("CHOOSE YOUR APPLICATION NAME",layout,background_color="white")
while True :
    event, values=Window.read()
    if event ==sg.WINDOW_CLOSED:
      break
    elif event =="speak":
      text=values["input"]
if values ["MAsculine"]:
          Source_Engine.setProperty("voice",Speech_Source_Engine[0].id)
elif   values ["Feminine"]:
  Source_Engine.setProperty("voice",Speech_Source_Engine[1].id)

  Source_Engine.say(text)
  Source_Engine.runAndWait()

  Window.close()

