## IRIS DATASET ##

import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

#read the dataset
data = pandas.read_csv('iris.data')
print('\nColumn Names\n')
print(data)

#label encore the target variable
encode = LabelEncoder()
data.Species = encode.fit_transform(data.Species)

#train-test-split
train, test = train_test_split(data, test_size = 0.2, random_state = 0)

print('Shape of training data : ', train.shape)
print('Shape of testing data : ', test.shape)

#seperate the target and independent variable
train_x = train.drop(columns = ['Species'], axis = 1)
train_y = train['Species']

test_x = test.drop(columns = ['Species'], axis = 1)
test_y = test['Species']

#create de object of the model
model = LogisticRegression(solver='lbfgs', multi_class='auto')

model.fit(train_x, train_y)

predict = model.predict(test_x)

print('Predicted Values on Test Data', encode.inverse_transform(predict))

print('\nAccuracy Score on test data :\n')
print(accuracy_score(test_y, predict))
