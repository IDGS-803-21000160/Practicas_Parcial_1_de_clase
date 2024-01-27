from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/formCinepolis")
def formulario():
    return render_template("formularioCinepolis.html")



@app.route("/opciones", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)
