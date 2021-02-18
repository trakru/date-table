Create a Date Table for all Data in Redshift

Columns are as follows:

Column Name | Data Type | Description
timestampID | timestamp | Primary Key. Each row represents 5 minute chunks of time
timstampfloor | timestamp | floor value of timestamp (to the start of the hour)
CALDATE | date | calendar date 2020-01-01
CALHOUR | smallint | hour of day
DAY | CHAR(3) | day of week (MO, TU etc)
WEEK | smallint | week number
MONTH | CHAR(5) | Short form of month (JUN, JUL etc)
QTR | CHAR(5) | Quarter number 1 through 4
YEAR | smallint | four digit year (2020)
HOLIDAY | BOOLEAN | Flag that denotes whether the day is a US public holiday

