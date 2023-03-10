import requests

def check_spellings(text):
    url = "https://api.spellcheck.bangla.gov.bd/checking"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "service": "spell",
        "content": text,
        "maxSuggestionCount": 10,
        "permissionToStoreData": True,
        "client": 17,
        "appVersion": "0.1.7",
        "apiVersion": "2.0",
        "userStoredData": {
            "addToDictionaryTokens": [],
            "ignoreAllTokens": [],
            "ignoreOnceTokens": []
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        json_response = response.json()
        tokens = json_response["tokens"]
        corrected_tokens = []
        for token in tokens:
            corrected_tokens.append(token["token"])
        corrected_text = " ".join(corrected_tokens)
        return corrected_text
    else:
        return None

# example usage
text = "the text i am testing"
corrected_text = check_spellings(text)
print(corrected_text)
