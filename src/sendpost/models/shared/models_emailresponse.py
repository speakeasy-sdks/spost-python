"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .models_emailerrorcode import ModelsEmailErrorCode
from typing import Optional


@dataclasses.dataclass
class ModelsEmailResponse:
    error_code: Optional[ModelsEmailErrorCode] = dataclasses.field(default=None)
    message: Optional[str] = dataclasses.field(default=None)
    message_id: Optional[str] = dataclasses.field(default=None)
    submitted_at: Optional[int] = dataclasses.field(default=None)
    to: Optional[str] = dataclasses.field(default=None)
    

