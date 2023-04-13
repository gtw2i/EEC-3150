import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# generate the data
nPts  = 100
a     = -1
b     = 1

slope = 2
inter = 1
std   = 0.1

x     = np.linspace(a,b,nPts)
y     = slope*x + inter
y     += np.random.normal(0,std,nPts)

X = x[:,np.newaxis]

# plot the data
fig = plt.figure(figsize=(6,6))
plt.plot(x,y,'.')
plt.xlabel("area (ft^2)")
plt.ylabel("price ($)")

# model the data

model = LinearRegression(fit_intercept=True)

model.fit(X, y)

coef = model.coef_
slope_pred = coef[0]
inter_pred = model.intercept_

print(slope,inter)
print(slope_pred,inter_pred)

# plot the model predictions
y_pred = model.predict(X)

plt.plot(x,y_pred,'r')




