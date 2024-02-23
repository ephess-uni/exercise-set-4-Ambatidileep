""" ex_4_3.py """
import os
from datetime import timedelta
try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

FILENAME = get_data_file_path("messages.log")


def time_between_shutdowns(logfile):
    shutdown_events = get_shutdown_events(logfile)

    if not shutdown_events:
        return timedelta()  
    first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split()[1])
    time_difference = last_shutdown_time - first_shutdown_time

    return time_difference

if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
