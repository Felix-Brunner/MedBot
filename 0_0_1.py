import time
import re
import sys
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import sqlite3
import requests
import webbrowser

version_self = 1
verbindung = sqlite3.connect("krankheiten.db")


class updater:
    url = 'https://raw.githubusercontent.com/Felix-Brunner/MedBot/main/newerst_version.txt'
    page = requests.get(url)
    version = int(page.text)
    if version_self < version:
        update = Tk()
        update.title("Updater")
        update.geometry("300x100")
        text1 = Label(
            update,
            text=
            "Eine neue Version ist verfügbar!\n Für mehr Infos clicke auf GitHub"
        )
        text1.pack()

        def openweb():
            webbrowser.open(
                "https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270"
            )

        Btn = Button(update, text="GitHub", command=openweb)
        Btn.pack()


class lizens:
    def print():
        return ("Programm von:\n Clara Köttel, Felix Brunner, Lukas Brunner")


class ki1_gui:
    def create_gui():
        global MainGui
        MainGui = Tk()
        MainGui.title("Med Bot - Arzt")
        MainGui.geometry("1200x1200")
        MainGui.config(bg="paleturquoise")
        
        def backitoff():
          MainGui.destroy()
          menue.create_Menue()
        #canvas = Canvas(MainGui, width=1000, height=1000)

        #image = PhotoImage(file="logomedbot.png")
        #background_label = Label(MainGui, image=image)
        #background_label.place(x=200, y=430)
        


        ausgabe = tk.Text(
            MainGui, background='teal', fg='white', cursor='xterm')
        ausgabe.config(state="disabled")
        ausgabe.config(heigh=30)
        ausgabe.config(width=70)
        ausgabe.place(x=0, y=0)
        S = Scrollbar(MainGui)
        S.place(x=570, y=10)
        S.config(command=ausgabe.yview)
        ausgabe.config(yscrollcommand=S.set)  
        eingabe = Entry(MainGui)
        eingabe.config(bg="lightcoral")
        eingabe.config(width=70)
        eingabe.place(x=0, y=550)
        S2 = Scrollbar(MainGui)
        S2.place(x=790, y=10)
        symp_list = tk.Text(
            MainGui, background='teal', fg='white', cursor='xterm')
        
        symp_list.insert(END, "Liste aller Symptome,\ndie ich kenne\n(alphabetisch):")
        symp_list.config(state="disabled")
        symp_list.config(heigh=30)
        symp_list.config(width=25)
        symp_list.place(x=585, y=0)
        S2.config(command=symp_list.yview)
        symp_list.config(yscrollcommand=S.set)  

        back = Button(MainGui, background='darkslategray', fg='white', text='Zurück zum Menü', command=backitoff)
        back.place(x=650, y=550)

        def printallsymptomes():
            #verbindung = sqlite3.connect("test.db")
            zeiger = verbindung.cursor()
            zeiger.execute("SELECT  symptom1 FROM krankheiten")
            inhalt = zeiger.fetchall()
            allesymptome = []
            for x in inhalt:
                x = str(x)
                x = x.replace(",","")
                x = x.replace("'","")
                x = x.replace("(","")
                x = x.replace(")"," ")
                #print(x)
                allesymptome.append(x)
                
            zeiger.execute("SELECT  symptom2 FROM krankheiten")
            inhalt = zeiger.fetchall()
            for x in inhalt:
                x = str(x)
                x = x.replace(",","")
                x = x.replace("'","")
                x = x.replace("(","")
                x = x.replace(")"," ")
                allesymptome.append(x)

            zeiger.execute("SELECT  symptom3 FROM krankheiten")
            inhalt = zeiger.fetchall()
            for x in inhalt:
                x = str(x)
                x = x.replace(",","")
                x = x.replace("'","")
                x = x.replace("(","")
                x = x.replace(")"," ")
                allesymptome.append(x)
                
            zeiger.execute("SELECT  symptom4 FROM krankheiten")
            inhalt = zeiger.fetchall()
            for x in inhalt:
                x = str(x)
                x = x.replace(",","")
                x = x.replace("'","")
                x = x.replace("(","")
                x = x.replace(")"," ")
                allesymptome.append(x)
                
            zeiger.execute("SELECT  symptom5 FROM krankheiten")
            inhalt = zeiger.fetchall()
            for x in inhalt:
                x = str(x)
                x = x.replace(",","")
                x = x.replace("'","")
                x = x.replace("(","")
                x = x.replace(")"," ")
                allesymptome.append(x)

            allesymptome = list(dict.fromkeys(allesymptome))
            return allesymptome


        symp_list.config(state="normal")
        allesymptome_list_alphabe = printallsymptomes()
        allesymptome_list_alphabe = sorted(allesymptome_list_alphabe)
        
        for x in allesymptome_list_alphabe:
            symp_list.insert(END, x + "\n")

        symp_list.config(state="disabled")
            
        #eingabe.grid(row=1, column=1, sticky="nsew")
        def writeinausgabe(text):
            ausgabe.config(state="normal")
            ausgabe.insert(END, "\n")
            ausgabe.insert(END, text)
            ausgabe.insert(END, "\n")
            ausgabe.config(state="disabled")

        def datenbank(symptome_suche):
            zeiger = verbindung.cursor()
            zeiger.execute("SELECT * FROM krankheiten")
            inhalt = zeiger.fetchall()
            krankheiten = {}

            for x in inhalt:
                symtome_gegeben = {
                    x[2].lower(), x[3].lower(), x[4].lower(), x[5].lower(),
                    x[6].lower()
                }
                set1 = set(symptome_suche)
                set2 = set(symtome_gegeben)
                set3 = set1.intersection(set2)
                found = []

                for match in set3:
                    found.append(match)

                try:
                    if found[0] != " ":
                        krankheiten[x[0]] = len(found)

                except:
                    pass

            ergebniss = list(krankheiten.keys())
            #for x in range(0, len(ergebniss)):
            #print(ergebniss[x])

            try:
                moeglich = str(', '.join(ergebniss))

                if moeglich == "":
                    a + b  #erzeugt fehler für try/except

                antworten_sg = [
                    "Du köntest die folgende Krankheit haben: " + moeglich,
                    "Es sieht danach aus, als hättest du " + moeglich + ".",
                    "Es könnte sein, dass du " + moeglich + " hast.",
                    "Vielleicht hast du " + moeglich + "."
                ]
                antworten_pl = [
                    "Du köntest einer der folgenden Krankheit haben: " +
                    moeglich,
                    "Es sieht danach aus, als hättest du einer dieser Krankheiten: "
                    + moeglich + ".",
                    "Es könnte sein, dass du einer dieser Krankheiten hast: " +
                    moeglich, "Vielleicht hast du einer dieser Krankheiten " +
                    moeglich + "."
                ]
                try:
                    moeglich_pl = ergebniss[1]
                    writeinausgabe("Bot: " + random.choice(antworten_pl) +
                                   "\n")

                except:
                    writeinausgabe("Bot: " + random.choice(antworten_sg) +
                                   "\n")

                y = 0
                for x in ergebniss:
                    zeiger.execute(
                        "SELECT * FROM krankheiten WHERE krankheit =?",
                        (ergebniss[y], ))
                    inhalt = zeiger.fetchall()
                    quelle = inhalt[0][1]
                    writeinausgabe("Bot: Die Krankheit " + ergebniss[y] +
                                   "\n habe ich hier gefunden: \n" + quelle)
                    y = y + 1

                writeinausgabe(
                    "Bot: Bitte beachte, dass ich nur ein Computer bin und keinen Arzt erstzen kann! \n Sollte es dir schlecht gehen, suche einen Arzt auf \n oder Rufe die Nummer 1450 an.\n"
                )

            except:
                writeinausgabe(
                    "Bot: Ich habe leider keine passende Krankheit gefunden!\n Überprüfe bitte die Eingabe deiner Symptome! \n "
                )

        writeinausgabe(
            "Bot: Servus! Welche Symptome hast Du? \n Bitte schreibe sie einzelnd und mit einem Beistrich getrennt.\n Zum Beispiel: Husten, Kopfschmerzen \n"
        )
        writeinausgabe(
            "Bot: Je mehr Symptome Du angibst, desto genauer ist die Diagnose!\n"
        )

        def ki1(eingabetext):
            if eingabetext == "hi":
                writeinausgabe(
                    "Bot: Servus! Welche Symptome hast du? \n Bitte schreibe sie einzelnd und mit einem Beistrich getrennt.\n Zum Beispiel: Husten, Kopfschmerzen \n"
                )

            elif eingabetext == "lizens":
                writeinausgabe(lizens.print())
            
            elif "danke" or "dank" in eingabetext:
                antworten_danke = ["Habe ich gerne gemacht!", "Gern geschehen!", "Immer wieder gerne!"]
                writeinausgabe("Bot: " + random.choice(antworten_danke))

            else:
                sympthome = eingabetext.lower().split(",")
                datenbank(sympthome)

        def comp_s(event):
            #print(eingabe.get())
            ausgabe.config(state="normal")
            eingabetxt = eingabe.get()
            eingabestr = "Du: " + eingabe.get() + "\n"
            ausgabe.insert(END, eingabestr)
            ausgabe.config(state="disabled")
            eingabe.delete(0, END)
            ki1(eingabetxt)


        MainGui.bind('<Return>', comp_s)


