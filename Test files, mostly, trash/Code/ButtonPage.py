from tkinter import *
from PIL import Image, ImageTk
import tkinter
import re
import pandas as pd
import nltk
import tensorflow
import tflearn
import random
import numpy as np
import pickle
from nltk.stem import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

import discord
import os  # default module
from dotenv import load_dotenv
import json


stemmer=SnowballStemmer('spanish')


# _____________________________________________ PYTHON WINDOW ____________________________________________________
def ventana():
    print("ENTRA AL CHATBOT")

    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]
        s_words = nltk.word_tokenize(s)  # Convierto la frase ingresada por el usuario en palabras
        s_words = [stemmer.stem(word.lower()) for word in s_words]
        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return np.array(bag)

    def chatbot_response(msg):
        import json
        with open('intents.json') as file:
            data = json.load(file)

        try:
            with open("data.pickle", "rb") as f:
                words, labels, training, output, data = pickle.load(f)

            with open('intents.json') as file:
                data2 = json.load(file)

            if data != data2:
                raise Exception("El Archivo json ha cambiado")
            model.load("model.tflearn")

        except:
            print("Estoy dentro del EXCEPT")

            words = []  # Palabras sin deferenciar la frase a la que pertenecen
            labels = []  # Titulos, legendas.
            docs_x = []
            docs_y = []

            for intents in data['intents']:
                for patterns in intents['patterns']:
                    wrds = nltk.word_tokenize(patterns)  # Convierte una frase a un conjunto de palabras
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intents["tag"])

                    if intents['tag'] not in labels:
                        labels.append(intents['tag'])

            words = [stemmer.stem(w.lower()) for w in words if w != "?"]

            words = sorted(list(set(words)))  # Organizando el conjunto de paralabras de forma no repetiva y ordenada.

            labels = sorted(labels)

            training = []
            output = []

            out_empty = [0 for _ in range(len(labels))]

            # Este ciclo for se encarga de analizar todas y cada una de las palabras en todas y cada una de las frases

            for x, doc in enumerate(docs_x):
                bag = []

                wrds = [stemmer.stem(w.lower()) for w in doc]

                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                    output_row = out_empty[:]
                    output_row[labels.index(docs_y[x])] = 1

                    training.append(bag)
                    output.append(output_row)

            training = np.array(
                training)  # Contiene la informacion preparada con la cual se va a alimentar el sistema referentes a las palabras
            output = np.array(
                output)  # Contiene la informacion preparada con la cual se va a alimentar el sistema referente a la categorizacion

        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output, data), f)

        tensorflow.compat.v1.reset_default_graph()

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)

        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)

        try:
            model.load("model.tflearn")
        except:
            model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
            model.save("model.tflearn")

        results = model.predict([bag_of_words(msg, words)])
        results_index = np.argmax(results)  # La funcion argmax obtiene la probabilidad mas alta.

        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
            # else if tg['tag'] == 'Cotizacion'

        return (random.choice(responses))

    def send():
        msg = EntryBox.get("1.0", 'end-1c').strip()
        print("mensaje captado: ", EntryBox.get("1.0", "end-1c"))

        print("\nborrando....")
        EntryBox.delete("0.0", END)
        print("mensaje borrado: ", EntryBox.get("1.0", "end-1c"))

        res = chatbot_response(msg)

        if msg != "":
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + " \n\n")
            ChatLog.config(foreground="black", font=("Verdana", 12))
            ChatLog.insert(END, "ChatBot: " + res + " \n\n")
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

    base = Tk()
    base.title("Chatbot (Atención al usuario)")
    base.geometry("400x500")
    base.config(bg="#00a9e0")
    base.resizable(width=FALSE, height=FALSE)  # Mantiene fija la ventana.

    ChatLog = Text(base, bd=0, bg="white", width=8, height="50", font="Arial")
    ChatLog.config(foreground="Black", font=("Verdana", 12))  # foreground cambia el color de la letra
    ChatLog.insert(END, "Bienvenido\n\n")
    ChatLog.place(x=6, y=6, height=386, width=370)
    ChatLog.config(state=DISABLED)  # bloquea la entrada de texto(lo hace de solo lectura)

    scrollbar = Scrollbar(base, command=ChatLog.yview(), cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=376, y=6, height=386)

    EntryBox = Text(base, bg="white", height="5", width=29, font="Arial")
    EntryBox.place(x=6, y=401, height=90, width=265)

    SendButton = Button(base, font=("Verdana", 12, "bold"), text="Send", height="5", width="9",
                        bd=3, bg="white", activebackground="#0689d8", fg='#0689d8', command=send)
    SendButton.place(x=282, y=401, height=90)

    base.bind('<Return>', lambda event: send())

    #  Primer parameter: posición
    #  ChatLog.grid(column=0, row=0)

    base.mainloop()



