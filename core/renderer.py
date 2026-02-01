from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from core.util import get_filepath_template


def render_project(project_dir: Path, data: dict):
    template_dir = project_dir / "templates"
    if not template_dir.exists():
        template_dir = project_dir

    output_dir = project_dir / "output"

    if not output_dir.exists():
        output_dir.mkdir()

    env = Environment(loader=FileSystemLoader(str(template_dir)))

    templates = get_filepath_template(template_dir)
    for t in templates:
        print(f"Rendering template: {t.name}", end="\t")
        template = env.get_template(t.name)
        html = template.render(**data)

        with open(output_dir / t.stem, "w", encoding="utf-8") as f:
            f.write(html)
        print("✔")

    print("✅ All files generated")
