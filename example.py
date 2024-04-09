import numpy as np
import json
import requests


def get_embedding(sentence: str) -> np.ndarray:
    url = 'http://localhost:5000/v1/embeddings'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {
        "input": sentence
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise ValueError(f'Error: {response.status_code}')
    else:
        embedding_vector = np.array(response.json()['data'][0]['embedding'])
        return embedding_vector


def run_example():
    sentence = 'Here is an example sentence'
    embedding = get_embedding(sentence=sentence)
    print('EMBEDDING: ')
    print(embedding)


if __name__ == '__main__':
    run_example()
