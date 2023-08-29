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
    
    def hist(df):
        missing_values = dataf.isnull().sum()
        missing_values.plot(kind='bar')
        plt.title('Missing Values per Column')
        plt.ylabel('Number of Missing Values')
        plt.xlabel('Columns')
        plt.show()
