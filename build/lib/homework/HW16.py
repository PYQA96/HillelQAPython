import requests
import json

url = "https://restful-booker.herokuapp.com/auth"

payload = json.dumps({
  "username": "admin",
  "password": "password123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://restful-booker.herokuapp.com/booking"

payload = {}
headers = {
  'token': '47cbb9f11cd1fd8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
url = "https://restful-booker.herokuapp.com/booking/1"

payload = {}
headers = {
  'Accept': 'application/json',
  'token': '47cbb9f11cd1fd8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
url = "https://restful-booker.herokuapp.com/booking"

payload = json.dumps({
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json',
  'token': ' 47cbb9f11cd1fd8'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://restful-booker.herokuapp.com/booking/1"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': '47cbb9f11cd1fd8'
}

response = requests.request("PUT", url, headers=headers, data=payload)

url = "https://restful-booker.herokuapp.com/booking/1"

payload = json.dumps({
  "firstname": "James",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": True,
  "bookingdates": {
    "checkin": "2018-01-01",
    "checkout": "2019-01-01"
  },
  "additionalneeds": "Breakfast"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': '47cbb9f11cd1fd8'
}

response = requests.request("PUT", url, headers=headers, data=payload)


url = "https://restful-booker.herokuapp.com/booking/1"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'token=token: 47cbb9f11cd1fd8'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)