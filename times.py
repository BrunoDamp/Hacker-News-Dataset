import read
from dateutil.parser import parse
import datetime

df = read.load_data()

def extract_hour(timestamp):
    dt = parse(timestamp)
    return str(dt.hour)

times = df['submission_time'].apply(extract_hour).value_counts()

print(times)