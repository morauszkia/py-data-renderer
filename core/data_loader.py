import pandas as pd
from core.util import get_filepath_data
from pathlib import Path


def load_table(project_dir: Path) -> pd.DataFrame:
    """
    Loads CSV or XLSX and returns a list of dicts.

    - Autodetects format based on extension
    - Treats first row as headers

    Args:
        file_path (Path): path to input file

    Returns:
        List[Dict[str, Any]]: _description_
    """
    file_path = get_filepath_data(project_dir)
    if file_path.suffix == ".csv":
        print("Loading CSV file...")
        df = pd.read_csv(file_path, encoding="utf-8")
        print(f"File: {file_path} loaded successfully")
        return df
    elif file_path.suffix in [".xls", ".xlsx"]:
        print("Loading Excel file...")
        df = pd.read_excel(file_path)
        print(f"File: {file_path} loaded successfully")
        return df
    else:
        raise ValueError("Unsupported file format")
