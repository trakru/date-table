import datetime
import pandas as pd
import sys
import argparse

def create_calendar(start,end):
    message = f'start:{start} end:{end}'
    print(message)
# dti = pd.date_range()

# start = sys.argv[1]
# end = sys.argv[2]

parser = argparse.ArgumentParser(description='Provide Start & End dates')

parser.add_argument('-s', "--startdate",
    help="Start Date - format YYYY-MM-DD",
    required=True,
    type=datetime.date.fromisoformat)
parser.add_argument('-e', "--enddate",
    help="End Date format YYYY-MM-DD (Inclusive)",
    required=True,
    type=datetime.date.fromisoformat)

args = parser.parse_args()

start = args.startdate
end = args.enddate

# create_calendar(start, end)

if __name__ == '__main__':
    create_calendar(start, end)
    # print(args.startdate)
    # print(args.enddate)

