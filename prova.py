import pandas as pd
import numpy as nu
data=pd.read_csv('student-mat.csv')

import seaborn as sns
import matplotlib.pyplot as plt
voti=data['G3']
b=sns.countplot(x=0, data=voti)
print(data['G3'])
b.axes.set_title('Distribution of Final grade of students', fontsize = 35)
b.set_xlabel('Final Grade', fontsize=20)
b.set_ylabel('Count', fontsize=20)
print(b)
#print(data['G3'])
plt.show()