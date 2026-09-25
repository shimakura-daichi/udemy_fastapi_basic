import json
import requests
from datetime import datetime

def main():
    base_url = "http://localhost:8000/contacts"
    current_time = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "John Doe",
        "email": "test1@test.com",
        "url": "https://example.com/johndoe",
        "gender": 1,
        "message": "メッセージです",
        "is_enabled": False,
        "created_at": current_time
    }
    response = requests.post(base_url, json.dumps(body))
    print(response.json())

if __name__ == "__main__":
    main()