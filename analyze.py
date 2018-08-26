import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

## data for the bar graph of total gender by month
def getGenderByMonth():
    data = np.ones(((len(os.listdir('data_conserv'))), 3), dtype=int)
    # data = np.ones(((len(os.listdir('data_conserv'))-1), 3), dtype=int)
    index = 0
    for filename in os.listdir('data_conserv'):
        if('.csv' in filename):
            df = pd.read_csv('data_conserv/{}'.format(filename))
            data[index, 0] = filename[:7].replace('-','')
            data[index, 1] = df[df.gender=='M'].gender.size
            data[index, 2] = df[df.gender=='F'].gender.size
            index += 1
    data = data[data[:,0].argsort()] # sorts data so smallest dates are first
    return data

# makes the bar graph of total gender by month,
# calling makeBarGraph(getGenderByMonth()) would make it
def makeBarGraph(data):
    N = data[:,0].size
    Males = data[:,1]

    fig, ax = plt.subplots()

    ind = np.arange(N)    # the x locations for the groups
    width = 0.5         # the width of the bars
    p1 = ax.bar(ind, Males, width, color='#66C3FF')
    # p1 = ax.bar(ind, Males, width)


    Females = data[:,2]
    p2 = ax.bar(ind + width, Females, width,
                color='#E56399')
    # p2 = ax.bar(ind + width, Females, width)

    ax.set_title("Monthly Articles by Writer's Gender", fontsize=16)
    ax.set_xticks(ind + width / 2)

    strDates = [str(date) for date in data[:,0]]
    strDates = [date[:4] if int(date[4:]) is 1 else '' for date in strDates]

    ax.set_xticklabels(strDates)
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=True)
    plt.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left=False,      # ticks along the bottom edge are off
        right=False)         # ticks along the top edge are off
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.legend((p1[0], p2[0]), ('Males', 'Females'))
    ax.autoscale_view()
    plt.show()

def makePlotLy(data):
    strDates = [str(date) for date in data[:,0]]
    # years = [(date[:4] + '-' date[4:]) if int(date[4:]) is 1 else (date + 'a') for date in strDates]
    years = [(date[:4] + '-' + date[4:]) for date in strDates]
    hover_text=[]
    for num in range(data[:,1].size):
        hover_text.append(('Number Males: {men}<br>' +
                           'Number Females: {women}<br>' +
                           'Month-Year: {year}-{month}').format(men=data[num,1],
                                                                women=data[num,2],
                                                                month=strDates[num][4:],
                                                                year=strDates[num][:4])
        )
    trace1 = go.Bar(
        x=years,
        y=data[:,1],
        text=hover_text,
        name='Males',
        marker=dict(
            color='#66C3FF'
        )
    )
    trace2 = go.Bar(
        x=years,
        y=data[:,2],
        text=hover_text,
        name='Females',
        marker=dict(
            color='#E56399'
        )
    )
    data = [trace1, trace2]
    layout = go.Layout(
        title='Monthly Articles by Writer\'s Gender',
        titlefont=dict(
            size=24
        ),
        xaxis=dict(
            type='category',
            nticks=18,
            tickangle=-45,
            tickfont=dict(
                size=14,
                color='#333'
            )
        ),
        yaxis=dict(
            tickfont=dict(
                size=14,
                color='#333'
            )
        ),
        legend=dict(
            x=0.9,
            y=0.9,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
            # titlefont=dict(
            #     size=18
            # )
        ),
        barmode='group',
        bargap=0,
        bargroupgap=0
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='style-bar')

if __name__ == "__main__":
    # makeBarGraph(getGenderByMonth())
    makePlotLy(getGenderByMonth())
