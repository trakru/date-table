import pyarrow.parquet as pq
import pandas as pd
from pathlib import Path


p = Path(Path().resolve().parent, "data", "date-table.parquet")

table = pq.read_table(p)
df = table.to_pandas()

print(df.head(5))