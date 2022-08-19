from multiprocessing.resource_sharer import stop
from threading import Thread
import time

class Mythread(Thread):
    def __init__(self,name,numero,numero_Utente):
        Thread.__init__(self)
        self.name= name
        self.numero = numero
        self.numero_Utente=numero_Utente
        self.runnig= True
    def run(self):
        while self.runnig:
            print(f"{self.name}: {self.numero}")
            self.numero += 2
            if self.numero_Utente <= self.numero:
                self.stop()
            time.sleep(1)
    def stop(self):
        self.runnig = False
          
def main():
    numero_Utente = int(input("Inserisci un numero: "))
    t1 = Mythread("PARI",0,numero_Utente)
    t1.start()
    t2 = Mythread("DISPARI",1,numero_Utente)
    t2.start()
if __name__=="__main__":
    main()