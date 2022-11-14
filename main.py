

import string
import sqlite3
from art import text2art
from hashlib import *
from getpass import getpass
from hashlib import sha256
print("welcom to my project")
conn=sqlite3.connect('Etudiant.db')
c=conn.cursor()
#activer les foreign_keys
#Création de deux tables

c.execute("PRAGMA foreign_keys=on")

c.execute(""" create table if not exists T_Etablissement(id_Etab integer  primary key autoincrement ,Libelle_Etab varchar(20), Adresse varchar(20)) """)

c.execute("""insert into T_Etablissement (Libelle_Etab, Adresse ) values ("universite centale", "12 rue Monplaisir")""")
c.execute("""insert into T_Etablissement (Libelle_Etab, Adresse ) values ("Esprit", "12 rue Nasr")""")
c.execute("""insert into T_Etablissement (Libelle_Etab, Adresse ) values ("Sesam", "12 rue lafayet")""")


c.execute(""" create table if not exists T_Etudiant(N_carte integer primary key autoincrement ,Nom varchar(20),Prenom varchar(20), email varchar(20), pwd varchar(30),id_Etablissement integer ,FOREIGN KEY(id_Etablissement) REFERENCES T_Etablissement(id_Etab)) """)


c.execute("""insert into T_Etudiant (Nom, Prenom, email, pwd ) values ('wertateni', 'fadwa','fadwawartat@gmail.com','ggggFFFF12547-*/')""")
c.execute("""insert into T_Etudiant (Nom, Prenom, email, pwd ) values ('BenAli', 'Asma', 'asmabenali@gmail.com', 'ghahduuJHGHGFF2546+-*')""")
c.execute("""insert into T_Etudiant (Nom, Prenom, email, pwd ) values ('Ali', 'Mohamed', 'mouhamedali@gmail.com', 'ghdfshsGG256//*')""")


conn.commit()
c.execute("""select * from  T_Etablissement""")







#check Email


import  re

"""
user_email="^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
def chek_email(email) :
    if (re.search(user_email,email)) :
        print(f"{email} correct ")
    else :
        print(f"{email} incorrect")
"""

def register():
    trouver=False
    user_email = "^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
    nom = input("Donner votre nom")
    #nom=nom.upper()
    prenom = input("Donner votre prenom")
    #prenom=string.capwords(prenom)
    # test mail
    while True:
        try:
         email = input("donnez votre email\n"+Fore.RED +" (exp:exemle.exemle@gmail.com):\n"+Style.RESET_ALL)
         if (re.search(user_email, email)):

            break

         else:
             print("Merci d'introduire un email valide ")
        except ValueError:
            print("Merci d'introduire un email valide ")
    c.execute("select id_Etab from T_Etablissement")
    itemes = c.fetchone()








    # test password


    while True:
        depno = int(input("Donner votre numero de dep"))
        if (depno in itemes):
            break

        else:
            print(Fore.RED + "le departement n'existe pas" + Style.RESET_ALL)

    user_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    while True:
        try:
            password = pyautogui.password(
                "Entrer votre mot de passe \n(exp:_qui contient alphabet miniscule et majuscule\n_contient les caractere speciaux :@#$%^&+=]\n_contient au moin un numero\n ")
            result = re.findall(user_password, password)
            if (result):
                break
            else:
                print("Merci d'introduire un mot de passe valide ")
        except ValueError:
            print("Merci d'introduire un mot de passe valide ")

    c.execute(""" insert into T_Etudiant(Nom,Prenom,email,pwd,id_Etablissement) values(?,?,?,?,?) """,
              (nom.upper(), string.capwords(prenom), email, hashlib.sha256(password.encode()).hexdigest(), depno))
    conn.commit()





def login():
        email=input("Donner votre email")
        password = pyautogui.password("Entrer votre mot de passe  ")
        c.execute("""select * from T_Etudiant where email=? and pwd=?""",(email, hashlib.sha256(password.encode()).hexdigest()))
        if(c.fetchone()==None):
         print('données incrorect ressaiyez ')
         login
        else:
         print(Fore.LIGHTCYAN_EX+(text2art("Welcome To your session"))+Style.RESET_ALL)


def ex1(d, reverse=False):
    print("Original dictionary elements:")
    colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
    print(colors)
    print("\nSort (ascending) the said dictionary elements by value:")
    print(ex1(colors))
    print("\nSort (descending) the said dictionary elements by value:")
    print(ex1(colors, True))
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


# ex2
def ex2():
    d = {0: 10, 1: 20}
    print(d)
    d.update({2: 30})
    print(d)


# ex 3
def ex3():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic4 = {}
    for d in (dic1, dic2, dic3): dic4.update(d)
    print(dic4)


# ex4
def ex4():
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    def is_key_present(x):
        if x in d:
            print('Key is present in the dictionary')
        else:
            print('Key is not present in the dictionary')

    is_key_present(5)
    is_key_present(9)


# ex5
def ex5():
    d = {'x': 10, 'y': 20, 'z': 30}
    for dict_key, dict_value in d.items():
        print(dict_key, '->', dict_value)


# ex6

def ex6():
    d = dict()
    for x in range(1, 16):
        d[x] = x ** 2
    print(d)


# ex7
def ex7():
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(myDict)
    if 'a' in myDict:
        del myDict['a']
    print(myDict)


# ex8
def ex8():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    color_dictionary = dict(zip(keys, values))
    print(color_dictionary)


# ex9
def ex9():
    color_dict = {'red': '#FF0000',
                  'green': '#008000',
                  'black': '#000000',
                  'white': '#FFFFFF'}

    for key in sorted(color_dict):
        print("%s: %s" % (key, color_dict[key]))


# ex10

# ex11
def ex11():
    student_data = {'id1':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['English, math, science']
                         },
                    'id2':
                        {'name': ['David'],
                         'class': ['V'],
                         'subject_integration': ['English, math, science']
                         },
                    'id3':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['English, math, science']
                         }
                    }

    result = {}

    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value

    print(result)


choises = {
    1: "ex1",
    2: "ex2",
    3: "ex3",
    4: "ex4",
    5: "ex5",
    6: "ex6",
    7: "ex7",
    8: "ex8",
    9: "ex9",
    10: "ex10",
    11: "ex11"}
print(choises)

x = int(input("Donner votre num"))

match x:
    case 1:
        ex1()

    case 2:
        ex2()

    case 3:
        ex3()

    case 4:
        ex4()

    case 5:
        ex5()

    case 6:
        ex6()

    case 7:
        ex7()

    case 8:
        ex8()

    case 9:
        ex9()

    case 11:
        ex11()



