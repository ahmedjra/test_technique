from datetime import datetime
import pandas as pd
import numpy as np
import os


class preprocessing:
    def __init__(self) -> None:
        self.data = pd.DataFrame(
            columns=[
                "Fichier",
                "Nom",
                "Adresse",
                "TEL",
                "FAX",
                "Date",
                "Heure",
                "Type",
                "Quantité",
                "Plaque",
            ]
        )

    def extract_date(self, chemin, element):
        """
        function to extract date
        parameters:
            element: name of the file
        Returns:
                datetime of the file
        """
        file_path = os.path.join(chemin, element)
        data = pd.read_csv(file_path, sep=";", skipinitialspace=True)

        if element.startswith("doc"):
            indices = data.index[data["content"].isin(["PESEE"])].tolist()
            if len(indices) == 0:
                print(f" 0 'PESEE' trouvé {element}")
                return None
            if len(indices) == 1:
                print(f" 1 'PESEE' trouvé {element}")
                return datetime.strptime(
                    data.loc[indices[0] + 3, "content"], "%Y-%m-%d"
                )
            return (
                datetime.strptime(data.loc[indices[0] + 3, "content"], "%Y-%m-%d"),
                datetime.strptime(data.loc[indices[1] + 3, "content"], "%Y-%m-%d"),
            )

        return None

    def extract_heure(self, chemin, element):
        """
        function to extract heure
        parameters:
            element: name of the file
        Returns:
                time of the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["PESEE"])].tolist()

            if len(indices) == 0:
                print(f" 0 'PESEE' trouvé {element}")
                return None

            if len(indices) == 1:
                print(f" 1 'PESEE' trouvé {element}")
                return data.loc[indices[0] + 4, "content"]

            return (
                datetime.strptime(
                    data.loc[indices[0] + 4, "content"], "%H:%M:%S"
                ).time(),
                datetime.strptime(
                    data.loc[indices[1] + 4, "content"], "%H:%M:%S"
                ).time(),
            )
        return None

    def extract_quant(self, chemin, element):
        """
        function to extract quantity
        parameters:
            element: name of the file
        Returns:
                quantity of products in the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin + element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["POIDS", "TICKET"])].tolist()

            results = []

            for indice in indices:
                if data.loc[indice, "content"] == "TICKET":
                    listequant = (
                        data.loc[indice + 11, "content"],
                        data.loc[indice + 16, "content"],
                        data.loc[indice + 20, "content"],
                    )
                    return [
                        (listequant[0], "KG"),
                        (listequant[1], "KG"),
                        (listequant[2], "KG"),
                    ]
                else:
                    value = data.loc[indice + 2, "content"]
                    results.append((value, "KG"))
            return results

        return None

    def extract_plaque(self, chemin, element):
        """
        function to extract vehicule number
        parameters:
            element: name of the file
        Returns:
                vehicule number in the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[
                data["content"].isin(["VEHICULE", "VEHICULE:", "REMORQUE"])
            ].tolist()
            for indice in indices:
                return data.loc[indice + 2, "content"]

    def extract_type(self, chemin, element):
        """
        function to extract type of products
        parameters:
            element: name of the file
        Returns:
                types of products in the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["PRODUIT"])].tolist()

            for indice in indices:
                if data.loc[indice + 2, "content"] == "TER":
                    info = [
                        "1",
                        data.loc[indice + 4, "content"],
                        "2",
                        data.loc[indice + 5, "content"],
                    ]
                    return f"{info[0]}-{info[1]},{info[2]}-{info[3]}"
                else:
                    info = [
                        "1",
                        data.loc[indice + 2, "content"],
                        "2",
                        data.loc[indice + 3, "content"],
                    ]
                    if np.isnan(data.loc[indice + 3, "content"]):
                        return f"-{info[1]}"
                    else:
                        return f"{info[0]}-{info[1]},{info[2]}-{info[3]}"
        return None

    def extract_tel(self, chemin, element):
        """
        function to extract tel
        parameters:
            element: name of the file
        Returns:
                phone number in the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["TEL", "TEL:"])].tolist()

            for indice in indices:
                if data.loc[indice, "content"] == "TEL":
                    value = data.loc[indice + 2, "content"]
                    return value
                else:
                    value = data.loc[indice + 1, "content"]
                    return value
        return None

    def extract_fax(self, chemin, element):
        """
        function to extract fax
        parameters:
            element: name of the file
        Returns:
                fax of the file
        """

        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["FAX"])].tolist()

            for indice in indices:
                data.loc[indice, "content"] == "FAX"
                value = data.loc[indice + 2, "content"]
                return value

    def extract_name(self, chemin, element):
        """
        function to extract name
        parameters:
            element: name of the file
        Returns:
                name mentionned in the file
        """

        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            value = data.loc[0, "content"]
            return value

    def extract_adr(self, chemin, element):
        """
        function to extract adress
        parameters:
            element: name of the file
        Returns:
                adress mentionned in the file
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            value = []
            indices = data.index[data["content"].isin(["TEL", "TEL:"])].tolist()

            for indice in indices:
                if data.loc[indice, "content"] == "TEL":
                    for index in range(1, indice - 1):
                        value.append(data.loc[index, "content"])
                else:
                    for index in range(1, indice):
                        value.append(data.loc[index, "content"])

            # Filter out NaN values
            values = [
                x
                for x in value
                if not (isinstance(x, (float, np.float64, np.float32)) and np.isnan(x))
            ]

            # Ensure you don't reference indices that don't exist
            return_string = ""
            if len(values) >= 4:
                return_string = f"{values[0]},{values[1]},{values[2]},{values[3]},{values[4]},{values[5]}"
            elif len(values) == 3:
                return_string = f"{values[0]},{values[1]},{values[2]}"
            elif len(values) == 2:
                return_string = f"{values[0]},{values[1]}"
            elif len(values) == 1:
                return_string = f"{values[0]}"

            return return_string

        def main(self, chemin):
            for element in os.listdir("/gdrive/MyDrive/data/test/"):
                self.data.loc[len(self.data["Fichier"])] = [
                    element,
                    self.extract_name(chemin, element),
                    self.extract_adr(chemin, element),
                    self.extract_tel(chemin, element),
                    self.extract_fax(chemin, element),
                    self.extract_date(chemin, element),
                    self.extract_heure(chemin, element),
                    self.extract_type(chemin, element),
                    self.extract_quant(chemin, element),
                    self.extract_plaque(chemin, element),
                ]
