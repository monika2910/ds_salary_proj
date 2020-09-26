from pandas import DataFrame

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/44785/Documents/GitHub/ds_salary_proj/chromedriver"
df: DataFrame = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)
df