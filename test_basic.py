import json
from urllib.parse import urljoin

import requests

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"

    url = base_url
    print(f"{url=}")
    print("response =", requests.get(url=url).text, end="\n\n")

    url = urljoin(base_url, "hello")
    print(f"{url=}")
    print("response =", requests.get(url=url).text, end="\n\n")

    url = urljoin(base_url, "data")
    print(f"{url=}")
    print("response =", requests.get(url=url).text, end="\n\n")

    url = urljoin(base_url, "data")
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"return_type": "json"})
    print(f"{url=}")
    print(f"{headers=}")
    print(f"{data=}")
    print("response =", requests.get(url=url, headers=headers, data=data).json())
