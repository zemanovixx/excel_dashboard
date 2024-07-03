import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from plotly.colors import n_colors


df = pd.read_excel('data.xlsx')

df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

def progress_calc(start_date,end_date):
    current_date = datetime.now()
    total_days = (end_date - start_date).days
    elapsed_days = (current_date - start_date).days
    progress = (elapsed_days * 100)/total_days
    return progress

progress_arr = []
for index, row in df.iterrows():
    start_date = row['start']
    end_date = row['end']
    progress  = progress_calc(start_date,end_date)
    progress_arr.append(progress)

farby = n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', len(progress_arr), colortype='rgb')

fig = go.Figure()
fig.add_trace(go.Bar(
    x=progress_arr,
    y = list(range(len(progress_arr))),
    orientation='h',
    marker=dict(color=farby),
    
    ))
fig.update_layout(
    width=5,
    barmode = 'stack'
)

fig.show()