import sys
from pathlib import Path
from typing import List

ROOT_DIR = Path(__file__).parent.parent
PROJECTS_DIR = ROOT_DIR / "projects"


def get_project_name() -> str:
    args = sys.argv[1:]
    if len(args) != 1:
        raise RuntimeError("Usage: python main.py <project_name>")

    return args[0]


def get_project_dir(project_name: str) -> Path:
    project_dir = PROJECTS_DIR / project_name
    if not project_dir.exists() or not project_dir.is_dir():
        raise ValueError(f"Error: Project '{project_name}' does not exist.")
    return project_dir


def get_filepath_data(project_dir: Path) -> Path:
    data_files = list(project_dir.glob("data.*"))

    if len(data_files) == 0:
        raise FileNotFoundError(
            f"Error: Data file not found in {project_dir}. \
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


def get_filepath_template(dir: Path) -> List[Path]:
    template_files = list(dir.glob("*.html.j2"))

    if len(template_files) == 0:
        raise FileNotFoundError(
            f"Error: Template file not found in {dir}. \
Please provide a Jinja template file with extension '.html.j2'"
        )

    return template_files
