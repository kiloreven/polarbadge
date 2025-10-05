import os
import tomllib

from pydantic import BaseModel, Field
from polarbadge.models.geekevents import GEConfig

_base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
_CONFIG_PATH = os.path.join(_base_path, "config.toml")

class GeneralConfig(BaseModel):
    output_path: str | None = None


class Config(BaseModel):
    geekevents: GEConfig | None = None
    general: GeneralConfig


def get_config():
    with open(_CONFIG_PATH, 'rb') as f:
        data = tomllib.load(f)
    return Config.model_validate(data)