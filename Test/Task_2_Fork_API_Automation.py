import requests
from Object.locators import App_Data


headers = {
        "Content-Type": 'application/json',
        }
body_data = {

    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : 'true',
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

response = requests.post(App_Data.API_url, json=body_data, headers=headers) # Send Post request to API




assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

# Parse JSON response
json_response = response.json()

# Assert specific key-value pairs in the JSON response
booking_id = json_response.get('bookingid')
assert isinstance(booking_id, (int, float)) and booking_id != 0
assert json_response['booking']['firstname'] == "Jim", f"Expected firstname 'Jim', but got {json_response['booking']['firstname']}"
assert json_response['booking']['lastname'] == "Brown", f"Expected lastname 'Brown', but got {json_response['booking']['lastname']}"
assert json_response['booking']['totalprice'] == 111, f"Expected totalprice 111, but got {json_response['booking']['totalprice']}"
assert json_response['booking']['depositpaid'] is True, f"Expected depositpaid True, but got {json_response['booking']['depositpaid']}"