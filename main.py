import sys
from pathlib import Path
from core.data_loader import load_table


ROOT_DIR = Path(__file__).parent
PROJECTS_DIR = ROOT_DIR / "projects"


def get_project_name() -> str:
    args = sys.argv[1:]
    if len(args) != 1:
        raise RuntimeError("Usage: python main.py <project_name>")

    return args[0]


def get_filepath(project_name: str) -> Path:
    project_dir = PROJECTS_DIR / project_name
    if not project_dir.exists() or not project_dir.is_dir():
        raise ValueError(f"Error: Project '{project_name}' does not exist.")

    data_files = list(project_dir.glob("data.*"))

    if len(data_files) == 0:
        raise FileNotFoundError(
            f"Error: Data file for project '{project_name}' not found. \
Please provide a data.xlsx or data.csv file"
        )

    if len(data_files) > 1:
        print("Multiple data files found. Please choose on of the following:")
        for idx, file in enumerate(data_files):
            print(f"{idx + 1}: {file.name}")
        choice = int(input("Enter your choice: ")) - 1
        if choice < 0 or choice >= len(data_files):
            raise ValueError("Invalid choice.")
        return project_dir / data_files[choice]

    return project_dir / data_files[0]


def main():
    try:
        project_name = get_project_name()
        filepath = get_filepath(project_name)
        data = load_table(filepath)
        print(data.head())

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
