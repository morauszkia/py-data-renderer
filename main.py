import sys
from core.util import get_project_name, get_project_dir
from core.data_loader import load_table
from core.transformer import load_transformer
from core.renderer import render_project


def main():
    try:
        project_name = get_project_name()
        project_dir = get_project_dir(project_name)
        transformer = load_transformer(project_dir)

        data = load_table(project_dir)
        transformed_data = transformer(data)
        render_project(project_dir, transformed_data)

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