def create():
  main = Tk()
  main.geometry('800x1000')
  main.configure(bg='mediumorchid')
 # picture = PhotoImage()
#background_label = Label(main, image=picture)
 # background_label.place(x=0, y=0)

  connection = sqlite3.connect("erstehilfe.db")
  c = connection.cursor()
  main.title("Erste Hilfe'  ' - Fragen")

  #wähle eine Frage aus und übergebe Datenpacket
  def frage_auswählen():
      c.execute("SELECT * FROM ehexzwei ORDER BY RANDOM() LIMIT 1")
      daten = c.fetchone()
      (problem, quelle, stichwort1, stichwort2, stichwort3, stichwort4, stichwort5, reihenfolge, infos) = daten
      print(daten)
      global lists
      lists = daten
      return daten
  #WORK NEEDS TO BE DONE: Split answer, 0 or 1?, split stichwörter with '/',  control if
  #answer contains stichwörter
  def thinking():
      print('hier kommt die aktuelle liste am beginn von thinking')
      print(lists)
      print('das war die aktuelle liste zu beginn von thinking')
      answersi = []
      answer = entry_field.get()
      answer = answer + ' '
      answersi = re.split('; |, |\*|\n| ', answer)
  #    answersi = answer.split(", ")
  #    answersi = re.split('r\W+', answer)
      answersi.remove(answersi[len(answersi) - 1])
      l = len(answersi)
      answersi = [ans.lower() for ans in answersi]
      correct_answers = 0
      chosen_element = 0
      stichwort_number = 2
      print(answersi)
      if lists[5] == '' and lists[6] == '':
          anzahl_stichworte = 3
      elif lists[6] == '' and lists[5] != '':
          anzahl_stichworte = 4
      else:
          anzahl_stichworte = 5
      print(anzahl_stichworte)
      print(lists)
  # wenn sie in der richtigen Reihenfolge sein müssen
      if lists[7]==1:
          for rounds in range(0,l):
              if answersi[chosen_element] == (lists[stichwort_number]):
                  correct_answers = correct_answers + 1
                  stichwort_number = stichwort_number + 1
                  chosen_element = chosen_element + 1
                  print('one correct answer!')
              else:
                  print('Testelement ' + answersi[chosen_element] + ' is not matching ' + lists[stichwort_number])
                  rounds = rounds - 1
                  chosen_element = chosen_element + 1
      elif lists[7] == 0:
          for rounds in range(0, anzahl_stichworte):
              if lists[stichwort_number] in answersi:
                  stichwort_number = stichwort_number + 1
                  correct_answers = correct_answers + 1
                  print('one correct answer', lists[stichwort_number])
              else:
                  print('it does not work') 
      print(correct_answers)    
      if correct_answers == anzahl_stichworte:
          friendly.config(text = 'Correct')
          aktuell = punkte.get() + 1
          punkte.set(aktuell)
      else:
          friendly.config(text = 'Wrong')
          friendly.pack(anchor=N)
          wrong.set('Möchtest du die Stichworte sehen?')
          buttonshow.pack(anchor=N)
      information.pack(anchor=N)
      entry_field.configure(state=DISABLED)
      next_question.pack(anchor=S)
                        
  #beende das Programm            
  def end():
      menue.create_Menue()
      main.destroy()

  #show stichworte
  def show_stichworte():
      wrong.set(wrongis)
  #öffne website
  def visiting():
      webbrowser.open(website, True)
      print(website)

  #Beginne nächste Frage
  def nexti():
      wrong.set('Bei Fragen schaue dir die weiteren Infos an!')
      againa()
      #correction.pack_forget()
      information.pack_forget()
      buttonshow.pack_forget()
      next_question.pack_forget()
      entry_field.configure(state=NORMAL)
      entry_field.delete(0, 500)

  #Hauptfunktion
  def againa():
      entry_field.delete(0, 500)
      print('againa')
      global lists
      lists = frage_auswählen()
      question.set(lists[0])
      stichwörter1 = (lists[2], lists[3], lists[4], lists[5], lists[6])
      stichwörter1 = [stichworts.capitalize() for stichworts in stichwörter1]
      global wrongis
      wrongis = ' '.join([str(elem) for elem in stichwörter1])
      wrong.set(wrongis)
      print('DEBUGGINGGGGGGGGGGGG')
      print(wrongis)
      print(lists)
                        
      further.set(lists[8])
      global website
      website = lists[1]
      print(website)
      friendly.config(text='Was denkst du?')
      main.update()

  frame = Frame(main)
  frame.pack()
  question = StringVar()
  punkte = IntVar()
  punkte.set(0)
  wrong=StringVar()

  next_question = Button(main, text='Nächste Frage', command=nexti)
  next_question.pack_forget()

  button = Button(main, text='Zurück zum Menü', command=end, bg='mediumspringgreen')
  button.pack(anchor=SE)

  friendly = Label(main, text='Gib die Antwort ein!', bg='mediumspringgreen')
  friendly.pack(anchor=S)

  label = Label(main, textvariable=question, relief=RAISED )
  label.pack(anchor=N)

  now_more = Button(main, text='Erhalte weitere Information', relief=RAISED, command=visiting)
  now_more.pack(anchor=E)

  sol = 'Ägypten'
  solution = []



  #correction = Label(main, textvariable=wrong, bg='crimson')
  buttonshow = Button(main, textvariable=wrong, command=show_stichworte, bg='crimson')

  further = StringVar()

  information = Label(main, textvariable=further, bg='chartreuse', wraplength=300)

  entry_field = Entry(frame, bd=0)
  entry_field.pack(side=RIGHT)

  stand = Label(main, text='Aktueller Punktestand', bg='deepskyblue')
  stand.pack(anchor=S)
  punktestand = Label(main, textvariable=punkte, bg='lightskyblue')
  punktestand.pack(anchor=S)
  # i = Anzahl der gegebenen Stichwörter
  #i = 5
  finalize = Button(frame, text='Fertig', command=thinking)
  finalize.pack(side=LEFT)
  againa()


