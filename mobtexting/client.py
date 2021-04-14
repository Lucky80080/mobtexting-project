import requests

api_endpoint = 'https://portal.mobtexting.com/api/v2/'


class Client:
    def __init__(self, access_token):
        self.headers = {
            'Accept': 'application/json',
            'Authorization': access_token
        }

    def send(self, to, _from, body, service='T', data={}):
        url = api_endpoint + 'sms/send?message=' \
              + body + '&sender=' + _from + '&to=' + to + '&service=' + service
        x = requests.post(url, data=data, headers=self.headers)
        return x

    def post_request(self, to, _from, body, service='T', data={}):
        url = api_endpoint + 'sms/send?message=' \
              + body + '&sender=' + _from + '&to=' + to + '&service=' + service
        x = requests.post(url, data=data, headers=self.headers)
        return x
