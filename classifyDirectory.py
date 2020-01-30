from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from dataProcessing import create_dataframe
from dataProcessing import strings
import numpy as np
import base64
import pandas as pd
import sys
import os

BASE64 = [b"A", b"B", b"C", b"D", b'E', b"F", b"G", b"H", b"I", b"J", b"K", b"L", b"M", b"N", b"O", b"P", b"Q", b"R",
          b"S", b"T", b"U", b"V", b"W", b"X", b"Y", b"Z", b"a", b"b", b"c", b"d", b"e", b"f", b"g", b"h", b"i", b"j",
          b"k", b"l", b"m", b"n", b"o", b"p", b"q", b"r", b"s", b"t", b"u", b"v", b"w", b"x", b"y", b"z", b"0", b"1",
          b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9", b"+", b"/", b"="]

def main():
    data = pd.read_csv("train_data.csv")
    X_train, X_test, y_train, y_test = train_test_split(data[["base64SD/len", "strings_min_4"]].to_numpy(),
                                                        data["isEncrypted"].to_numpy(), test_size=0.33, random_state=42)
    decision_tree_model = DecisionTreeClassifier().fit(X_train.reshape(-1, 2), y_train)
    directory_to_inspect = sys.argv[1]
    column_names = ["filename", "base64SD/len", "strings_min_4"]
    test_data = pd.DataFrame(columns=column_names)

    for root, subdirs, files in os.walk(directory_to_inspect):
        for file_ in files:
            path = os.path.join(root, file_)
            df = create_dataframe.create_dataframe_demo(path)
            decision = decision_tree_model.predict(data[['base64SD/len', 'strings_min_4']])
            print(f"{path}: {'ENCRYPTED' if decision[0] else 'UNENCRYPTED'} \t\t\tCertainty: {decision_tree_model.predict_proba(data[['base64SD/len', 'strings_min_4']])[0][0]*100}%")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Enter an argument")
    else:
        main()
