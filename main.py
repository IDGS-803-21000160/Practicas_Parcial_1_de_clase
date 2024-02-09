from flask import Flask, render_template,request
import math
import formdistance
import formResistencia


app=Flask(__name__)

@app.route("/")
def index():
    escuela="UTL!!!"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos")
def alum():
    return render_template("alumnos.html")

@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def saludo():
    return "<p><h1>Hola desde la funcion saludar<br> Y hola mundo</h1></p>"

''' http://127.0.0.1:5000/user/jose '''
@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola "+name


@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID {} Nombre {}".format(id,name)

#http://127.0.0.1:5000/suma/5.0/8.0
@app.route("/suma/<float:n1>/<float:n2>")
def funcSumar (n1,n2):
    return "El valor de {} + {} = {}".format(n1,n2,n1+n2)
    
@app.route("/default")
@app.route("/default/<string:ab>")
def fun(ab="UTL"):
    return "Hola " + ab

@app.route("/multiplicar",methods=["GET","POST"])
def multiplicar():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1>La multiplicación es: {} </h1>".format(str(int(num1)*int(num2)))
    else:
        return'''
        <form action="/multiplicar" method="POST">
            <label>N1:</labes>
            <input type="text" name="n1"/><br>
            <label>N2:</labes>
            <input type="text" name="n2"/><br>
            <input type="submit"/>
        </form>
        '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/opciones",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        if request.form.get('sum'):
            return "<h1>La Suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif request.form.get('res'):
            return "<h1>La Resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif request.form.get('mul'):
            return "<h1>La Multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        else:
            return "<h1>La Division es: {} </h1>".format(str(int(num1)/int(num2)))

@app.route("/formCinepolis")
def form():
    return render_template("formularioCinepolis.html")



@app.route("/munuProces", methods=["POST"])
def calc():
    if request.method == "POST":
        boletos = int(request.form.get("cantidadBoletos"))
        compradores=int(request.form.get('cantidadCompradores'))
        mensaje=""
        
        if request.form.get('si'):
            if (boletos > (5*compradores)) & (boletos <=(7*compradores)):
                costo= float(boletos * 12)
                descuento=float(costo * 0.15)
                desTar=((costo-descuento))
                totalTar=float(desTar * 0.10)
                total=(desTar-totalTar)
                
            elif boletos <=(5*compradores) & boletos >=2:
                costo= float(boletos * 12)
                descuento=float(costo * 0.10)
                desTar=((costo-descuento))
                totalTar=float(desTar * 0.10)
                total=(desTar-totalTar)
            elif boletos==1:
                total=12
            else:
                total=0
                mensaje="No puedes comprar esa cantidad de boletos"
        elif request.form.get('no'):
            if (boletos > (5*compradores)) & (boletos <=(7*compradores)):
                costo= float(boletos * 12)
                descuento=float(costo * 0.10)
                total=float(costo-descuento)
            elif boletos <=(5*compradores) & boletos >=2:
                costo = float(boletos * 12)
                descuento=float(costo * 0.10)
                total=float(costo-descuento)
            elif boletos==1:
                total=12
            else:
                total=0
                mensaje="No puedes comprar esa cantidad de boletos"

        return render_template("formularioCinepolis.html",total=total,mensaje=mensaje)

@app.route("/formCalDistancia",methods=["GET","POST"])
def calcularDistancia():
    distance_form=formdistance.DistanceForm(request.form)
    resultado=0
    if request.method=='POST':
        valx1=float(distance_form.valorx1.data)
        valx2=float(distance_form.valorx2.data)
        valy1=float(distance_form.valory1.data)
        valy2=float(distance_form.valory2.data)
        
        print("Valor X1 : {} ".format(valx1)) 
        print("Valor X2 : {} ".format(valx2))        
        print("Valor Y1  : {} ".format(valy1)) 
        print("Valor Y2  : {} ".format(valy2)) 
        

        primerPar=math.pow(((valx2)-(valx1)),2)
        segundoPar=math.pow(((valy2)-(valy1)),2)
        
        resultado=math.sqrt((primerPar)+(segundoPar))
        
        print("Resultado: { } ",format((resultado)))
    
    return render_template("distacia.html",form=distance_form,resultado=resultado)

def colors(colors):
    switcher={
        0:'black',
        1:'burlywood',
        2:'red',
        3:'orange',
        4:'yellow',
        5:'green',
        6:'blue',
        7:'plum',
        8:'gray',
        9:'white'
    }
    return switcher.get(colors,'default')

def colorsTol(color):
    switcher={
        1:'black',
        10:'burlywood',
        100:'red',
        1000:'orange',
        10000:'yellow',
        100000:'green',
        1000000:'blue',
        10000000:'plum',
        100000000:'gray',
        1000000000:'white'
    }
    return switcher.get(color,'default')

@app.route("/formResistencias", methods=["GET", "POST"])
def calcularVol():
    text = ''
    texttwo = ''
    textthree = ''
    tolerancia = ''
    valMin = 0
    valMax = 0
    valor = 0

    resistencia_form = formResistencia.ResistenciaForm(request.form)
    
    if request.method == 'POST':
        if request.form.get('btn1') == 'registrar':
            colorOne = float(resistencia_form.colores1.data)
            colorTwo = float(resistencia_form.colores2.data)
            colorThree = resistencia_form.colores3.data
            options = int(resistencia_form.options.data)

            text = colors(colorOne)
            texttwo = colors(colorTwo)
            textthree = colorsTol(float(colorThree))

            dupColors = str(int(colorOne)) + str(int(colorTwo))
            valor = float(dupColors) * float(colorThree)

            if options == 5:
                tolerancia = 'Dorado 5%'
                porcentajefive = 0.05 * valor
                valMax = valor + porcentajefive
                valMin = valor - porcentajefive
            elif options == 10:
                tolerancia = 'Plata 10%'
                porcentajeTen = 0.10 * valor
                valMax = valor + porcentajeTen
                valMin = valor - porcentajeTen
        
        elif request.form.get('btn2') == 'limpiar':
            resistencia_form.colores1.data = ''
            resistencia_form.colores2.data = ''
            resistencia_form.colores3.data = ''
            resistencia_form.options.data = ''

            text = ''
            texttwo = ''
            textthree = ''
            tolerancia = ''
            valMin = 0
            valMax = 0
            valor = 0

    return render_template("formResistenca.html", form=resistencia_form, text=text, texttwo=texttwo, textthree=textthree, tolerancia=tolerancia, valMin=valMin, valMax=valMax, valor=valor)

'''
Aqui colocamos el motodo que iniciara la App
'''
if __name__=="__main__":
    app.run(debug=True)