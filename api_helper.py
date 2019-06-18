import requests
import logging
import time

class ApiHelper:
    def __init__(self):
        self.url = "https://swapi.co/api"
        self.people_endpoint = "people"
        self.people_count = 0
        timestamp = str(int(time.time()))
        logging.basicConfig(filename='api_helper_{}.log'.format(timestamp),level=logging.DEBUG,
                            filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    def get_data(self,url):
        """perform GET request

        :param url: API URL
        :return:json result
        """
        response = requests.get(url)
        if response.status_code != 200:
            logging.error("Get request failed for url : {}".format(url))
            raise Exception("Get request failed for url : {}".format(url))
        else:
            return {"data": response.json(), "header":response.headers}

    def star_wars_characters(self, page_nr=None):
        """
        returns a list, of the name, height, and gender of each
        :param page_nr = number: returns star wars characters for given page number
               page_nr = None : navigates through each page and returns all page data
        :return: list
        """
        starwars_characters = []
        characters=[]
        if page_nr:
            people_url = "{}/{}/?page={}".format(self.url, self.people_endpoint,str(page_nr))
            logging.debug("GET request for url: {}".format(people_url))
            response = self.get_data(people_url)
            starwars_characters = self.parse_result(response["data"]["results"])
        else :
            people_url = "{}/{}".format(self.url, self.people_endpoint)
            response = self.get_data(people_url)
            pg_url = response["data"]["next"]
            while pg_url:
                logging.debug("GET request for url: {}".format(pg_url))
                characters = self.parse_result(response["data"]["results"])
                starwars_characters.extend(characters)
                response = self.get_data(pg_url)
                pg_url = response["data"]["next"]
        return starwars_characters

    def parse_result(self,result):
        """

        :param response:
        :return:
        """
        person_list = []
        for person in result:
            character = {"name": person["name"], "height": person["height"], "gender": person["gender"]}
            person_list.append(character)
        return person_list