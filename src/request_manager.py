import requests

class RequestManager:
    def __init__(self):
        self.url = "https://truth-lens-api-86f85eeef375.herokuapp.com/"
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "request"
        }

    def get_user_info(self, prompt):
        body = {
            "text": prompt
        }
        response = requests.post(self.url + 'answer', headers=self.headers, json=body)
        return response.json()

    '''
    {
        "predicted_class": 0,
        "predicted_proba": [
            0.6657964661133176,
            0.3342035338866825
        ],
        "answer": "F"
    }
    '''
    def get_beatiful_info(self, info):
        answer = info['answer']
        max_proba = max(info['predicted_proba'])

        emoji = "✅" if answer == "T" else "❌"
        truthfulness = "истина" if answer == "T" else "лъжа"

        return f"Бих казал, че заглавието е {truthfulness} {emoji} с вероятност {max_proba:.2f}"

