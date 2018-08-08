import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

def getGenderByMonth():
    # date, males, females
    data = np.ones(((len(os.listdir('data'))-1), 3), dtype=int)
    # males = np.ones(len(os.listdir('data'))-1)
    # females = np.ones(len(os.listdir('data'))-1)

    index = 0
    for filename in os.listdir('data'):
        if('.csv' in filename):
            df = pd.read_csv('data/{}'.format(filename))
            data[index, 0] = filename[:7].replace('-','')
            data[index, 1] = df[df.gender=='M'].size
            data[index, 2] = df[df.gender=='F'].size
            index += 1
    data = data[data[:,0].argsort()] # sorts data so smallest dates are first
    return data

def makeBarGraph(data):
    N = data[:,0].size
    Males = data[:,1]

    fig, ax = plt.subplots()

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35         # the width of the bars
    p1 = ax.bar(ind, Males, width, color='#66C3FF')
    # p1 = ax.bar(ind, Males, width)


    Females = data[:,2]
    p2 = ax.bar(ind + width, Females, width,
                color='#E56399')
    # p2 = ax.bar(ind + width, Females, width)

    ax.set_title("Monthly articles by writer's gender")
    ax.set_xticks(ind + width / 2)

    strDates = [str(date) for date in data[:,0]]
    strDates = [date[:4] if int(date[4:]) is 1 else '' for date in strDates]

    ax.set_xticklabels(strDates)

    ax.legend((p1[0], p2[0]), ('Males', 'Females'))
    ax.autoscale_view()
    ax.grid(False)
    plt.show()

if __name__ == "__main__":
    makeBarGraph(getGenderByMonth())
