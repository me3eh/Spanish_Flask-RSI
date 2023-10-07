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
response = requests.post(BASE + "productos/", json = {'name': 'tomate',
                                                      'height': 122.4,
                                                      'age': 23})

print('____________________')
print('')
print('introducimos tomate')
print('status: '+ str(response.status_code))
print('cabecera: '+ str(response.headers))
print('JSON: '+ str(response.json()))


# creamos segundo recurso
response = requests.post(BASE + "productos/", json = {'name': 'lechuga',
                                                      'height': 144.4,
                                                      'age': 33})

print('____________________')
print('')
print('introducimos lechuga')
print('status: '+ str(response.status_code))
print('cabecera: '+ str(response.headers))
print('JSON: '+ str(response.json()))

muestra_productos()

# creamos un recurso con definición incompleta --> DEBE DAR ERROR
response = requests.post(BASE + "productos/", json = {'name': 'acelgas',
                                                      'height': 166.4,
                                                      'age': 23
                                                      })

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

# PUT a un recurso
response = requests.put(BASE + "productos/2", json = {'name': 'melon',
                                                     'height': 2000.4,
                                                      'age': 55})
print('____________________')
print('')
print('    PUT id = 2 ')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

# DELETE
response = requests.delete(BASE + "productos/1")

print('____________________')
print('')
print('   DELETE id = 1 ')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

muestra_productos()