import requests

url = "http://127.0.0.1:8000/chat"
data = {"query": "Hello"}

with requests.post(url, json=data, stream=True) as response:
    print(f'response : {response}');
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                print(line.decode("utf-8"))  # Print each chunk as it is received
    else:
        print(f"Failed to connect. Status code: {response.status_code}, {response}")
