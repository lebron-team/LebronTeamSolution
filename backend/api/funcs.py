from datetime import datetime

def time_to_unix(dj_time):
    time_list = list(map(int, (dj_time.strftime('%Y,%m,%d,%H,%M').split(','))))
    return datetime(time_list[0], time_list[1], time_list[2], time_list[3], time_list[4]).timestamp()
def unix_to_time(unix_time):
    dt = datetime.fromtimestamp(unix_time)
    return dt