import json
from textwrap import dedent
from urllib.parse import urljoin

import requests

if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"

    url = urljoin(base_url, "graphql")

    gquery = dedent(
        """\
        {
            hello
        }\
        """
    )
    response = requests.get(url=url, json={"query": gquery})
    print(f"gquery=\n{gquery}")
    print("response =", response.json(), end="\n\n")

    gquery = dedent(
        """\
        {
            ask(name: "myself")
        }\
        """
    )
    response = requests.get(url=url, json={"query": gquery})
    print(f"gquery=\n{gquery}")
    print("response =", response.json(), end="\n\n")

    gquery = dedent(
        """\
        {
            add(number: 7)
        }\
        """
    )
    response = requests.get(url=url, json={"query": gquery})
    print(f"gquery=\n{gquery}")
    print("response =", response.json(), end="\n\n")
