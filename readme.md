## Create a Date Table for all Data in Redshift

Columns are as follows:

| Column Name | Data Type | Description |
|------------ | ------------- | ---------------------------------------------------|
| timestampID | timestamp | Primary Key. Each row represents 5 minute chunks of time |
| caldate | date | calendar date 2020-01-01 |
| calhour | smallint | hour of day |
| dayofyear | smallint | day of year |
| month | smallint | month number |
| year | smallint | four digit year (2020) |
| week | smallint | week number |
| qtr | CHAR(5) | Quarter number 1 through 4 |
| holiday | BOOLEAN | Flag that denotes whether the day is a US public holiday |
| weekend | BOOLEAN | Flag that denotes whether the day is a weekend |

