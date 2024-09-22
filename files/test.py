import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

data = {
    "Inputs": {
        "data": [
            {
                "ano_campeonato": 2023,
                "mes": 6,
                "dia": 23,
                "week_day": 5,
                "rodada": 11,
                "estadio": 15,
                "arbitro": 53,
                "time_mandante": 17,
                "time_visitante": 37,
                "tecnico_mandante": 113,
                "tecnico_visitante": 135,
                "colocacao_mandante": 19,
                "colocacao_visitante": 17,
                "valor_equipe_titular_mandante": 3610,
                "valor_equipe_titular_visitante": 1030,
                "idade_media_titular_mandante": 23.9,
                "idade_media_titular_visitante": 28.2,
                "gols_1_tempo_mandante": 0,
                "gols_1_tempo_visitante": 0,
                "escanteios_mandante": 0,
                "escanteios_visitante": 4,
                "faltas_mandante": 11,
                "faltas_visitante": 15,
                "chutes_bola_parada_mandante": 15,
                "chutes_bola_parada_visitante": 9,
                "defesas_mandante": 3,
                "defesas_visitante": 2,
                "impedimentos_mandante": 3,
                "impedimentos_visitante": 4,
                "chutes_mandante": 10,
                "chutes_visitante": 15,
                "chutes_fora_mandante": 4,
                "chutes_fora_visitante": 7
            }
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

body = str.encode(json.dumps(data))

url = 'ENDPOINT DO MODEL'
api_key = ''
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
