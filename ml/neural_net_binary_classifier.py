from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

def classify(data):
    X_train, X_test, y_train, y_test = train_test_split(data[["base64SD/len", "strings_min_4"]].to_numpy(), data["isEncrypted"].to_numpy(), test_size=0.33, random_state=42)

    my_classifierMLP = MLPClassifier().fit(X_train.reshape(-1, 2), y_train)
    print(f"MLP: {my_classifierMLP.score(X_test.reshape(-1, 2), y_test)}")

    my_classifierKNeighbor = KNeighborsClassifier().fit(X_train.reshape(-1, 2), y_train)
    print(f"K Neighbors: {my_classifierKNeighbor.score(X_test.reshape(-1, 2), y_test)}")

    my_classifierSVC = SVC().fit(X_train.reshape(-1, 2), y_train)
    print(f"SVC: {my_classifierSVC.score(X_test.reshape(-1, 2), y_test)}")

    my_classifierTree = DecisionTreeClassifier().fit(X_train.reshape(-1, 2), y_train)
    print(f"Decision Tree: {my_classifierTree.score(X_test.reshape(-1, 2), y_test)}")
