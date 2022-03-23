import pickle
import os
class car:
    def __init__(self,make,model,rental):
        self.mk=make
        self.ml=model
        self.rl=rental
    def showme(self):
        print(self.mk," ",self.ml," ",self.rl)

with open('spcnotes15.dat','wb') as spc_out:
    try:
        while True:
            mk=input("Input car brand name: ")
            ml=input("Input car model name: ")
            rl=int(input("Input rate in USD per hour: "))
            c=car(mk,ml,rl)   #take a note of this step
            pickle.dump(c,spc_out,pickle.HIGHEST_PROTOCOL)
            ans=input("Wanna Cont? ")
            if ans=="n" or ans=="N":
                break
    except EOFError:
        pass
spc_out.close()
#now lets read the file
with open('spcnotes15.dat','rb') as spc_in:
    try:
        while True:
            cc=pickle.load(spc_in)
            print(cc.mk," ",cc.ml," ",cc.rl)
    except EOFError:
        pass