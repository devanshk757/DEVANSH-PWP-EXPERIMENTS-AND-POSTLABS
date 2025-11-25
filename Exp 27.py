import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sns.set(style="white")
# # Generate a random univariate dataset
# rs = np.random.RandomState(10)
# d = rs.normal(size=100)
# # Plot a simple histogram and kde
# sns.histplot(d, kde=True, color="m")
# plt.show()

# sns.set(style="dark")
# fmri = sns.load_dataset("fmri")
# # Plot the responses for different\
# # events and regions
# sns.lineplot(x="timepoint",
#              y="signal",
#              hue="region",
#              style="event",
#              data=fmri)
# plt.show()

# sns.set(style="ticks")
# # Loading the dataset
# df = sns.load_dataset("anscombe")
# # Show the results of a linear regression
# sns.lmplot(x="x", y="y", data=df)
# plt.show()


#---------------------------------------------------------------POST-LAB---------------------------------------------------------------
#1.
# initialise data of lists
# data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
#         'Age':[ 30 , 21 , 29 , 28 ]}
# df = pd.DataFrame( data )
# sns.boxplot( data['Age'] )
# plt.show()

#2.
# initialise data of lists
# data = {'Name':[ 'Mohe' , 'Karnal' , 'Yrik' , 'jack' ],
#         'Age':[ 30 , 21 , 29 , 28 ]}
# df = pd.DataFrame( data )
# sns.violinplot(data['Age'])
# plt.show()
