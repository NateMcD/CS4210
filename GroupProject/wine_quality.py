#http://www3.dsi.uminho.pt/pcortez/wine/

#importing some Python libraries
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

dataSets = ['winequality-red.csv', 'winequality-white.csv']
for ds in dataSets:
    dbTraining = []
    X = []
    Y = []

    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                rowSplit = row[0].split(";")
                dbTraining.append(rowSplit)


    for row in range(len(dbTraining)):
        data = []
        for i in range(11):
            data.append(float(dbTraining[row][i]))
        X.append(data)
        Y.append(float(dbTraining[row][11]))

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    gnb = GaussianNB()
    y_pred_gnb = gnb.fit(X_train, y_train).predict(X_test)

    correct = 0
    total = 0
    for i in range(len(y_pred_gnb)):
        total += 1
        if y_pred_gnb[i] == y_test[i]:
            correct += 1

    print("Total accuracy for %s, using Naive Bayes is %.2f" % (ds, correct / total))

    knn = KNeighborsClassifier(n_neighbors=1, p=2)
    y_pred_knn = knn.fit(X_train, y_train).predict(X_test)

    correct = 0
    total = 0
    for i in range(len(y_pred_knn)):
        total += 1
        if y_pred_knn[i] == y_test[i]:
            correct += 1

    print("Total accuracy for %s, using KNN is %.2f" % (ds, correct / total))
