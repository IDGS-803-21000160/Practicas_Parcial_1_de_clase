class piramide:
    #Declacion de propiedades de clase
    num=0
    
    #Declaracion del constructor
    def __init__(self,n):
        self.num=n
    
    #Declaracion de metodos de clase
    
    def generarPiramide(self):
        tamaño=range(1,self.num+1)
        for i in tamaño:
            print("*" * i)

def main():
    obj=piramide(9)
    obj.generarPiramide()
    

if __name__=="__main__":
    main()
        