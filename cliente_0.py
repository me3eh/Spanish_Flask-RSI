import requests
BASE = "http://localhost:5000"
# create first resource
response = requests.post ( BASE + "/products/" , json = {"name": "123",
    "height": 144,
    "age": 21
})

print ( '____________________' )
print ( '' )
print ( ' we enter tomato ' )
print ( 'status: ' + str ( response.status_code ))
print ( 'header: ' + str ( response.headers ))
print ( 'JSON: ' + str ( response))
print ( 'JSON: ' + str(response))