from pathlib import Path
import yaml

class Config:
    # raiz del proyecto
    ROOT_DIR = Path(__file__).parent.parent
    CONFIG_DIR = ROOT_DIR / "config"

    @classmethod
    def get_paths(cls):
        with open(cls.CONFIG_DIR / "paths_config.yaml", "r") as f:
            return yaml.safe_load(f)

    @classmethod
    def get_params(cls):
        with open(cls.CONFIG_DIR / "config.yaml", "r") as f:
            return yaml.safe_load(f)