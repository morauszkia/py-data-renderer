import pandas as pd
from pathlib import Path


def load_table(file_path: Path) -> None:
    """
    Loads CSV or XLSX and returns a list of dicts.

    - Autodetects format based on extension
    - Treats first row as headers

    Args:
        file_path (Path): path to input file

    Returns:
        List[Dict[str, Any]]: _description_
    """
    if file_path.suffix == ".csv":
        print("Loading CSV file...")
        df = pd.read_csv(file_path, encoding="utf-8")
        return df
    elif file_path.suffix in [".xls", ".xlsx"]:
        print("Loading Excel file...")
        df = pd.read_excel(file_path)
        return df
    else:
        raise ValueError("Unsupported file format")
