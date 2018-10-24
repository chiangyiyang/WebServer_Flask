

import urequests

#response = urequests.post("http://jsonplaceholder.typicode.com/posts", data = "some dummy content")
#response = urequests.get("http://192.168.1.4:8080")
#response = urequests.get("http://192.168.1.4:8080/login")
response = urequests.post("http://192.168.1.4:8080/dht", json={'temp':123})

print(response.text)



