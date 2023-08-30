import matplotlib.pyplot as plt


class evaluation:
    def __init__(self) -> None:
        pass

    def column_completeness(self, df):
        total_rows = len(df)

        completeness = {}
        for column in df.columns:
            non_missing_rows = df[column].count()
            completeness[column] = (non_missing_rows / total_rows) * 100

        return completeness

    def hist(self, df):
        missing_values = df.isnull().sum()
        missing_values.plot(kind="bar")
        plt.title("Missing Values per Column")
        plt.ylabel("Number of Missing Values")
        plt.xlabel("Columns")
        plt.savefig("Missing_values.png")

    def main(self, data):
        completeness = self.column_completeness(data)
        print(completeness)  # Print the completeness data
        self.hist(data)
