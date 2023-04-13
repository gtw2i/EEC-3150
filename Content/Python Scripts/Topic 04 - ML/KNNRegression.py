import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

plt.style.use("dark_background")

def f(x):
    return np.sin(2*np.pi*x)
# end

# create some data

a = -1
b = 1

n_train = 20
n_test  = 1000

# train data
x_train = np.linspace(a,b,n_train)
X_train = x_train[:,np.newaxis]
y_train = f(x_train)

# test data
x_test = np.linspace(a,b,n_test)
X_test = x_test[:,np.newaxis]
y_test = f(x_test)

# train the model

nNeigh = 2
#model = KNeighborsRegressor(n_neighbors=nNeigh,weights='uniform')
model = KNeighborsRegressor(n_neighbors=nNeigh,weights='distance')
model.fit(X_train,y_train)

# test the model

y_pred = model.predict(X_test)

r2 = r2_score(y_test,y_pred)
print(r2)
MSE = mean_squared_error(y_test,y_pred)
print(MSE)

# plot the results

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(4,8))

axes[0].plot(x_test,y_test,'g',linewidth=1)
axes[0].plot(x_test,y_pred,'r--',linewidth=1)
axes[0].plot(x_train,y_train,'b.',markersize=10)
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

MAX = max(np.max(abs(y_test)),np.max(abs(y_pred)))

axes[1].plot(y_test,y_pred,'r.',markersize=2)
axes[1].plot([-MAX,MAX],[-MAX,MAX],'b',linewidth=2)
axes[1].set_xlabel("test")
axes[1].set_ylabel("pred")

plt.tight_layout()





