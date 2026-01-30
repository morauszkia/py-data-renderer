import importlib
import sys
from pathlib import Path


def load_transformer(project_dir: Path):
    """
    Dynamically imports def transform(df: pd.DataFrame) -> dict
    from "transformer.py" file inside project folder.

    Args:
        project_dir (Path): Path to project folder
    """
    transformer_path = project_dir / "transformer.py"

    if not transformer_path.exists():
        raise FileNotFoundError(f"File not found at '{transformer_path}'")

    spec = importlib.util.spec_from_file_location(
        "transformer", transformer_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["transformer"] = module
    spec.loader.exec_module(module)

    if not hasattr(module, "transform"):
        raise AttributeError(
            f"{transformer_path}: must define function 'transform(df)'"
        )

    print("Transformer loaded successfully!")
    return module.transform