def pytk():
    buttonPage.destroy()
    # _______Validaciones______
    def es_nombre(nombre):
        nombre = nombre.replace(' ', '')

        if nombre.isalpha() == False:
            nombre = ""
            raise ValueError()

    # ___ Telefono ___
    def validar_telefono(numero):
        patron = re.compile(r'^\d{4}\d{4}$')

        return patron.match(numero)

    # ____ Correo ____
    def validar_correo(correo):
        print("está validando")
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(patron, correo):
            print("validó el correo")
            return True
        else:
            return False

    # ______ Guardar el archivo en csv _________

    def save_to_csv(email, name, tel, subscribed):
        dict = {'Name': '', 'eMail': '', 'Phone': 0, 'Subscribed': ''}

        dict['Name'] = name
        dict['eMail'] = email
        dict['Phone'] = tel
        dict['Subscribed'] = subscribed

        try:
            df = pd.DataFrame(dict, index=[0])
            df.to_csv("informe.csv", sep=";", mode='a', index=False, header=False)
            pass

        except:
            df = pd.DataFrame(dict, index=[0])
            df.to_csv("informe.csv", sep=";", index=False)
            pass

    # _________ validar correo y telefono ________
    def validate():
        email = correo_in.get("1.0", "end-1c").strip()
        name = nombre_in.get("1.0", "end-1c").strip()
        tel = tel_in.get("1.0", "end-1c").strip()

        if checkvar.get() == 0:
            subscribed = 'No'
        else:
            subscribed = 'yes'

        if validar_correo(email):
            print("CORREO VALIDO")
            validate_mail = True
        else:
            tkinter.messagebox.showerror(message="Correo inválido", title="ERROR")
            print("CORREO INVALIDO")
            validate_mail = False
        if validar_telefono(tel):
            print("NUMERO VALIDO")
            validate_phone = True
        else:
            print("NUMERO INVÁLIDO")
            tkinter.messagebox.showerror(
                message="Numero de teléfono inválido, no incluyas letras ni caracteres especiales",
                title="ERROR")
            validate_phone = False

        if (validate_phone and validate_mail):
            print("datos guardados...")
            save_to_csv(email, name, tel, subscribed)  # Guarda
            log_in.destroy()  # Cierra la ventana del LOGIN
            ventana()  # Corre el chatbot
            print("\n○\nLanzando chatbot...")
    names = []
    emails = []
    phones = []
    subs = []
    informe = pd.DataFrame()
    headers = ["Name", "eMail", "Number", "Subscribed"]
    # __________________________ front end __________________________
    log_in = Tk()
    log_in.geometry("550x500")
    log_in.title("Inicia sesión")
    log_in.resizable(width=False, height=False)

    # ______ Imagen Background _______
    imagen = PhotoImage(file="SamsungBackground.png")
    background_label = Label(log_in, image=imagen)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    texto1 = "introduce tu nombre"

    # ______ Label que indica al usuario que ingrese el nombre _______

    nombre_lab = Label(log_in, compound=CENTER, text=texto1, image=imagen, padx=100, pady=70, takefocus=True)
    nombre_lab.config(foreground="white", font=("Montserrat, sans-serif", "12", "bold"))
    nombre_lab.place(x=100, y=70, height=25, width=170)

    # ______ Usuario ingresa el nombre _______
    nombre_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
    nombre_in.config(foreground="black", font=("Verdana", 12))
    nombre_in.place(x=100, y=100, height=25, width=350)

    # ______ Label que indica al us-uario que ingrese el correo _______

    correo_lab = Label(log_in, width=1, height="5", font="Arial", compound=CENTER, image=imagen,
         text="Introduce tu correo electronico")
    correo_lab.config(foreground="white", font=("Montserrat, sans-serif", 12, "bold"), bd=1,  background="ghost white")
    correo_lab.place(x=100, y=145, height=25, width=240)

    w_mail = Label(log_in, width=1, height="5", font="Arial", compound=CENTER, image=imagen,
                   text="(nombre@dominio.com)")
    w_mail.config(foreground="white", font=("Montserrat, sans-serif", 7))
    w_mail.place(x=350, y=150, height=20, width=100)

    # ______ Usuario ingresa el correo _______
    correo_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
    correo_in.config(foreground="black", font=("Verdana", 12))
    correo_in.place(x=100, y=175, height=25, width=350)

    # ______ Label que indica al usuario que ingrese el numero de telefono _______

    tel_lab = Label(log_in, bd=0, width=1, height="5", font="Arial", compound=CENTER, image=imagen,
                    text="Introduce tu numero de telefono")
    tel_lab.config(foreground="white", font=("Montserrat, sans-serif", 12, "bold"))
    tel_lab.place(x=100, y=220, height=25, width=253)

    w_tel = Label(log_in, bd=0, bg="ghost white", width=1, height="5", font="Arial", compound=CENTER, image=imagen,
                  text="(xxxxxxxx)")
    w_tel.config(foreground="white", font=("Montserrat, sans-serif", 8))
    w_tel.place(x=370, y=220, height=25, width=60)

    # ______ Usuario ingresa el numero de telefono _______
    tel_in = Text(log_in, bd=0, bg="white", width=1, height="5", font="Arial")
    tel_in.config(foreground="black", font=("Verdana", 12))
    tel_in.place(x=100, y=250, height=25, width=350)

    # __________ SMI Logo ___________

    samsung_logo = ImageTk.PhotoImage(Image.open("Samsung.png"))
    samsung_label = Label(log_in, image=samsung_logo, background="#0689d8", compound=CENTER)
    samsung_label.place(x=100, y=350)

    # _______ Checkvar ___________

    checkvar = IntVar()
    check_btn = tkinter.Checkbutton(log_in, text="¿Deseas estar suscribirte a nuestro portal?",
                                    variable=checkvar)
    check_btn.config(background="#0689d8", bd=3, font=("Montserrat, sans-serif", 9), foreground="white")
    check_btn.place(x=95, y=300)

    # _______ Botón de enviar ___________
    sendButton = Button(log_in, font=("Montserrat, sans-serif", 12, "bold"),
                        text="Enviar", height="5", width="9",
                        bd=3, bg="#0689d8", activebackground="#1428a0",
                        fg='white', command=validate)
    sendButton.place(x=350, y=350, height=90)

    # ______ Crear dataframe para guardar los datos ________


    log_in.mainloop()