def create_quiz():
    main = Tk()
    main.geometry('800x1000')
    main.configure(bg="mediumorchid")

    connection = sqlite3.connect('krankheiten.db')

    c = connection.cursor()
    main.title('Krankheiten & ihre Symptome' + ' - Fragen')
    #Choose question
    def frage_auswählen():    
        c.execute("SELECT * FROM krankheiten ORDER BY RANDOM() LIMIT 1")
        res = c.fetchone()
        (problem, quelle, sym1, sym2, sym3, sym4, sym5) = res
        print(res)
        return res

    #Check players answer
    def thinking():
        if (int(v.get()) ==1 and solution==first) or (int(v.get())==2 and solution==second) or (int(v.get())==3 and solution==third) or (int(v.get())==4 and solution==fourth):
            friendly.config(text = 'Richtig!')
            aktuell = punkte.get() + 1
            punkte.set(aktuell)
        else:
            friendly.config(text = 'Leider nein, richtig ist')
            friendly.pack(anchor=N)
            #correct.pack(anchor=N)
            information.pack(anchor=N)
        choice1.configure(state=DISABLED)
        choice2.configure(state=DISABLED)
        choice3.configure(state=DISABLED)
        choice4.configure(state=DISABLED)
        next_question.pack(anchor=S)


       
    #Choose random wrong answers
    def find_dummies():
        for i in range(0, 3):
                c.execute("SELECT symptom1, symptom2, symptom3, symptom4, symptom5 FROM krankheiten ORDER BY RANDOM() LIMIT 4")
                dummies = c.fetchall()
                (sym1, sym2, sym3, sym4,) = dummies
                print(dummies)
                return dummies    
        #print(dummies)
        #return dummies

    def end():
        global again
        again = False
        main.destroy()
        menue.create_Menue()

    def visiting():
        webbrowser.open(website, True)
        print(website)

    def againa():
        v.set(5)
        global not_selected
        global lists
        lists = frage_auswählen()
        global dums
        dums = find_dummies()
        loi.set(lists[0])
        global website
        website = lists[1]

        global sol
        sol = (lists[2], lists[3], lists[4], lists[5], lists[6])
        sol = ', '.join([str(elem) for elem in sol])
        sol = sol.rstrip(", ")

        global f
        info.set(sol)
        f = dums[0]
        f = ', '.join([str(elem) for elem in f])
        f = f.rstrip(", ")
        s = dums[1]
        s = ', '.join([str(elem) for elem in s])
        s = s.rstrip(", ")
        t = dums[2]
        t = ', '.join([str(elem) for elem in t])
        t = t.rstrip(", ")
        fo = dums[3]
        fo = ', '.join([str(elem) for elem in fo])
        fo = fo.rstrip(", ")

        first.set(f)
        second.set(s)
        third.set(t)
        fourth.set(fo)
        buttons = [first, second, third, fourth]
        global solution

        if f==sol:
            solution = first
        elif s==sol:
            solution = second
        elif t==sol:
            solution = third
        elif fo==sol:
            solution = fourth
        else:
            chosen = random.choice(buttons)
            chosen.set(sol)
            solution = chosen
        print(sol)
        print(dums[0], dums[1], dums[2], dums[3])

        friendly.config(text='Was sind die Symptome?')
        main.update()
        print('random')    
        print('starting again')

    def nexti():
        info.set("If you aren't sure about the answer, visit the page for further information!")
        information.pack_forget()
        next_question.pack_forget()
        choice1.configure(state=NORMAL)
        choice2.configure(state=NORMAL)
        choice3.configure(state=NORMAL)
        choice4.configure(state=NORMAL)
        againa()
    frame = Frame(main)
    frame.pack(anchor=CENTER)

    again = True

    loi = StringVar()
    first = StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    v = IntVar()
    info=StringVar()
    next_question = Button(main, text='Nächste Frage', command=nexti)
    next_question.pack_forget()
    choice1 = Radiobutton(frame, textvariable=first, variable=v, value=1, command=thinking)
    choice1.pack(anchor=CENTER)
    choice2 = Radiobutton(frame, textvariable=second, variable=v, value=2, command=thinking)
    choice2.pack(anchor=CENTER)
    choice3 = Radiobutton(frame, textvariable=third, variable=v, value=3, command=thinking)
    choice3.pack(anchor=CENTER)
    choice4 = Radiobutton(frame, textvariable=fourth, variable=v, value=4, command=thinking)
    choice4.pack(anchor=CENTER)

    button = Button(main, text='Zurück zum Menü', command=end, bg='mediumspringgreen')
    button.pack(anchor=SE)

    friendly = Label(main, text='Was sind die Symptome=', bg='mediumspringgreen')
    friendly.pack(anchor=S)

    label = Label(main, textvariable=loi,  relief=RAISED )
    label.pack(anchor=N)

    punkte = IntVar()
    punkte.set(0)

    stand = Label(main, text='Punktestand', bg='deepskyblue')
    stand.pack(anchor=S)
    punktestand = Label(main, textvariable=punkte, bg='deepskyblue')
    punktestand.pack(anchor=S)


    now_more = Button(main, text='Erfahre weitere Infos!', relief=RAISED, command=visiting)
    now_more.pack(anchor=E)
    #sol = 'Ägypten'
    #solution = 'unknown'
    #website = 'google.de'
    #lists = frage_auswählen()
    #dums=find_dummies()
    #correct = Label(main, textvariable=solution, bg='mediumspringgreen')
    information = Label(main, textvariable=info, bg='crimson')
    againa()


