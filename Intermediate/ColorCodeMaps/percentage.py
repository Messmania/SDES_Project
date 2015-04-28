import matplotlib.pyplot as plt
import numpy as np

popdensity = {
    'Alaska':     52,
    'New Jersey':  438.00,
    'Rhode Island':   387.35,
    'Massachusetts':   312.68,
    'Connecticut':    271.40,
    'Maryland':   209.23,
    'New York':    155.18,
    'Delaware':    154.87,
    'Florida':     114.43,
    'Ohio':  107.05,
    'Pennsylvania':  105.80,
    'Illinois':    86.27,
    'California':  83.85,
    'Hawaii':  72.83,
    'Virginia':    69.03,
    'Michigan':    67.55,
    'Indiana':    65.46,
    'North Carolina':  63.80,
    'Georgia':     54.59,
    'Tennessee':   53.29,
    'New Hampshire':   53.20,
    'South Carolina':  51.45,
    'Louisiana':   39.61,
    'Kentucky':   39.28,
    'Wisconsin':  38.13,
    'Washington':  36.20,
    'Alabama':     33.84,
    'Missouri':    39.36,
    'Texas':   30.75,
    'West Virginia':   29.00,
    'Vermont':     25.41,
    'Minnesota':  23.86,
    'Mississippi':   23.42,
    'Iowa':  20.22,
    'Arkansas':    19.82,
    'Oklahoma':    19.40,
    'Arizona':     17.43,
    'Colorado':    16.01,
    'Maine':  15.95,
    'Oregon':  13.76,
    'Kansas':  12.69,
    'Utah':  10.50,
    'Nebraska':    8.60,
    'Nevada':  7.03,
    'Idaho':   6.04,
    'New Mexico':  5.79,
    'South Dakota':  3.84,
    'North Dakota':  3.59,
    'Montana':     2.39,
    'Wyoming':      1.96
    }

def plotPercentage(percentageDict):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ## the data
    N = 50
    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.15                      # the width of the bars


    ## the bars
    ax.bar(ind, percentageDict.values(), width,color=(0.1,0.749,1))

    # axes and labels
    ax.set_xlim(-3*width,len(ind)+4*width,3*width)
    ax.set_ylim(0,445)
    ax.set_ylabel('Percentage of positive tweets')
    ax.set_title('Percentage of happiness in states')
    xTickMarks = percentageDict.keys()
    ax.set_xticks(ind+width+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=80, fontsize=8)


    plt.show()

plotPercentage(popdensity)
