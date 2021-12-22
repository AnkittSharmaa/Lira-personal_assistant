import wolframalpha
import wikipedia                             # wikipedia and wolframalpha modules to get answers to users queries
from tkinter import *                        # Tkinter module to display answers on GUI window
import speech_recognition as sr              #Speech Recognition Module was used to take audio input
from apimodule import *                      #Separate Module Created to Stored Personal API key

# Importing all the required modules required 
# to get information

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Listening to Microphone for Audio Input
        print("Speak something....")
        audio = r.listen(source)

        try:
            userInput = r.recognize_google(audio)
            # Performs speech recognition on audio_data (an AudioData instance),
            # using the Google Speech Recognition API and coverting 
            # audio data to text format

            input = "\nHello!! Welcome to Lira-Your Own Assistant \n \n You Asked Me :  "+userInput+" \n\n\n"
            # Storint Greeting Message and question asked in a variable in string format

            if userInput == "stop": #If user says stop, Program will stop implementing
                print("Program will exit")
                break

            else:
                

                try:
                    # Exception handling is done again using try except statement
	
                    window = Tk()   	#Creating main GUI application window with proper dimensions
                    window.geometry("700x600")

                    app_id = api_id 	#YOUR API KEY (storing personal api key in variable)
                    client = wolframalpha.Client(app_id)    
                    res = client.query(userInput)
                    answer = next(res.results).text 
                    # answer is obtained from wolframalpha and is stored

                    print("Answer form WOlfram|Alpha: ")
                    print(answer)

                    # Answer received is printed in GUI window 
                    label1 = Label(window, justify=CENTER, wraplength=650, compound=CENTER,
                                   padx=10, text=input + answer,fg='#063970', font='times 15 bold')
                    label1.pack()

                    # Closing window we created after printing output
                    window.after(7000, lambda: window.destroy())
                    mainloop()

                except Exception as e:

                    window = Tk()   #Creating main GUI application window with proper dimensions
                    window.geometry("700x600")

                    # If no output form wolframalpha then wikipedia is used

                    print("No results from Wolfram|Alpha. Trying Wikipedia.")

                    answer = wikipedia.summary(userInput)      #Answer is obtained using wikipedia.summary method
                   
                    print("Answer form Wikipedia: ")
                    print(answer)
                    
                    # Answer received is printed in GUI window 
                    label1 = Label(window, justify=CENTER, wraplength=650, compound=CENTER,
                                   padx=10, text=input + answer,fg='#873e23', font='times 15 bold')
                    label1.pack()

                    # Closing window we created after showing output
                    window.after(7000, lambda: window.destroy())
                    mainloop()

        except Exception as e:
            # If source unable to listen then print exception

            print(e)
            answer = "Sorry we cannot hear you"
            print(answer)
