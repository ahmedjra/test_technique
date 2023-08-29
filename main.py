from preprocessing import preprocessing
from evaluation import evaluation
import argparse
import os

if __name__ == "__main__":
    preprocessing = preprocessing()
    evaluation = evaluation()
    parser = argparse.ArgumentParser(description="Path for preprocessing.")
    parser.add_argument("path", type=str, help="Path to the directory to be processed.")
    args = parser.parse_args()
    preprocessing.main(args.path)
    output_data = preprocessing.data
    output_data.to_csv("output.csv", index=True)
