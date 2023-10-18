"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import models_copyto as shared_models_copyto
from typing import List, Optional


@dataclasses.dataclass
class ModelsToCustomFields:
    pass


@dataclasses.dataclass
class ModelsTo:
    bcc: Optional[List[shared_models_copyto.ModelsCopyTo]] = dataclasses.field(default=None)
    cc: Optional[List[shared_models_copyto.ModelsCopyTo]] = dataclasses.field(default=None)
    custom_fields: Optional[ModelsToCustomFields] = dataclasses.field(default=None)
    email: Optional[str] = dataclasses.field(default=None)
    name: Optional[str] = dataclasses.field(default=None)
    

