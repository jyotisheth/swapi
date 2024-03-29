import requests
import logging
import time

def log_args(func_name):
    """Decorator function for logging method name and arguments
    :param func_name: name of the function to be decorated
    :return: returns original function
    """
    def _log_args(*args,**kwargs):
        logging.debug("Processing Function name:{},arguments:{}".format(func_name.__name__,args[1:]))
        return (func_name(*args, **kwargs))
    return _log_args

class ApiHelper:
    def __init__(self):
        self.url = "https://swapi.co/api"
        self.people_endpoint = "people"
        self.people_count = 0
        timestamp = str(int(time.time()))
        logging.basicConfig(filename='api_helper_{}.log'.format(timestamp),level=logging.DEBUG,
                            filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    @log_args
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

    @log_args
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
            logging.debug("GET request for url: {}".format(people_url))
            response = self.get_data(people_url)
            pg_url = response["data"]["next"]
            characters = self.parse_result(response["data"]["results"])
            starwars_characters.extend(characters)
            while pg_url:
                logging.debug("GET request for url: {}".format(pg_url))
                response = self.get_data(pg_url)
                characters = self.parse_result(response["data"]["results"])
                starwars_characters.extend(characters)
                pg_url = response["data"]["next"]
        return starwars_characters

    @log_args
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