# _________________________________________ LINK WITH DISCORD __________________________________________________________


def run_discord():
    buttonPage.destroy()
    stemmer = LancasterStemmer()
    tag = ''

    with open('intents.json') as json_data:
        intents = json.load(json_data)

    words = []
    classes = []
    documents = []
    ignore_words = ['?','¿']
    print("Looping through the Intents to Convert them to words, classes, documents and ignore_words.......")
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # tokenize each word in the sentence
            w = nltk.word_tokenize(pattern)
            # add to our words list
            words.extend(w)
            # add to documents in our corpus
            documents.append((w, intent['tag']))
            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    print("Stemming, Lowering and Removing Duplicates.......")
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    print (len(documents), "documents")
    print (len(classes), "classes", classes)
    print (len(words), "unique stemmed words", words)
    print("Creating the Data for our Model.....")
    training = []
    output = []
    print("Creating an List (Empty) for Output.....")
    output_empty = [0] * len(classes)

    print("Creating Traning Set, Bag of Words for our Model....")
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append([bag, output_row])

    print("Shuffling Randomly and Converting into Numpy Array for Faster Processing......")
    random.shuffle(training)
    training = np.array(training)

    print("Creating Train and Test Lists.....")
    train_x = list(training[:,0])
    train_y = list(training[:,1])
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
    net = tflearn.regression(net)
    print("Training....")
    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

    model.load('model.tflearn')
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(sentence, words, show_details=False):
        sentence_words = clean_up_sentence(sentence)
        bag = [0]*len(words)
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))

    ERROR_THRESHOLD = 0.25
    print("ERROR_THRESHOLD = 0.25")

    def classify(sentence):
        results = model.predict([bow(sentence, words)])[0]
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((classes[r[0]], r[1])) #Tuppl -> Intent and Probability
        return return_list

    def response(sentence, userID='123', show_details=False):
        results = classify(sentence)
        if results:
            while results:
                for i in intents['intents']:
                    if i['tag'] == results[0][0]:
                        return i

                results.pop(0)

    load_dotenv() # load all the variables from the env file
    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")

    @bot.event
    async def on_message(message):
        global tag

        if tag != 'greeting':
            if message.author != bot.user:
                # SENDS BACK A MESSAGE TO THE CHANNEL.
                await message.channel.send(random.choice(response(message.content)['responses']))
                tag = response(message.content)['tag']
        else:
            nombre = ''
            for i in message.content:
                if (i.isnumeric()) == False:
                    nombre += i
            if message.author != bot.user:
                await message.channel.send(('Bienvenido ' + nombre))
                tag = response(message.content)['tag']

    @bot.slash_command(name = "hello", description = "Say hello to the bot")
    async def hello(ctx):
        await ctx.respond("Hey!")



    control_window = Tk()
    control_window.config(height=250, width=250)
    buttonPage.title("Controlando el sistema")
    control_window.mainloop()


    bot.run(os.getenv('TOKEN'))


