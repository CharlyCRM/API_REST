from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return products


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"productos": products, 
                    "mensage": "Lista Productos"})


############
# API GET #
###########

'''@app.route('/products/<string:product_nombre>'): Define una ruta "/products/string:product_nombre" que responde a las solicitudes GET. 
La parte "string:product_nombre" indica que se espera un parámetro en la URL llamado "product_nombre", que debe ser una cadena. 
Cuando se accede a esta ruta, se llama a la función "getProduct(product_nombre)" y se pasa el valor del parámetro "product_nombre".'''
@app.route('/products/<string:product_nombre>')
def getProduct(product_nombre):
    # Reccore la lista products. Si dentro de product['nombre'] localiza alguno que coincida con el valor pasado desde el servidor, lo retorna.
    productsFound = [product for product in products if product['nombre'] == product_nombre]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"mensage": "Producto no Encontrado"})

# Misma función pero usando solo un bucle for. Sin usar una compresión de lista:

# @app.route('/products/<string:product_nombre>')
# def getProduct(product_nombre):
#     productsFound = []
#     for product in products:
#         if product['nombre'] == product_nombre:
#             productsFound.append(product)
    
#     if len(productsFound) > 0:
#         return jsonify({"product": productsFound[0]})
    
#     return jsonify({"mensaje": "Producto no Encontrado"})

############
# API POST #
############

# No hay problema al usar la misma ruta
@app.route('/products', methods=['POST'])
def addProducts():
    # request recibe las peticiones enviadas desde el servidor con el método POST
    new_product = {
        'nombre': request.json['nombre'],
        'precio': request.json ['precio'],
        'cantidad': request.json['cantidad']
    }
    # Añade el nuevo producto a la lista de productos defina en products.py
    products.append(new_product)
    return jsonify({'mensage': 'Producto añadido correctamente',
                    'productos': products})


###########
# API PUT #
###########

@app.route('/products/<string:product_nombre>', methods=['PUT'])
def editProduct(product_nombre):
    productFound = [product for product in products if product['nombre'] == product_nombre]
    # Si encuentra el producto, modifica sus 3 propiedades
    if (len(productFound)) > 0:
        productFound[0]['nombre'] = request.json['nombre']
        productFound[0]['precio'] = request.json['precio']
        productFound[0]['cantidad'] = request.json['cantidad']
        
        return jsonify({'mensage': 'Producto Actualizado',
                        'producto': productFound[0]
                        })
    
    return jsonify({'mensage': 'Producto no Encontrado'})

##############
# API DELETE #
##############

@app.route('/products/<string:product_nombre>', methods=['DELETE'])
def deleteProduct(product_nombre):
    productFound = [product for product in products if product['nombre'] == product_nombre]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({
            'mensage': 'Producto Eliminado',
            'productos': products})
    return jsonify({'mensage': 'Producto no Encontrado'})

if __name__ == "__main__":
    app.run(debug=True)


# GET = Método por defeto
# POST = Se usa para guardar datos
# PUT = Se usa para actualizar datos
# DELETE = Se usa para eliminar datos