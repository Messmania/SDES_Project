import numpy as np
import matplotlib.pyplot as plt


#Sample data
florida = [48, 35, 30, 35]
virginia = [35, 32, 34, 20]
california=[40,20,25,10]

def plotDayWiseScore(florida,virginia,california):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ## the data
    N = 4
    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.15                      # the width of the bars


    ## the bars
    rects1 = ax.bar(ind, florida, width,color=(0.1,0.749,1))

    rects2 = ax.bar(ind+width, virginia, width,color='orange')

    rects3 = ax.bar(ind+width+width, california, width,color='green')

    # axes and labels
    ax.set_xlim(-3*width,len(ind)+4*width,3*width)
    ax.set_ylim(0,55)
    ax.set_ylabel('Scores')
    ax.set_title('Happiness score of states, time wise')
    xTickMarks = ['Morning','Afternoon','Evening','Night']
    ax.set_xticks(ind+width+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=0, fontsize=12)

    #ax.legend( (rects1[0], rects2[0],rects3[0]), ('Florida', 'Virginia','California'))

    plt.show()


if __name__=='__main__':
    plotDayWiseScore(florida,virginia,california)
