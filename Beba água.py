import time
from win10toast import ToastNotifier
import datetime

def Definição():
    Hora = int(input("Quantas horas de intervalo: "))
    Minutos = int(input("Quantos minutos de intervalo: "))
    Segundos = int(input("Quantos segundos de intervalo: "))
    time_interval = Segundos+(Minutos*60)+(Hora*3600)
    return time_interval

def Anotação():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"Você bebeu água {now} \n")

def Notificação():
    notificação = ToastNotifier()
    notificação.show_toast("Hora de beber água")
    Anotação()

def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        Notificação()

if __name__ == '__main__':
    time_interval = Definição()
    starttime(time_interval)
