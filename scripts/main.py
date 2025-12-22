import os
import sys
import requests
import json

API_URLS  = json.loads(open('../JSON/API_URL').read())
API_POSTS = json.loads(open('../JSON/API_URL_POST').read())
API_GETS  = json.loads(open('../JSON/API_URL_GET').read())


Url_type = [API_URLS["dppack"],
            API_URLS["atendimentos"],
            API_URLS["cnd"],
            API_URLS["documentos"],
            API_URLS["identificacao"]]

URl_Endpoint_POST = [API_POSTS["CAND"],
                    API_POSTS["AGEN_FERI"],
                    API_POSTS["ATEN"],
                    API_POSTS["NOTI_RESC"],
                    API_POSTS["MOVI"],
                    API_POSTS["INTE_ALTE"]]


URl_Endpoint_GET = [API_GETS["CAND"],
                    API_GETS["AGEN_FERI"],
                    API_GETS["ATEN"],
                    API_GETS["NOTI_RESC"],
                    API_GETS["MOVI"],
                    API_GETS["INTE_ALTE"],
                    API_GETS["HIST_TARE"],
                    API_GETS["HIST_FUNC"],
                    API_GETS["USUA"]]


TOKEN_ENV_NAME = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1YyI6IjI1NzM5IiwiaXNzIjoicGFja3VwIiwiZGF0YSI6IjIwMjUtMTItMDhUMDg6MTg6MTAuNTIxMzk5Ny0wMzowMCJ9.bjcJPqjyvNXFUpwwgX_7qR45Q-fdlVc-DApUxs6TB9SJhSi4lz9NX5gQP_IYch9G6M6NEwsG6tQctKqeXcZ9Ww"   # nome da variável de ambiente que guarda o token

def get_bearer_token():
    token = TOKEN_ENV_NAME
    if token:
        return token
    print(f"Erro: variável de ambiente {TOKEN_ENV_NAME} não encontrada.")
    sys.exit(1)

def get_resource(Params=None,API_URL=None):
    token = get_bearer_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.api+json",
        "User-Agent": "imperio-client/1.0"
    }
    try:
        resp = requests.get(API_URL, headers=headers, params=Params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print("Requisição falhou:", e)
        sys.exit(2)
    except ValueError:
        print("Resposta não é JSON válido.")
        sys.exit(3)

def GET_CATE_DOC(Params={}):
   # params = {"filter[login]": 31616520000157,"filter[descricao]": "Livros Fiscais/Contábeis"}
    API_URL = Url_type[2]+URl_Endpoint_GET[2]
    data = get_resource(Params=Params,API_URL=API_URL)
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    GET_CATE_DOC({})

    