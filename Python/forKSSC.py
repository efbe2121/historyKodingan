while (True):

    a = int(input("count W-1|W: "))
    b = int(input("count W-1: "))
    c = int(input("Total Words: "))

    z = (a+1)/(b+c)
    x = (a)/(b)
    y = ((a+1)*b)/(b+c)

    print("""
    Laplace Smoothing-biagrams : %s
    Reconstituted counts       : %s
    Normal Biagram             : %s
    """%(z,x,y))
    
    del (a,b,c)