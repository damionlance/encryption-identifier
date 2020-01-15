import os
import sys
import base64
import pandas as pd
import numpy as np
from dataProcessing import strings

def create_dataframe(path):
    base64_set = [b"A", b"B", b"C", b"D", b'E', b"F", b"G", b"H", b"I", b"J", b"K", b"L", b"M", b"N", b"O", b"P", b"Q", b"R", b"S", b"T", b"U", b"V", b"W", b"X", b"Y", b"Z", b"a", b"b", b"c", b"d", b"e", b"f", b"g", b"h", b"i", b"j", b"k", b"l", b"m", b"n", b"o", b"p", b"q", b"r", b"s", b"t", b"u", b"v", b"w", b"x", b"y", b"z", b"0", b"1", b"2", b"3", b"4", b"5", b"6", b"7", b"8", b"9", b"+", b"/", b"="]
    column_names = ["filename", "base64SD/len", "strings_min_4", "isEncrypted"]  # add more, just test for now
    test_data = pd.DataFrame(columns=column_names)

    path_decrypted = os.path.join(path, "Unencrypted")
    path_encrypted = os.path.join(path, "Encrypted")

    ## Debug:
    # path_decrypted = path
    # path_encrypted = path

    count = 0

    for root, subdirs, files in os.walk(path_decrypted):
        count = 0
        for file_ in files:
            print(count / len(files))
            file_path = os.path.join(root, file_)
            try:
                data_file = open(file_path, "rb")
                data = data_file.read()
                encoded_string = base64.b64encode(data)
                num_set = []
                for i in range(0, len(base64_set)):
                    count_ = encoded_string.count(base64_set[i])
                    num_set.append(count_)
                sd = np.std(num_set)
                strings_len = strings.strings(str(data))
                test_data = test_data.append(
                    {'filename': file_, "base64SD/len": sd / len(encoded_string), "strings_min_4": strings_len,
                     "isEncrypted": False}, ignore_index=True)
            except:
                pass
            data_file.close()
            count += 1

    for root, subdirs, files in os.walk(path_encrypted):
        count = 0
        for file_ in files:
            print(count / len(files))
            file_path = os.path.join(root, file_)
            try:
                data_file = open(file_path, "rb")
                data = data_file.read()
                encoded_string = base64.b64encode(data)
                num_set = []
                for i in range(0, len(base64_set)):
                    count_ = encoded_string.count(base64_set[i])
                    num_set.append(count_)
                sd = np.std(num_set)
                strings_len = strings.strings(str(data))
                test_data = test_data.append(
                    {'filename': file_, "base64SD/len": sd / len(encoded_string), "strings_min_4": strings_len,
                    "isEncrypted": True}, ignore_index=True)
            except:
                pass
            data_file.close()
            count += 1

    test_data.to_csv("test_data.csv")
