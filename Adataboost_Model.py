from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
# Import train_test_split function
from sklearn.model_selection import train_test_split
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
import numpy as np

def train_ada_boost(X, target, estimators = 3, random_seed = 0):
	X_train, X_test, y_train, y_test = train_test_split(X, target, random_state=random_seed)

	# Create adaboost classifer object
	abc = AdaBoostClassifier(n_estimators=estimators,
	                         random_state=random_seed)
	# Train Adaboost Classifer
	model = abc.fit(X_train, y_train)

	#Predict the response for test dataset
	y_pred = model.predict(X_test)

	print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
	return (model, X_test, y_test)

X = np.zeros(10)
#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
target = np.ones(10)
#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Z = X.reshape(-1, 1)


#train_ada_boost(Z, target)
train_ada_boost(Z, np.array([-875.,  477.,  -49., -212., -937., -931., -811.,  751., -167., -195.,]), 3, 0)
'''
[[0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]]
'''

https://www.codewars.com/kata/building-an-adaboost-model-with-sklearn-introductory-machine-learning/discuss/python
