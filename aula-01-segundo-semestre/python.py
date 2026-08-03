import pyautogui as pa
import time as ti

decisao = input("Qual aplicativo você deseja abrir? (1 - Visual Studio Code, 2 - Brave, 3 - Microsoft Teams: ")

lista_apps = ["Visual Studio Code", "Brave", "Microsoft Teams"]

def abrir_app(app):
    pa.press("win")
    ti.sleep(0.5)
    pa.write(app)
    ti.sleep(0.5)
    pa.press("enter")

abrir_app(lista_apps[int(decisao) - 1])


#colab.research.google.com/drive/