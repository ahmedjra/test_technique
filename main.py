from preprocessing import preprocessing
from evaluation import evaluation

if __name__ == "__main__":
    preprocessing = preprocessing()
    for name in os:
        preprocessing.main(name)
        evaluation.main(name)
