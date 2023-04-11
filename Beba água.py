import time
from win11toast import toast

def Definição():
    Hora = int(input("Quantas horas de intervalo: "))
    Minutos = int(input("Quantos minutos de intervalo: "))
    Segundos = int(input("Quantos segundos de intervalo: "))
    time_interval = Segundos+(Minutos*60)+(Hora*3600)
    return time_interval

def Notificação():
    toast("BEBA ÁGUA", "Está na hora de beber água", icon="https://cdn-icons-png.flaticon.com/128/1079/1079119.png", audio='ms-winsoundevent:Notification.Looping.Alarm',
          buttons=["OK"])

def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        Notificação()

if __name__ == '__main__':
    time_interval = Definição()
    starttime(time_interval)
