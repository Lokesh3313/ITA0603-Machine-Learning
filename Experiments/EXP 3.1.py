from sklearn.tree import DecisionTreeClassifier

X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

y = ['No','No','Yes','Yes']

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[1,0]]))
from sklearn.tree import DecisionTreeClassifier

X = [
    [0,0,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [2,1,0,0],
    [2,2,1,0],
    [2,2,1,1],
    [1,2,1,1],
    [0,1,0,0],
    [0,2,1,0],
    [2,1,1,0],
    [0,1,1,1],
    [1,1,0,1],
    [1,0,1,0],
    [2,1,0,1]
]

y = [
    'No','No','Yes','Yes','Yes','No',
    'Yes','No','Yes','Yes','Yes','Yes',
    'Yes','No'
]

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[0,2,0,0]]))
from sklearn.tree import DecisionTreeClassifier

X = [
    [2,1,1,1],
    [2,2,1,2],
    [1,1,1,1],
    [1,0,0,0],
    [0,3,0,3],
    [2,1,0,1],
    [0,0,0,0],
    [1,1,1,2],
    [2,2,1,1],
    [0,3,1,0]
]

y = [
    'Yes','Yes','Yes','No','No',
    'Yes','No','Yes','Yes','No'
]

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[2,1,1,2]]))
from sklearn.tree import DecisionTreeClassifier

X = [
    [2,2,1,1],
    [2,2,1,0],
    [1,2,1,1],
    [0,0,0,0],
    [1,1,1,0],
    [2,1,0,1],
    [0,0,0,1],
    [1,2,1,1],
    [2,2,1,1],
    [0,1,0,0]
]

y = [
    'Yes','Yes','Yes','No','Yes',
    'No','No','Yes','Yes','No'
]

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[1,2,1,1]]))
from sklearn.tree import DecisionTreeClassifier

X = [
    [1,1,1,1],
    [1,1,0,1],
    [0,1,1,0],
    [1,0,1,1],
    [0,0,0,0],
    [1,1,1,0],
    [0,1,0,1],
    [1,0,0,1],
    [1,1,1,1],
    [0,0,1,0]
]

y = [
    'Positive','Positive','Negative',
    'Positive','Negative','Positive',
    'Negative','Positive','Positive',
    'Negative'
]

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[1,1,0,1]]))
from sklearn.tree import DecisionTreeClassifier

X = [
    [2,2,1,1],
    [2,1,1,1],
    [1,1,0,1],
    [0,0,0,0],
    [1,2,1,1],
    [0,3,0,0],
    [2,1,1,0],
    [1,0,0,1],
    [2,2,1,1],
    [0,3,0,1]
]

y = [
    'Yes','Yes','Yes','No','Yes',
    'No','Yes','No','Yes','No'
]

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)

print(clf.predict([[1,1,1,1]]))
