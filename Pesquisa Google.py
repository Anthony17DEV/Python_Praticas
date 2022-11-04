import pyautogui as pyg
from time import sleep


def pesquisar():
    texto = pyg.prompt("OQUE QUER QUE SEJA PESQUISADO ?")

    while texto == "":
        pyg.alert("ENTÃO VA PRA UMA PORRA!")
        texto = pyg.prompt("OQUE QUER QUE SEJA PESQUISADO ?")
    if texto == None:
        exit()

    pyg.press('win')
    pyg.write('Navegador', interval=0.2)
    pyg.press('Enter')
    sleep(2)
    pyg.write(texto, interval=0.2)
    pyg.press('Enter')

pesquisar()
