from flask import Flask, request, jsonify, url_for
products = {1: {'nombre': 'tomate'}}
counter = 1
# Inicializamos app
app = Flask(__name__)
# POST: introducimos un nuevo elemento
@app.route("/productos/", methods=["POST"])
def add_product():
    global counter
    counter += 1
    posted_data = request.get_json()
    products[counter] = posted_data
    cabeceras = {'Location': url_for('get_products')+str(counter) }
    return {'estado': 'Recurso creado correctamente'}, 201, cabeceras

# GET: consultamos elementos
@app.route("/productos/", methods=["GET"])
def get_products():
    return jsonify(products)
    # hilo principal donde se ejecuta la app

# GET: we consult a specific element
@app.route("/productos/<int:id>", methods=["GET"])
def get_product(id):
    if id not in products.keys():
        return {'error': 'product not found'}, 404
    product = products[id]
    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)


