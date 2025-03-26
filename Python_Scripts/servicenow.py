import requests
import json

# ServiceNow instance credentials
INSTANCE = 'dev252340'
USERNAME = 'admin'
PASSWORD = 'aGNUwwv1$5C!'

# ServiceNow API endpoint for incident creation
url = f'https://{INSTANCE}.service-now.com/api/now/table/incident'

# Incident payload in JSON format
incident_data = {
    'short_description': 'Panner Momos',
    'description': 'Panner Momos',
    'caller_id': 'Panner Momos',  # You can specify the caller's name or ID
    'category': 'Postman',   # Example category
    'impact': '3',  # Example impact, 1 for High, 2 for Medium, 3 for Low
    'urgency': '3',  # Example urgency, 1 for High, 2 for Medium, 3 for Low
    'assigned to': 'paneer.momos'
}

# Headers for HTTP POST request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Authenticate and create incident
response = requests.post(url, auth=(USERNAME, PASSWORD), headers=headers, data=json.dumps(incident_data))

# Check response
if response.status_code == 201:
    print("Incident created successfully!")
else:
    print(f"Failed to create incident. Status code: {response.status_code}, Response: {response.text}")
