import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt


grades = np.array([4, 6, 8, 10, 11, 12, 14, 99])

print("MEAN: ", np.mean(grades)) #media
print("MEDIAN: ", np.median(grades)) #mediana
print("MAX: ", np.max(grades)) #maximo
print("MAX: ", np.std(grades))
print("MAX: ", np.percentile(grades, 50))
print("MODE: ", st.mode(grades)) #maximo


plt.scatter([0,1,2,3],[1,2,3,4])
plt.show()