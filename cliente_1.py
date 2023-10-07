import requests

BASE = "http://127.0.0.1:5000/"

def muestra_productos():

    response = requests.get(BASE + "productos/")

    print('____________________')
    print('')
    print('   GET productos ')
    print('status: '+ str(response.status_code))
    print('JSON: '+ str(response.json()))


# creamos primer recurso
response = requests.post(BASE + "productos/", json = {'nombre': 'tomate', 
                                                      'origen': 'Mazarron', 
                                                      'precio': 0.7, 
                                                      'descripcion': 'tomate de pera'})

print('____________________')
print('')
print('introducimos tomate')
print('status: '+ str(response.status_code))
print('cabecera: '+ str(response.headers))
print('JSON: '+ str(response.json()))


# creamos segundo recurso
response = requests.post(BASE + "productos/", json = {'nombre': 'lechuga',
                                                      'origen': 'Torre Pacheco',
                                                      'precio': 0.8,
                                                      'descripcion': 'lechuga de ensalada'})

print('____________________')
print('')
print('introducimos lechuga')
print('status: '+ str(response.status_code))
print('cabecera: '+ str(response.headers))
print('JSON: '+ str(response.json()))

muestra_productos()

# creamos un recurso con definición incompleta --> DEBE DAR ERROR
response = requests.post(BASE + "productos/", json = {'nombre': 'acelgas',
                                                      'origen': 'Lorca',
                                                      'precio': 0.4})

print('____________________')
print('')
print('introducimos acelgas sin descripcion')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

muestra_productos()

# accedemos a recurso 1 (ojo ahora se indexa a partir de 1)
response = requests.get(BASE + "productos/1")
print('____________________')
print('')
print('   GET id = 1 ')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

# accedemos a recurso 2 
response = requests.get(BASE + "productos/2")
print('____________________')
print('')
print('    GET id = 2 ')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

# accedemos a recurso 3 --> DEBE DAR ERROR
response = requests.get(BASE + "productos/3")
print('____________________')
print('')
print('    GET id = 3 ')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

# # PUT a un recurso
# response = requests.put(BASE + "productos/2", json = {'nombre': 'melon',  
#                                                      'precio': 0.6,
#                                                      'descripcion': 'melon amarillo',
#                                                      'origen': 'Roldan'})
# print('____________________')
# print('')
# print('    PUT id = 2 ')
# print('status: '+ str(response.status_code))
# print('JSON: '+ str(response.json()))

# # DELETE
# response = requests.delete(BASE + "productos/1")

# print('____________________')
# print('')
# print('   DELETE id = 1 ')
# print('status: '+ str(response.status_code))
# print('JSON: '+ str(response.json()))

# muestra_productos()