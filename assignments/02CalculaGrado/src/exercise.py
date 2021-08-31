
def calcula_grado(x):
    if 0.0<=x and x<=1.0:
        if x>0.9:
            nota=str('A')
        elif x>0.8:
           nota=str('B')
        elif x>0.7:
            nota=str('C')
        elif x>0.6:
            nota=str('D')
        else:
            nota=str('F')
    else:
       nota=str('score incorrecto')
    return nota 

def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))   

if __name__=='__main__':
    main()
