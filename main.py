from dataProcessing import create_dataframe
import sklearn
import pandas as pd
from ml import neural_net_binary_classifier

def main():
    #r"G:\ML"
    #r"./test_data"
    #create_dataframe.create_dataframe(r"G:\ML")
    data = pd.read_csv("train_data.csv", header=0)
    neural_net_binary_classifier.classify(data)

if __name__ == "__main__":
    main()