class psychologe:
    global prefix
    prefix = "Dr: "

    def create_gui():
        PsychoGui = Tk()
        PsychoGui.title("MedBot - Psychologe")
        PsychoGui.geometry("800x800")
        canvas = Canvas(PsychoGui, width=800, height=800)
        ausgabe = tk.Text(
            PsychoGui, background='darkgrey', fg='white', cursor='xterm')
        ausgabe.config(state="disabled")
        ausgabe.grid(row=0, column=0, sticky="nsew")
        eingabe = Entry(PsychoGui)
        eingabe.config(bg="red")
        eingabe.grid(row=1, column=0, sticky="nsew")
        text = tk.Text(
            PsychoGui, background='darkgrey', fg='white', cursor='xterm')
        text.config(state="disabled")
        text.grid(row=0, column=1, sticky="nsew") 
        btn = tk.Button(
            text,
            height=1,
            width=20,
            relief=tk.FLAT,
            bg="gray99",
            fg="purple3",
            font="Dosis",
            text='Button 1')
        btn.pack(padx=10, pady=5, side=tk.TOP)

        #
        #ki
        #
        def writeinausgabe(text):
            ausgabe.config(state="normal")
            ausgabe.insert(END, text)
            ausgabe.config(state="disabled")

        def ki(eingabetext):
            skip = 0
            eingabetext = eingabetext.lower()  #macht alles zu kleinbuchstaben
            if eingabetext == "hi":
                writeinausgabe(prefix + "Servus \n")
                skip = 1

            eingabetextsplit = eingabetext.split(" ")
            check = {"wie", "geht"}
            for word in eingabetextsplit:
                if word in check:
                    writeinausgabe(
                        prefix +
                        "Gut. Aber welche Probleme hast du? \n Was soll ich machen?(Du kannst mit mir schreiben oder dir eine \n möglichkeit Links aussuchen) ”\n"
                    )
                    skip = 1
                    break

            if skip == 0:
                writeinausgabe(prefix + "Bot: Befehl nicht gefunden \n")

        def comp_s(event):
            print(eingabe.get())
            ausgabe.config(state="normal")
            eingabetxt = eingabe.get()
            eingabestr = "Du: " + eingabe.get() + "\n"
            ausgabe.insert(END, eingabestr)
            ausgabe.config(state="disabled")
            eingabe.delete(0, END)
            ki(eingabetxt)

        PsychoGui.bind('<Return>', comp_s)


