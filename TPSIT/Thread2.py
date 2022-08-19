from threading import Thread
import time


class Mythread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name= name
        self.runnig= True
        self.coda = []
    
    def enqueue(self,elemento):
        print(f"Inserisco: {elemento}")
        self.coda.append(elemento)
        
  
    def dequeue(self):
        if len(self.coda) != 0:
            return print(f"Eliminato: {self.coda.pop(0)}")
        else:
            return None

    def run(self):
        while self.runnig:
            pass

    def stop(self):
        self.runnig = False
    
    def print(self):
        print(self.coda)

def main():

    t1 = Mythread("CODA: ")
    t1.start()
    t1.enqueue(5)
    t1.print()
    t1.enqueue(6)
    t1.print()
    t1.enqueue(7)
    t1.print()
    t1.dequeue()
    t1.print()
    t1.dequeue()
    t1.print()
    t1.stop()
    t1.join()




if __name__ == "__main__":
    main()