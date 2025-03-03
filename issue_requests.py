from urllib.parse import urljoin

import requests

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"
    response = requests.get(
        url=urljoin(base_url, "data"), headers={"Content-Type": "application/json"}
    )
    print(response.json())
