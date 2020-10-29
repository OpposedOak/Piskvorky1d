def tah(pole , pozice , znak):
    
    b = pole[:pozice]
    e = pole[pozice + 1:]
    pole = b + znak + e
    return pole
