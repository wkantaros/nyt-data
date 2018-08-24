import plotly.plotly as py
import plotly.graph_objs as go

import cmocean
import json

import pandas as pd
import numpy as np
import pickle

data = pd.read_csv("updated_stats.csv")
s = data.iloc[data.index.size - 1].dropna()
with open('monthly_stats_dict.pickle', 'rb') as handle:
        counts_dict = pickle.load(handle)


hover_text = []
bubble_size = []
x = []
y = []
t = counts_dict['2016']['12']

for key, value in t.items():
    if value['total'] == 0:
        continue
    else:
        x.append(value['total'])
        y.append(value['women']/value['total'] * 100)
        bubble_size.append(value['women'] + 2)
        hover_text.append(('Topic: {topic}<br>'+
                          'Number of Women: {nwomen}<br>' +
                          'Total Articles: {total}<br>' +
                          'Percent Women: {pwomen}').format(topic=key,
                                                nwomen=value['women'],
                                                total=value['total'],
                                                pwomen=value['women']/value['total']*100))

s = s.drop(labels=['Year','Month'])
df = pd.DataFrame({'topic':s.index, 'percent':s.values})
df['text'] = hover_text
df['size'] = bubble_size
# sizeref = 2.*max(df['size'])/(100**2)
sizeref = 2.*max(bubble_size)/(100**2)

trace0 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='2016',
    text=hover_text,
    marker=dict(
        color= '#66C3FF',
        symbol='circle',
        sizemode='area',
        sizeref=sizeref,
        size=bubble_size,
        line=dict(
            width=2
        )
    )
)
data = [trace0]
# data = [
#     {
#         'x':x,
#         'y':y,
#         'mode':'markers',
#         'name':'2016',
#         'text':hover_text,
#         'marker': {
#             'color': '#66C3FF',
#             'symbol':'circle',
#             'sizemode':'area',
#             'sizeref':sizeref,
#             'size':bubble_size,
#             'line':{
#                 'width':2
#             }
#         }
#     }
# ]

layout = go.Layout(
    title='Percent of Articles by Gender, by Topic, 2016',
    titlefont=dict(
        size=22
    ),
    xaxis=dict(
        title='Number of Articles by Topic',
        titlefont=dict(
            size=18
        ),
        # gridcolor='rgb(255, 255, 255)',
        gridcolor='rgb(243, 243, 243)',
        range=[0, 600],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Percent of Articles by Women, by Topic',
        titlefont=dict(
            size=18
        ),
        # gridcolor='rgb(255, 255, 255)',
        gridcolor='rgb(243, 243, 243)',
        range=[0, 105],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),

    shapes=[
        # Line Horizontal
        dict(
            type='line',
            x0=0,
            y0=50,
            x1=600,
            y1=50,
            line=dict(
                color='#E56399',
                width=2,
                dash='dot',
            )
        )
    ],
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(255, 255, 255)',
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='articles-by-gender-topic')
