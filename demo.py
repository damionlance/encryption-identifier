from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import sys
from dataProcessing import create_dataframe


def main():
    data = pd.read_csv("train_data.csv")
    X_train, X_test, y_train, y_test = train_test_split(data[["base64SD/len", "strings_min_4"]].to_numpy(),
                                                        data["isEncrypted"].to_numpy(), test_size=0.33, random_state=42)
    decision_tree_model = DecisionTreeClassifier().fit(X_train.reshape(-1, 2), y_train)
    for item in sys.argv:
        data = create_dataframe.create_dataframe_demo(item)
        print(f"file name: {item}\nresult: {decision_tree_model.predict(data[['base64SD/len', 'strings_min_4']])}\n")


if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("Enter an argument")
    else:
        main()