class menue:
    def create_Menue():
        MenueGui = Tk()
        MenueGui.title("MedBot - Auswahl")
        MenueGui.geometry("800x800")
        MenueGui.configure(bg='paleturquoise')

        def arzt():
            MenueGui.destroy()
            ki1_gui.create_gui()

        def sani():
            MenueGui.destroy()
            create()
        def fragen__fragen():
          MenueGui.destroy()
          create_quiz()

        def exitit():
          sys.exit()


        arzt_b = Button(MenueGui, text="Arzt", command=arzt, bg='teal', fg="white")
        arzt_b.grid(row=0, column=1, sticky="nsew")
        arzt_l = Label(
            MenueGui,
            text=
            "Wenn du auf  Arzt klickst, wirst Du zu Dr. Schlau weitergeleitet. \n Du schreibst ihm dann Symptome wie Husten oder Kopfschmerzen.\n Er versucht Dir dann eine Krankheit zu finden, die Du haben könntest!", bg='cornflowerblue'
        )
        arzt_l.grid(row=1, column=0, sticky="nsew")
        sani_b = Button(MenueGui, text="Sanitäter", command=sani, bg="teal", fg="white")
        sani_b.grid(row=3, column=1, sticky="nsew")
        sani_l = Label(
            MenueGui,
            text=
            "Wenn du auf  Sani klickst, wirst Du zu dem Sanitäter Sani weitergeleitet. \n Er stellt Dir Fragen zur Ersten-Hilfe.\n Wenn Du die Fragen richtig beantwortest, kriegst Du Punkte", bg="cornflowerblue"
        )
        sani_l.grid(row=4, column=0)
        
        fragen_b = Button(MenueGui, text="Fragen", command=fragen__fragen, bg="teal", fg="white")
        fragen_b.grid(row=6, column=1, sticky="nsew")
        fragen_l = Label(MenueGui, text="Wenn du auf 'Fragen' klickst,\n kannst du im Multiple-Choice-Format die Symptome \n von verschiedenen Krankheiten lernen", bg="cornflowerblue")
        fragen_l.grid(row=7, column=0, sticky="nsew")

        exit_b = Button(MenueGui, text="Schließen", command=exitit, bg='teal', fg='white')
        exit_b.place(x=400, y=550)

        

        #fragen_b = Button(MenueGui, text='Fragen zu Krankheiten', command=create_quiz)
        #fragen_b.grid(row=1, column=1, sticky="nsew")
        MenueGui.grid_rowconfigure(2, minsize=100)
        MenueGui.grid_rowconfigure(5, minsize=100)
        MenueGui.grid_rowconfigure(8, minsize=100)
        MenueGui.grid_columnconfigure(1, minsize=340)


menue.create_Menue()
