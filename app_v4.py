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

# Tabla de productos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)
    origen = db.Column(db.String(40))

    def __init__(self, nombre, descripcion, precio, origen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.origen = origen

    def to_dict(self):
        diccionario = {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'origen': self.origen
            }
        return diccionario

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
    items = ['nombre', 'descripcion', 'precio', 'origen']
    for item in items:
        if item not in campos:
            return True
    return False

def error_400():
    response = jsonify({'error': 'faltan campos en la peticion'})
    response.status_code = 400
    return response

# POST: introducimos un nuevo elemento
@app.route("/productos/", methods=["POST"])
def add_product():
    if request_incompleta(request):
        return error_400()

    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    precio = request.json['precio']
    origen = request.json['origen']

    nuevo_producto = Producto(nombre, descripcion, precio, origen)

    db.session.add(nuevo_producto)
    db.session.commit()

    cabeceras = {'Location': url_for('get_product', id = nuevo_producto.id)}
    return {'estado': 'Recurso creado correctamente'}, 201, cabeceras

# GET: consultamos elementos
@app.route("/productos/", methods=["GET"])
def get_products():
    todos_los_productos = Producto.query.all()
    return jsonify({'productos': [prod.to_dict() 
                                  for prod in todos_los_productos]})

# GET: consultamos un elemento concreto
@app.route("/productos/<int:id>", methods=["GET"])
def get_product(id):
    prod = Producto.query.get_or_404(id)
    return jsonify(prod.to_dict())

# PUT: modificamos un elemento
@app.route("/productos/<int:id>", methods=["PUT"])
def update_product(id):
    if request_incompleta(request):
        return error_400()
    
    prod = Producto.query.get_or_404(id)

    prod.nombre = request.json['nombre']
    prod.descripcion = request.json['descripcion']
    prod.precio = request.json['precio']
    prod.origen = request.json['origen']  
    
    db.session.commit()
        
    return jsonify(prod.to_dict())

# DELETE: borramos un elemento
@app.route("/productos/<int:id>", methods=["DELETE"])
def delete_product(id):
    prod = Producto.query.get_or_404(id)
    db.session.delete(prod)
    db.session.commit()

    return jsonify(prod.to_dict())

# hilo principal donde se ejecuta la app
if __name__=='__main__':
    app.run(debug=True)
