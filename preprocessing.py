from datetime import datetime
import numpy as np
import pandas as pd
import os


class preprocessing:
    def __init__(self) -> None:
        """
        Constructor: Initializes an empty DataFrame with predefined columns.
        """
        self.data = pd.DataFrame(
            columns=[
                "Fichier",
                "Nom",
                "Adresse",
                "TEL",
                "FAX",
                "Date",
                "Heure",
                "Plaque",
                "Client",
                "Produit",
                "Quantité",
                "Transporteur",
            ]
        )

    def extract_date(self, chemin, element):
        """
        Extracts date(s) from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Date(s) extracted from the file or None if not found.
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
        Extracts time(s) from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Time(s) extracted from the file or None if not found.
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
        Extracts quantities from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - List of quantities and their units extracted from the file or None if not found.
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
                        (listequant[0], "KG(BRUT)"),
                        (listequant[1], "KG(TARE)"),
                        (listequant[2], "KG(NET)"),
                    ]
                else:
                    value = data.loc[indice + 2, "content"]
                    results.append((value, "KG"))
            return results

        return None

    def extract_plaque(self, chemin, element):
        """
        Extracts vehicle plate number from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Plate number or None if not found.
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
        Extracts product type from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Product type string or None if not found.
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
        Extracts phone number from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - TEL or None if not found.
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
        Extracts fax number from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Fax number or None if not found.
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
        Extracts name from the first row of a given CSV file.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Name from the file or None if not found.
        """

        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            value = data.loc[0, "content"]
            return value

    def extract_adr(self, chemin, element):
        """
        Extracts address details from a given CSV file based on specific patterns.

        Parameters:
            - chemin: Path to the directory containing the file.
            - element: Filename of the CSV file.

        Returns:
            - Address string or None if not found.
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

    def extract_client(self, chemin, element):
        """
        Extract client information from a CSV file based on certain conditions.

        Parameters:
        - chemin (str): The directory path where the file resides.
        - element (str): The name of the file to be read.

        Returns:
        - str: The extracted client information from the CSV file.
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[data["content"].isin(["CLIENT", "CLIENT:"])].tolist()

            if len(indices) <= 2:
                return data.loc[indices[0] + 2, "content"]

    def extract_trans(self, chemin, element):
        """
        Extract transporter information from a CSV file based on certain conditions.

        Parameters:
        - chemin (str): The directory path where the file resides.
        - element (str): The name of the file to be read.

        Returns:
        - str: The extracted transporter information from the CSV file.
        """
        if element.startswith("doc"):
            file_path = os.path.join(chemin, element)
            data = pd.read_csv(file_path, sep=";", skipinitialspace=True)
            indices = data.index[
                data["content"].isin(["TRANSPORTEUR", "TRANSPORTEUR:"])
            ].tolist()
            return data.loc[indices[0] + 2, "content"]

    def main(self, chemin):
        for element in os.listdir(chemin):
            self.data.loc[len(self.data["Fichier"])] = [
                element,
                self.extract_name(chemin, element),
                self.extract_adr(chemin, element),
                self.extract_tel(chemin, element),
                self.extract_fax(chemin, element),
                self.extract_date(chemin, element),
                self.extract_heure(chemin, element),
                self.extract_plaque(chemin, element),
                self.extract_client(chemin, element),
                self.extract_type(chemin, element),
                self.extract_quant(chemin, element),
                self.extract_trans(chemin, element),
            ]
