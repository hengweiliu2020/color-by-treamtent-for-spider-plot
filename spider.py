# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

df = pd.read_sas('adtr.sas7bdat')
df=df.assign(ADY2=df['ady']/7)
df.set_index('ADY2',inplace=True)

print(df)

df2=df[ (df['paramcd']==b'SUMDIAM') & (df['trt01p']==b'trt1')]
df3=df[ (df['paramcd']==b'SUMDIAM') & (df['trt01p']==b'trt2')]
df4=df[ (df['paramcd']==b'SUMDIAM') & (df['trt01p']==b'trt3')]

df2.groupby('subjid')['pchg'].plot(color='red', marker='o')
df3.groupby('subjid')['pchg'].plot(color='green', marker='o')
df4.groupby('subjid')['pchg'].plot(color='blue', marker='o')

plt.title('Spider Plot', fontsize=9)
plt.xlabel('Treatment Duration (weeks)', fontsize=9)
plt.ylabel('Percent Change from Baseline in Sum of Diameters', fontsize=9)

red_patch = mpatches.Patch(color='red', label='trt1')
green_patch = mpatches.Patch(color='green', label='trt2')
blue_patch = mpatches.Patch(color='blue', label='trt3')

plt.legend(handles=[red_patch, green_patch, blue_patch])
plt.grid(True)
plt.show()
