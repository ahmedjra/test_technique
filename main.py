from preprocessing import preprocessing
from evaluation import evaluation
import os

if __name__ == "__main__":
    preprocessing = preprocessing()
    for name in os.listdir("/home/octopus/Downloads/test_technique_stage_NLP-OCR-20230727T133531Z-001/test_technique_stage_NLP-OCR/test"):
        preprocessing.main(name)
        evaluation.main(name)
