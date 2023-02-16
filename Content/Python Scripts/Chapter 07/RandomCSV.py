import numpy as np

data = np.random.rand(100,10)
np.savetxt("CSVData.csv",data,delimiter=',')