import datetime
import pandas as pd
import argparse
from pandas.tseries.holiday import USFederalHolidayCalendar as holiday_calendar
from pathlib import Path

p = Path(Path().resolve().parent, "data", "date-table.csv")

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

startdate = args.startdate
enddate = args.enddate

def create_calendar(start,end):
    cal = holiday_calendar()
    holidays = cal.holidays(start=startdate, end=enddate)
    holidays=holidays.date
    weekends = ['5', '6']
    dti = pd.date_range(startdate, enddate, freq='5 Min')
    df = pd.DataFrame(dti)
    df.columns=['timestampID']
    df['caldate'] = df.timestampID.dt.date
    df['calhour'] = df.timestampID.dt.hour
    df['dayofyear'] = df.timestampID.dt.dayofyear
    df['dayofweek'] = df.timestampID.dt.dayofweek
    df['month'] = df.timestampID.dt.month
    df['year'] = df.timestampID.dt.year
    df['week'] = df.timestampID.dt.isocalendar().week
    df['quarter'] = df.timestampID.dt.quarter
    df['holiday'] = df.caldate.isin(holidays)
    df['weekend'] = df.dayofweek.isin(weekends)
    # print(df[df.holiday == True].head(10))  # testing to see if Fed holidays are working
    df.to_csv(p)

if __name__ == '__main__':
    create_calendar(startdate, enddate)

