from collections import Counter
class ordenadorDeNumeros:
    #Declacion de propiedades de clase
    num=0
    
    #Declaracion del constructor
    def __init__(self,n):
        self.num=n
    
    #Declaracion de metodos de clase
    
    def ordenarNumeros(self):
        tamaño=range(1,self.num+1)
        lista=[]
        numerosPares=[]
        numerosImpares=[]
        
        for i in tamaño:
            num=int(input("Ingresa el numero en la posicion {} : ".format(i)))
            lista.append(num)
        lista.sort()
         
        for n in lista:
            if n%2 ==0 :
                numerosPares.append(n)
            else:
                numerosImpares.append(n)
        
        numerosRepetidos=Counter(lista)
                
        print("La lista ordenada es : {} ".format(lista))
        print("Los numeros pares son : {} ".format(numerosPares))
        print("Los numeros Impares son : {} ".format(numerosImpares))
        
        for nm,repet in numerosRepetidos.items():
            print("El numeto {} se repite {} veces".format(nm,repet))
        
        
def main():
    num=int(input("Ingresa la cantidad de numeros a capturar: "))
    obj=ordenadorDeNumeros(num)
    obj.ordenarNumeros()
    

if __name__=="__main__":
    main()
        