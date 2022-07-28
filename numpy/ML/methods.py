import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt


grades = np.array([56, 34, 88, 98, 65, 76])

print("MEAN: ", np.mean(grades)) #media
print("MEDIAN: ", np.median(grades)) #mediana
print("MAX: ", np.max(grades)) #maximo
print("MAX: ", np.std(grades))
print("MAX: ", np.percentile(grades, 50))
print("MODE: ", st.mode(grades)) #maximo


# plt.scatter([0,1,2,3],[1,2,3,4]) #X and Y axis
plt.scatter([0,20,40,60,80,100],grades) #X and Y must be the same size
plt.show()