from dataProcessing import create_dataframe
import sklearn
import pandas as pd
from ml import neural_net_binary_classifier

def main():
    #r"G:\ML"
    create_dataframe.create_dataframe(r"./test_data")
    data = pd.read_csv("test_data.csv")
    #neural_net_binary_classifier.classify(data)

if __name__ == "__main__":
    main()