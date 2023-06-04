from flask import Flask, render_template
from pymongo import MongoClient
from bson.json_util import dumps
import json

# Configuración de Flask
app = Flask(__name__)

# Configuración de MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['proyectoBlogNoticias']  

@app.route('/')
def index():
    # Consulta a la base de datos
    collection = db['Users']  
    #result = collection.find_one()
    result = collection.find_one({"Name":"cesar"},{"Name":1, "_id":0})

    if result:
        return render_template("index.html")
    else:
        return " No se encontraron resultados en la consulta."    


@app.route('/usuarios.html')
def usuarios(): 
    collection = db['Users']  
    #consulta para buscar por usuario
    result = collection.find_one({"Name":"cesar"},{"Name":1, "_id":0})
    #Consulta contar codigo postal igual
    cp = collection.find_one({"Name":"cesar"}, {"CP":1,"_id":0})
    #Consultar username
    usr = collection.find_one({"userName":"cesarjabmx"},{"userName":1,"_id":0})
    #consultar twitte
    tw = collection.find_one({"Account":"cesarjabmx"},{"Account":1,"_id":0})
    #Consultar telefono(s)
    tel = collection.find_one({"phone":"2382073493"},{"phone":1,"_id":0})
    #consultar Descripcion
    desc = collection.find_one({"Desciption":"Estudiante ISC"},{"Desciption":1,"_id":0})
    #consultar calle
    call = collection.find_one({"Address":"calle 8 sur"},{"Address":1,"_id":0})
    #consultar ciudad
    city = collection.find_one({"City":"Tehuacan"},{"City":1,"_id":0})
    #consultar pais
    pais = collection.find_one({"Country": "Mexico"},{"Country":1,"_id":0})

    #Consulta para saber cuantos usuarios son de Mexico
    contar = collection.count_documents({"Country": "Mexico"})
    usrmx= collection.find({"Country": "Mexico"})

    #for doc in usrmx:
    #    print (doc)

    #consultar todos los registros
    todos = collection.find({})
    vectorconsul = []

    #print (type(pruebacon))
    for all in todos:
        cadenacol = dumps(todos)
        pruebacon = cadenacol
        #vectorconsul = all 
        #print (cadenacol)

        #Agregarmos una variable a cada campo 
        nombreusr = all["Name"]
        vectorconsul.append(nombreusr)
        #print(nombreusr)

        
        usuarioo = all["userName"]
        vectorconsul.append(usuarioo)
        #print(vectorconsul[1])        


    print (cadenacol[0])    
    print (cadenacol[-1]) 
    print (type(cadenacol))
    convertir = cadenacol[1:-1]
    #print(convertir)
    print (type(convertir))
    nuevo = json.loads(cadenacol)
    print(type(nuevo))

    #Consulta codigo postal similar 
    cps = collection.count_documents({"CP": "75768"})   

    return render_template ("usuarios.html", content=result, codigo=cp, userna=usr, twit=tw
    , cel=tel, des=desc, calle=call, ciudad=city, countt=pais, cantidad=contar, Usuarios=usrmx
    , cantidadcp=cps, vectorenvio=vectorconsul, consulta=nuevo)    

@app.route('/noticias.html')
def noticias():
    collection = db['News']  
    #consulta noticias sin tag
    #db.News.find({"Tags":[]},{"userName":1});
    ntag = collection.find({"Tags":[]},{"Name":1, "_id":0})
    #db.News.find({"Tags":[]},{"Title":1});
    nombrenot = collection.find_one({"Title":"Contingencia Ambiental"},{"Title":1,"_id":0})
    descnot = collection.find_one({"Tags":[]},{"Description":1,"_id":0})
    fecha = collection.find_one({"Title":"Contingencia Ambiental"},{"Date":1,"_id":0})
    tags = collection.find_one({"Tags":[]},{"Tags":1,"_id":0})


    return render_template("noticias.html", noticia1=nombrenot, Descripcion=descnot, fec=fecha , tag=tags)       

@app.route('/comentarios.html')
def comentarios():
    
    #Mostrar los datos de los comentarios que realizaron a cierta noticia.

    # Consultas de noticias publicadas por usuarios.:
    #3 últimas noticias publicadas ordenadas por fecha(de más reciente a más antigua)
    
    # Número de comentarios por noticia, por día o por usuario.

    return render_template("comentarios.html")      

if __name__ == '__main__':
    app.run(debug=True)
