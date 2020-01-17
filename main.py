import pandas as pd
from ml import neural_net_binary_classifier


def main():
    data = pd.read_csv("train_data.csv", header=0)
    neural_net_binary_classifier.classify(data)


if __name__ == "__main__":
    main()
