import config
import datetime

def sim2realtime(simulation_time):
    return config.__start + datetime.timedelta(seconds=simulation_time)
