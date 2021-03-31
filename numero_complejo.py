#Clase para las operaciones con numeros complejos

class Numero_complejo:
    #Metodo constructor
    def __init__Numero_complejo(self, real_1, imaginaria_1, real_2, imaginaria_2):
        self.__real1 = real_1
        self.__real2 = real_2
        self.__imaginaria1 = imaginaria_1
        self.__imaginaria2 = imaginaria_2

    #Metodos para cada operacion

    #Suma
    def suma_complejos(self, real1, imaginaria1, real2, imaginaria2):
        par_real = real1 + real2
        par_imag = imaginaria1 + imaginaria2

        print("\n\nEl resultado es: {:.2f} + {:.2f}i".format(par_real, par_imag))

    #Resta
    def resta_complejos(self, real1, imaginaria1, real2, imaginaria2):
        par_real = real1 - real2
        par_imag = imaginaria1 - imaginaria2

        print("\n\nEl resultado es: {:.2f} - {:.2f}i".format(par_real, par_imag))
    
    #Multiplicación
    def multiplicacion_complejos(self, real1, imaginaria1, real2, imaginaria2):
        par_real = real1 * real2 - imaginaria1 * imaginaria2
        par_imag = real1 * imaginaria2 + imaginaria1 * real2

        print("\n\nEl resultado es: {:.2f} * {:.2f}i".format(par_real, par_imag))