from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from core.util import get_filepath_template


def render_project(project_dir: Path, data: dict):
    env = Environment(loader=FileSystemLoader(str(project_dir)))

    templates = get_filepath_template(project_dir)
    for t in templates:
        print(f"Rendering template: {t.name}")
        template = env.get_template(t)
        html = template.render(**data)

        with open(t.stem, "w", encoding="utf-8") as f:
            f.write(html)
            print(f"{t.stem} generated")
