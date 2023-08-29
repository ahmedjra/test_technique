import seaborn as sns
import matplotlib.pyplot as plt


class evaluation:
    def __init__(self) -> None:
        pass

    def column_completeness(df):
        total_rows = len(df)

        completeness = {}
        for column in df.columns:
            non_missing_rows = df[column].count()
            completeness[column] = (non_missing_rows / total_rows) * 100

        return completeness
