import json

# Read config file.
# route.json is a configuration file for town station infomation.
def station_conf():
    with open("./src/conf/route.json", "r") as conf:
        return json.loads(conf.read())


stations = station_conf()
