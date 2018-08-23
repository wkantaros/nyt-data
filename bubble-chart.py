import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import math
#
# data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
# df_2007 = data[data['year']==2007]
# df_2007 = df_2007.sort_values(['continent', 'country'])
# slope = 2.666051223553066e-05
# hover_text = []
# bubble_size = []
#
# for index, row in df_2007.iterrows():
#     hover_text.append(('Country: {country}<br>'+
#                       'Life Expectancy: {lifeExp}<br>'+
#                       'GDP per capita: {gdp}<br>'+
#                       'Population: {pop}<br>'+
#                       'Year: {year}').format(country=row['country'],
#                                             lifeExp=row['lifeExp'],
#                                             gdp=row['gdpPercap'],
#                                             pop=row['pop'],
#                                             year=row['year']))
#     bubble_size.append(math.sqrt(row['pop']*slope))
#
# df_2007['text'] = hover_text
# df_2007['size'] = bubble_size
# sizeref = 2.*max(df_2007['size'])/(100**2)
#
# trace0 = go.Scatter(
#     x=df_2007['gdpPercap'][df_2007['continent'] == 'Africa'],
#     y=df_2007['lifeExp'][df_2007['continent'] == 'Africa'],
#     mode='markers',
#     name='Africa',
#     text=df_2007['text'][df_2007['continent'] == 'Africa'],
#     marker=dict(
#         symbol='circle',
#         sizemode='area',
#         sizeref=sizeref,
#         size=df_2007['size'][df_2007['continent'] == 'Africa'],
#         line=dict(
#             width=2
#         ),
#     )
# )
# trace1 = go.Scatter(
#     x=df_2007['gdpPercap'][df_2007['continent'] == 'Americas'],
#     y=df_2007['lifeExp'][df_2007['continent'] == 'Americas'],
#     mode='markers',
#     name='Americas',
#     text=df_2007['text'][df_2007['continent'] == 'Americas'],
#     marker=dict(
#         sizemode='area',
#         sizeref=sizeref,
#         size=df_2007['size'][df_2007['continent'] == 'Americas'],
#         line=dict(
#             width=2
#         ),
#     )
# )
# trace2 = go.Scatter(
#     x=df_2007['gdpPercap'][df_2007['continent'] == 'Asia'],
#     y=df_2007['lifeExp'][df_2007['continent'] == 'Asia'],
#     mode='markers',
#     name='Asia',
#     text=df_2007['text'][df_2007['continent'] == 'Asia'],
#     marker=dict(
#         sizemode='area',
#         sizeref=sizeref,
#         size=df_2007['size'][df_2007['continent'] == 'Asia'],
#         line=dict(
#             width=2
#         ),
#     )
# )
# trace3 = go.Scatter(
#     x=df_2007['gdpPercap'][df_2007['continent'] == 'Europe'],
#     y=df_2007['lifeExp'][df_2007['continent'] == 'Europe'],
#     mode='markers',
#     name='Europe',
#     text=df_2007['text'][df_2007['continent'] == 'Europe'],
#     marker=dict(
#         sizemode='area',
#         sizeref=sizeref,
#         size=df_2007['size'][df_2007['continent'] == 'Europe'],
#         line=dict(
#             width=2
#         ),
#     )
# )
# trace4 = go.Scatter(
#     x=df_2007['gdpPercap'][df_2007['continent'] == 'Oceania'],
#     y=df_2007['lifeExp'][df_2007['continent'] == 'Oceania'],
#     mode='markers',
#     name='Oceania',
#     text=df_2007['text'][df_2007['continent'] == 'Oceania'],
#     marker=dict(
#         sizemode='area',
#         sizeref=sizeref,
#         size=df_2007['size'][df_2007['continent'] == 'Oceania'],
#         line=dict(
#             width=2
#         ),
#     )
# )
#
# data = [trace0, trace1, trace2, trace3, trace4]
# layout = go.Layout(
#     title='Life Expectancy v. Per Capita GDP, 2007',
#     xaxis=dict(
#         title='GDP per capita (2000 dollars)',
#         gridcolor='rgb(255, 255, 255)',
#         range=[2.003297660701705, 5.191505530708712],
#         type='log',
#         zerolinewidth=1,
#         ticklen=5,
#         gridwidth=2,
#     ),
#     yaxis=dict(
#         title='Life Expectancy (years)',
#         gridcolor='rgb(255, 255, 255)',
#         range=[36.12621671352166, 91.72921793264332],
#         zerolinewidth=1,
#         ticklen=5,
#         gridwidth=2,
#     ),
#     paper_bgcolor='rgb(243, 243, 243)',
#     plot_bgcolor='rgb(243, 243, 243)',
# )
#
# fig = go.Figure(data=data, layout=layout)
# py.iplot(fig, filename='life-expectancy-per-GDP-2007')
#

data = pd.read_csv("updated_stats.csv")
s = data.iloc[data.index.size - 1].dropna()

hover_text = []
bubble_size = []

for i in range(2, s.size):
    hover_text.append(('Topic: {topic}<br>'+
                      'Percent Women: {pwomen}<br>'+
                      'Year: {year}').format(topic=s.index[i],
                                            pwomen=s.iloc[i],
                                            year=s.iloc[0]))
    bubble_size.append(s.iloc[i])

s = s.drop(labels=['Year','Month'])
df = pd.DataFrame({'topic':s.index, 'percent':s.values})
df['text'] = hover_text
df['size'] = bubble_size
sizeref = 2.*max(df['size'])/(100**2)

data = [
    {
        'x':100 - df['size'],
        'y':df['size'],
        'mode':'markers',
        'name':'2016',
        'text':df['text'],
        'marker': {
            'symbol':'circle',
            'sizemode':'area',
            'sizeref':sizeref,
            'size':df['size'],
            'line':{
                'width':2
            }
        }
    }
]

layout = go.Layout(
    title='Percent of Articles by Gender, by Topic, 2016',
    xaxis=dict(
        title='Percent of Articles by Men',
        gridcolor='rgb(255, 255, 255)',
        range=[0, 100],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Percent of Articles by Women',
        gridcolor='rgb(255, 255, 255)',
        range=[0, 100],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='articles-by-gender-topic')

# data = [
#     {
#         'x': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
#         'y': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
#         'mode': 'markers',
#         'marker': {
#             'color': [120, 125, 130, 135, 140, 145],
#             'size': [15, 30, 55, 70, 90, 110],
#             'showscale': True
#         }
#     }
# ]
#
# py.iplot(data, filename='scatter-colorscale')
