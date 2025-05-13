import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('base_vendas.csv', encoding='latin1')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("your_report.html")
