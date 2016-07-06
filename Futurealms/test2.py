import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.datasets import load_iris
from sklearn import metrics, ensemble
from sklearn.cross_validation import train_test_split
iris=load_iris()
y = iris['target']
x = iris['data']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
model = sklearn.ensemble.GradientBoostingClassifier()
model.fit(x_train, y_train)
expected = y_test
predicted = model.predict(x_test)
print(metrics.confusion_matrix(expected, predicted))
print(model.score(x_test, y_test))