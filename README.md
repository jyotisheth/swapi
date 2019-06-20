
### Isentia Python Test

##### This project contains code for below assignments:
- Write a python class, that goes through each paginated 
response of API: https://swapi.co/api/people/ and returns a list of the name, height, and gender of each Star Wars character.
def star_wars_characters(self, page_nr):
- Further, export all star wars characters list to CSV file
- Add unit test to verify non empty star_wars_character list is retrieved from the swapi API
- Add decorator to log method name and passed arguments in the log file

##### Prerequisites
- Python 3.7.2 (installed and configured)
```pip install -r requirements.txt```

##### Running the unit tests
```python -m unittest test.api_helper_test```

##### Running program
```python main.py```
