from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("../train_data.csv")
    mlp_accuracy = pd.DataFrame(columns=['hidden_layer_size_X', 'hidden_layer_size_Y', 'alpha', 'activation', 'solver'])
    X_train, X_test, y_train, y_test = train_test_split(data[["base64SD/len", "strings_min_4"]].to_numpy(),
                                                        data["isEncrypted"].to_numpy(), test_size=0.33, random_state=42)
    for solver_ in range(0, 3):
        if solver_ == 0:
            solver = "lbfgs"
        elif solver_ == 1:
            solver = "sgd"
        elif solver_ == 2:
            solver = "adam"
        for activation_ in range(0, 4):
            if activation_ == 0:
                activation = 'identity'
            elif activation_ == 1:
                activation = "logistic"
            elif activation_ == 2:
                activation = "tanh"
            elif activation_ == 3:
                activation = "relu"
            for i in range(0, 11):
                alpha_ = .1*i
                for hidden_X in range(1, 5):
                    for hidden_Y in range(1, 5):
                        my_classifierMLP = MLPClassifier(hidden_layer_sizes=(hidden_X, hidden_Y), activation=activation,
                                                         solver=solver, alpha=alpha_).fit(X_train.reshape(-1, 2),
                                                                                          y_train)
                        mlp_accuracy.append({'hidden_layer_size_X': hidden_X, 'hidden_layer_size_Y': hidden_Y,
                                             'alpha': alpha_, 'solver': solver, 'activation': activation},
                                            ignore_index=True)
    mlp_accuracy.to_csv("neural_net_data")

