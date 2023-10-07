from flask import Flask, request, jsonify, url_for, make_response

productos = {1: {'nombre': 'tomate'},
             2: {'nombre':'lechuga'}}

counter = 2

# Inicializamos app
app = Flask(__name__)

# Comprobar si existe el productoC
def id_not_in_db(id):
    if id not in productos.keys():
        return True
    return False

def error_404():
    response = make_response({'error': 'producto no encontrado'})
    response.status_code = 404
    return response

# POST: introducimos un nuevo elemento
@app.route("/productos/", methods=["POST"])
def add_product():
    global counter
    counter += 1
    posted_data = request.get_json()
    productos[counter] = posted_data
    cabeceras = {'Location': url_for('get_product', id=counter) }
    return {'estado': 'Recurso creado correctamente'}, 201, cabeceras   

# GET: consultamos elementos
@app.route("/productos/", methods=["GET"])
def get_products():
    return jsonify(productos)

# GET: consultamos un elemento concreto
@app.route("/productos/<int:id>", methods=["GET"])
def get_product(id):
    if id_not_in_db(id):
        return error_404()
    producto = productos[id]
    return jsonify(producto)

# PUT: modificamos un elemento
@app.route("/productos/<int:id>", methods=["PUT"])
def update_product(id):
    if id_not_in_db(id):
        return error_404()
    productos[id] = request.get_json()    
    return jsonify(productos[id])

# DELETE: borramos un elemento
@app.route("/productos/<int:id>", methods=["DELETE"])
def delete_product(id):
    if id_not_in_db(id):
        return error_404()
    producto_eliminado = productos.pop(id)
    return jsonify(producto_eliminado)

# hilo principal donde se ejecuta la app
if __name__=='__main__':
    app.run(debug=True)
