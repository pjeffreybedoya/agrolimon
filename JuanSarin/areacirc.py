#crear variables
area_cir=0
lado=0

print("por favor ingresar el valor de uno de los lados del trianqulo:")

#creacion de variable lado y asignacion del valor ingresado
lado=int(input())


#aplicamos la formula del modelo matematico con el valor de  la variable 'lado'
area_cir=3.14*((2*(lado**2-(lado/2)**2)**(1/2))/3)**2

print("El area de la circunferencia es de: ", area_cir)