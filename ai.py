import util

def tah_pocitace(pole,symbol_pocitace):
    import random as rd
    
    while True:
        
        pozice = rd.randrange(0,20,1)
        
        if pole[pozice] != "o" or pole[pozice] != "x":
            return util.tah(pole, pozice, symbol_pocitace)

        else:
            continue
