"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class EmailRouterSendEmailRequest:
    request_body: bytes = dataclasses.field(metadata={'request': { 'media_type': '*/*' }})
    r"""The Email Message"""
    x_sub_account_api_key: str = dataclasses.field(metadata={'header': { 'field_name': 'X-SubAccount-ApiKey', 'style': 'simple', 'explode': False }})
    r"""Sub-Account API Key"""
    x_send_post_mock_email: Optional[bool] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-SendPost-Mock-Email', 'style': 'simple', 'explode': False }})
    r"""Mock email header"""
    x_send_post_mock_time_shift: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-SendPost-Mock-Time-Shift', 'style': 'simple', 'explode': False }})
    r"""Mock email time shift"""
    



@dataclasses.dataclass
class EmailRouterSendEmailResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    body: Optional[bytes] = dataclasses.field(default=None)
    

