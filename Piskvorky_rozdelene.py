import util
import ai

def vyhodnot(pole):
    
    if "xxx" in pole:
        return "x"
        
    elif "ooo" in pole:
        return "o"
    
    elif "-" not in pole:
        return"!"
    else:
        return "-"        



def tah_hrace(pole,symbol_hrace):
    
    while True:
        pozice = int(input("Kam chceš hrát 0 - 19: "))
        
        if (pozice >= 0) and (pozice < 20) and (pole[pozice] == "-"):
            
            return util.tah(pole , pozice , symbol_hrace)
        
        else:
            print("Zadej pole 0 - 19")


def piskvorky():
        
    symbol_hrace = input("Zvol si herni symblo x/o: ")
    symbol_pocitace = "o"
    
    if symbol_hrace == "x":
        symbol_pocitace = "o"
        
    else:
       symbol_pocitace = "x"
    
        
    pole = "-" * 20
    while True:
        pole = tah_hrace(pole,symbol_hrace)
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = ai.tah_pocitace(pole,symbol_pocitace)
        if vyhodnot(pole) != '-':
            break
    
    print(pole)
    if vyhodnot(pole) == '!':
        print('Remíza')
    elif (vyhodnot(pole) == 'x' and symbol_hrace == "x") or (vyhodnot(pole) == 'o'and symbol_hrace == "o"):
        print('Výhra')

    else:
        print("Prohra")
