from flask import Flask, request, jsonify, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from os import remove

try:
    remove('database.db') # solo para la practica. Normalmente no queremos borrar la base de datos.
except FileNotFoundError:
    pass

# Inicializamos app
app = Flask(__name__)

# Inicializamos base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# # Tabla de productos
# class Human(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100), unique=True)
#     descripcion = db.Column(db.String(200))
#     precio = db.Column(db.Float)
#     origen = db.Column(db.String(40))
#
#     def __init__(self, nombre, descripcion, precio, origen):
#         self.nombre = nombre
#         self.descripcion = descripcion
#         self.precio = precio
#         self.origen = origen
#
#     def to_dict(self):
#         diccionario = {
#             'id': self.id,
#             'nombre': self.nombre,
#             'descripcion': self.descripcion,
#             'precio': self.precio,
#             'origen': self.origen
#             }
#         return diccionario
class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    height = db.Column(db.Float)
    age = db.Column(db.Integer)

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def to_dict(self):
        diccionario = {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'height': self.height,
            }
        return diccionario

with app.app_context():
    db.create_all()

# error de producto no encontrado
def error_404(e):
    response = make_response({'error': 'recurso no encontrado'})
    response.status_code = 404
    return response

#registramos error de id no encontrado
app.register_error_handler(404, error_404)

# error de petición incompleta
def request_incompleta(req):
    campos = list(req.json.keys())
    items = ['name', 'age', 'height']
    for item in items:
        if item not in campos:
            return True
    return False

def error_400():
    response = make_response({'error': 'faltan campos en la peticion'})
    response.status_code = 400
    return response

# POST: introducimos un nuevo elemento
@app.route("/productos/", methods=["POST"])
def add_product():
    if request_incompleta(request):
        return error_400()
    print("poszlo")
    name = request.json['name']
    age = request.json['age']
    height = request.json['height']
    print("asdfasdf", height)
    nuevo_producto = Human(name, height, age)

    db.session.add(nuevo_producto)
    db.session.commit()

    cabeceras = {'Location': url_for('get_product', id = nuevo_producto.id)}
    return {'estado': 'Recurso creado correctamente'}, 201, cabeceras

# GET: consultamos elementos
@app.route("/productos/", methods=["GET"])
def get_products():
    if request.args:
        args = request.args
        lista_productos = []
        for item, valor in args.items():
            if item == 'name':
                productos = Human.query.filter_by(name = valor)
            elif item == 'height':
                productos = Human.query.filter_by(height = valor)
            elif item == 'age':
                productos = Human.query.filter_by(age = valor)
            else:
                return error_400()
            lista_productos.extend(productos)
        if len(lista_productos)>0:
            return jsonify({'resultado': [prod.to_dict() 
                                          for prod in lista_productos]})
        else:
            return jsonify({'resultado': 'no hay productos coincidentes'})

    todos_los_productos = Human.query.all()
    return jsonify({ 'productos': [prod.to_dict() 
                                   for prod in todos_los_productos]})

# GET: consultamos un elemento concreto
@app.route("/productos/<int:id>", methods=["GET"])
def get_product(id):
    prod = Human.query.get_or_404(id)
    return jsonify(prod.to_dict())

# PUT: modificamos un elemento
@app.route("/productos/<int:id>", methods=["PUT"])
def update_product(id):
    if request_incompleta(request):
        return error_400()
    
    prod = Human.query.get_or_404(id)

    prod.nombre = request.json['nombre']
    prod.descripcion = request.json['descripcion']
    prod.precio = request.json['precio']
    prod.origen = request.json['origen']  
    
    db.session.commit()
        
    return jsonify(prod.to_dict())

# DELETE: borramos un elemento
@app.route("/productos/<int:id>", methods=["DELETE"])
def delete_product(id):
    prod = Human.query.get_or_404(id)
    db.session.delete(prod)
    db.session.commit()

    return jsonify(prod.to_dict())

# hilo principal donde se ejecuta la app
if __name__=='__main__':
    app.run(debug=True)
