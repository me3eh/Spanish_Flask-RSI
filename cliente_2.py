import requests

BASE = "http://localhost:5000/"

def muestra_productos():

    response = requests.get(BASE + "productos/")

    print('____________________')
    print('')
    print('   GET productos ')
    print('status: '+ str(response.status_code))
    print('JSON: '+ str(response.json()))

response = requests.post(BASE + "productos/", 
                         json = {'name': 'tomate',
                                 'height': 155.7,
                                 'age': 23 })

print('____________________')
print('')
print('introducimos tomate')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.post(BASE + "productos/", json = {'name': 'lechuga',
                                                      'height': 0.7,
                                                      'age': 21})

print('____________________')
print('')
print('introducimos lechuga')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

muestra_productos()

response = requests.get(BASE + "productos?name=lechuga")
print('____________________')
print('')
print('consultamos name=lechuga')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.get(BASE + "productos?height=0.7")
print('____________________')
print('')
print('consultamos precio=0.7')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))

response = requests.get(BASE + "productos?name=broccoli")
print('____________________')
print('')
print('consultamos name=broccoli')
print('status: '+ str(response.status_code))
print('JSON: '+ str(response.json()))