# __________________________________________ BUTTON WINDOW _____________________________________________________________

buttonPage = Tk()
buttonPage.config(height=250, width=500)
buttonPage.title("Bievenido")
buttonPage.resizable(width=False, height=False)


# _______________ ICONS ___________________
photo_discord = PhotoImage(file="discordd.png")
photo_telegram = PhotoImage(file="telegramm.png")
photo_python = PhotoImage(file="python.png")
background = PhotoImage(file="FirstScreen_background.png")


# ________________ LABELS __________________
background_label = Label(buttonPage, image=background)
background_label.place(x=0,y=0)

# __________ principal label _______________
label_principal = Label(buttonPage, height=2, width=30,
                      text="¿Donde desea iniciar el chatbot?", bg="#0057b8",
                      foreground="white", font=("Verdana", 12, "bold")
                        )
label_principal.place(x=85, y=50)

# __________ DISCORD LABEL _________________

label_discord = Label(buttonPage, height=1, width=8,
                      text="DISCORD",
                      foreground="white", font=("Verdana", 8, "bold"),
                      background="#0057b8")
label_discord.place(x=90, y=190)

# __________ TELEGRAM LABEL ________________
label_telegram = Label(buttonPage, height=1, width=9,
                      text="TELEGRAM",
                      foreground="white", font=("Verdana", 8, "bold"),
                      background="#0057b8")
label_telegram.place(x=215, y=190)
# __________ PYTHON LABEL  _________________
label_python = Label(buttonPage, height=1, width=9,
                      text="PYTHON",
                      foreground="white", font=("Verdana", 8, "bold"),
                      background="#0057b8")
label_python.place(x=340, y=190)

# ____________ DISCORD BUTTON ____________
iniciar_discord = Button(buttonPage, height=50, width=75, bg="white",
                         foreground="black", text="Discord", image=photo_discord,command=run_discord)
iniciar_discord.place(x=85, y=120)

# ____________ TELEGRAM BUTTON ____________
iniciar_telegram = Button(buttonPage, height=50, width=75, bg="white", foreground="black", text="Telegram", image=photo_telegram)
iniciar_telegram.place(x=215, y=120)

# ____________ PYTHON BUTTON ____________
iniciar_interfaz = Button(buttonPage, height=50, width=75,
                          bg="white", foreground="black", text="Interfaz", image=photo_python,
                          command=pytk)
iniciar_interfaz.place(x=340, y=120)

buttonPage.mainloop()
