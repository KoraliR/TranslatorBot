import requests, os, json

FOLDER_ID = "b1ge0b1ud4qfu0tv97iu"
target_language = 'ru'


def start():
    TOKEN_FILE_NAME = "Yandex_api_token.txt"
    api_token_path = os.path.join(os.getcwd(), TOKEN_FILE_NAME)
    with open(api_token_path) as f:
        API_TOKEN = f.read().strip()
    return API_TOKEN

def make_request(texts, token):
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": FOLDER_ID,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key {0}".format(token)
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    translated_text = response.json()
    translated_text = translated_text.get("translations")[0]["text"]
    print("API!!!!")
    return translated_text