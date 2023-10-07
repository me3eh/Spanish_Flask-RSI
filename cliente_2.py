import requests

BASE = "http://127.0.0.1:5000/"

def muestra_productos():

    response = requests.get(BASE + "productos/")

    print('____________________')
    print('')
    print('   GET productos ')
    print('status: '+ str(response.status_code))
    print('JSON: '+ str(response.json()))

response = requests.post(BASE + "productos/", 
                         json = {'nombre': 'tomate', 
                                 'origen': 'Mazarron', 
                                 'precio': 0.7, 
                                 'descripcion': 'tomate de pera'})

print('____________________')
print('')
print('introducimos tomate')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.post(BASE + "productos/", json = {'nombre': 'lechuga', 
                                                      'origen': 'Torre Pacheco', 
                                                      'precio': 0.7, 
                                                      'descripcion': 'lechuga de ensalada'})

print('____________________')
print('')
print('introducimos lechuga')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

muestra_productos()

response = requests.get(BASE + "productos?nombre=lechuga")
print('____________________')
print('')
print('consultamos nombre=lechuga')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.get(BASE + "productos?precio=0.7")
print('____________________')
print('')
print('consultamos precio=0.7')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.get(BASE + "productos?nombre=broccoli")
print('____________________')
print('')
print('consultamos nombre=broccoli')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))
