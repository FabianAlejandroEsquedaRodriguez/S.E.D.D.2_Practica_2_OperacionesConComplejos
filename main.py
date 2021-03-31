from numero_complejo import Numero_complejo

#Creando un objeto de la clase Numero_complejo
complejo = Numero_complejo()

operacion = input("Elige la operacion que deseas realizar (+, -, *): ")

par_real1=float(input("\n\nIngrese parte real del número 1: "))
par_imag1=float(input("\nIngrese parte imaginaria del número 1: "))
par_real2=float(input("\nIngrese parte real del número 2: "))
par_imag2=float(input("\nIngrese parte imaginaria del número 2: "))

#Menu de opciones
if operacion == '+':
    complejo.suma_complejos(par_real1, par_imag1, par_real2, par_imag2)

elif operacion == '-':
    complejo.resta_complejos(par_real1, par_imag1, par_real2, par_imag2)

elif operacion == '*':
    complejo.multiplicacion_complejos(par_real1, par_imag1, par_real2, par_imag2)