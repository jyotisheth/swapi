from api_helper import ApiHelper
import time

def append_to_file(filepath, name, height, gender):
    FP = open(filepath,"a+")
    line = "{}, {}, {}".format(name,height,gender)
    FP.write(line + '\n')
    FP.close()


if __name__ == '__main__':
    api_helper = ApiHelper()
    starwars_characters = api_helper.star_wars_characters()
    timestamp = int(time.time())
    filepath = "starwars_char_{}.csv".format(str(timestamp))
    append_to_file(filepath, "Name", "Height", "Gender")
    for character in starwars_characters:
        append_to_file(filepath, character["name"], character["height"], character["gender"])
