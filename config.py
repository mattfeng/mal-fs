import datetime

# Configurable simulation start time to represent real world times (24 hour time)
SIMULATION_START_TIME = '09/07/2016 12:00:00'
__start = datetime.datetime.strptime(SIMULATION_START_TIME, '%d/%m/%Y %H:%M:%S')

OUTPUT_FILE = '/home/pwn/PycharmProjects/mal-fs/output/output_flows1.txt'
