from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
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
        print(f"files: {files}")
        for file_ in files:
            path = os.path.join(root, file_)
            try:
                data_file = open(path, "rb")
                data = data_file.read()
                encoded_string = base64.b64encode(data)
                num_set = []
                for i in range(0, len(BASE64)):
                    count_ = encoded_string.count(BASE64[i])
                    num_set.append(count_)
                sd = np.std(num_set)
                strings_len = strings.strings(str(data))
                if len(encoded_string) == 0:
                    temp = 1
                else:
                    temp = len(encoded_string)
                test_data = test_data.append(
                    {'filename': path, "base64SD/len": sd / temp, "strings_min_4": strings_len}, ignore_index=True)
            except Exception as inst:
                print(type(inst))
                pass
            else:
                data_file.close()
        for index, row in test_data.iterrows():
            row_ = row.to_frame()
            decision = decision_tree_model.predict(row_[["base64SD/len", "strings_min_4"]])
            print(f"{row['filename']}: {'ENCRYPTED' if decision else 'UNENCRYPTED'}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Enter an argument")
    else:
        main()
