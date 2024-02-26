import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program)

        return programs_list
    
# object = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').get_response_body()
# print(object)
    
# object = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').load_json()    
# print(object)
