from threading import Thread
import time

import pygame

pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((520, 520))


class Mythread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name= name
        self.runnig= True
        self.coda = []
        self.c = 1
        self.d = 1
        self.y = 30
        self.yr = 30
        
    
    def enqueue(self,elemento):
        #print(f"Inserito: {elemento}")
        self.coda.append(elemento)
        if self.c == 17:
            self.c = 1
            self.y += 130
            pygame.draw.rect(screen, green, (30*self.c,self.y,100,100),0)
        else:
            pygame.draw.rect(screen, green, (30*self.c,self.y,100,100),0)
        self.c+=4
        pygame.display.update()
        time.sleep(0.5)
        
  
    def dequeue(self):
        if len(self.coda) != 0:
            if self.d == 17:
                self.d = 1
                self.yr += 130
                pygame.draw.rect(screen, red, (30*self.d,self.yr,100,100),0)
            else:
                pygame.draw.rect(screen, red, (30*self.d,self.yr,100,100),0)
            self.d+=4
            pygame.display.update()
            time.sleep(0.5)
            return self.coda.pop(0)
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
    t1.enqueue(2)
    t1.enqueue(3)
    t1.enqueue(4)
    t1.enqueue(5)
    t1.enqueue(5)
    t1.enqueue(5)
    t1.enqueue(5)
    t1.enqueue(3)
    t1.enqueue(3)
    t1.enqueue(3)
    t1.print()
    print(t1.dequeue())
    print(t1.dequeue())
    print(t1.dequeue())
    print(t1.dequeue())
    print(t1.dequeue())
    t1.print()
    t1.stop()
    t1.join()

if __name__ == "__main__":
    main()