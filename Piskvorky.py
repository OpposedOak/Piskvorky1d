def vyhodnot(pole):
    
    if "xxx" in pole:
        return "x"
        
    elif "ooo" in pole:
        return "o"
    
    elif "-" not in pole:
        return"!"
    else:
        return "-"        

def tah(pole , pozice , znak):
    
    b = pole[:pozice]
    e = pole[pozice + 1:]
    pole = b + znak + e
    return pole

def tah_hrace(pole):
    
    while True:
        pozice = int(input("Kam chceš hrát 0 - 19: "))
        
        if (pozice >= 0) and (pozice <=20) and (pole[pozice] == "-"):
            
            return tah(pole , pozice , "x")
        
        else:
            print("Zadej pole 0 - 19")

def tah_pocitace(pole):
    import random as rd
    
    while True:
        
        pozice = rd.randrange(0,20,1)
    
        if pole[pozice] != "x" or pole[pozice] != "o":
            return tah(pole, pozice, "o")
        else:
            continue

def piskvorky():

    pole = "-" * 20
    while True:
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != '-':
            break
    
    print(pole)
    if vyhodnot(pole) == '!':
        print('Remíza')
    elif vyhodnot(pole) == 'x':
        print('Výhra')
    elif vyhodnot(pole) == 'o':
        print('Prohra')

        
piskvorky()

