import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns

plt.style.use("dark_background")

# generate data
X, y = make_blobs(n_samples=10,
                  centers=3,
                  cluster_std=2)#,
                  #random_state=0)

X -= np.mean(X,axis=0)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3)#,
                                                    #random_state=0)

# train model

nNeigh = 1

model = KNeighborsClassifier(n_neighbors=nNeigh)
model.fit(X_train, y_train)

# test model

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)
print("Accuracy:", accuracy)

# Plot the training data, test data, and decision boundary

MAX = np.max(np.abs(X))

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,12))
axes = axes.flatten()

markersize = 100
cmap = "RdBu"

axes[0].scatter(X[:,0],X[:,1],c=y,s=markersize,cmap=cmap)
axes[0].set_xlabel("x1")
axes[0].set_ylabel("x2")
axes[0].set_xlim(-MAX,MAX)
axes[0].set_ylim(-MAX,MAX)
axes[0].set_title("Full Data")

axes[1].scatter(X_train[:,0],X_train[:,1],c=y_train,s=markersize,cmap=cmap)
axes[1].set_xlabel("x1")
axes[1].set_ylabel("x2")
axes[1].set_xlim(-MAX,MAX)
axes[1].set_ylim(-MAX,MAX)
axes[1].set_title("Train Data")

axes[2].scatter(X_test[:,0],X_test[:,1],c=y_test,s=markersize,cmap=cmap,label='true')
axes[2].scatter(X_test[:,0],X_test[:,1],c=y_pred,s=markersize*3,cmap=cmap,marker="x",label='pred')
axes[2].set_xlabel("x1")
axes[2].set_ylabel("x2")
axes[2].set_xlim(-MAX,MAX)
axes[2].set_ylim(-MAX,MAX)
axes[2].set_title("Test / Pred")
axes[2].legend()

nGrid = 100
a1 = np.linspace(-MAX,MAX,nGrid)
a2 = np.linspace(-MAX,MAX,nGrid)

A1, A2 = np.meshgrid(a1,a2)
A1 = A1.flatten()
A2 = A2.flatten()
A = np.vstack((A1,A2)).T

B = model.predict(A)
B = B.reshape(nGrid,nGrid)
B = np.flipud(B)

extent = [-MAX,MAX,-MAX,MAX]

axes[1].imshow(B, interpolation='none', extent=extent,cmap=cmap, alpha=0.5)
#axes[3].grid(True)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, ax=axes[3])



plt.tight_layout()