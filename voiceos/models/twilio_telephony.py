# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TwilioTelephony(BaseModel):
    """
    TwilioTelephony
    """ # noqa: E501
    provider: Optional[StrictStr] = Field(default='twilio', description="The telephony provider.")
    phone_number_sid: StrictStr = Field(description="The twilio phone number SID.")
    account_sid: Optional[StrictStr] = Field(default=None, description="The account sid of the telephony provider (i.e Twilio Account SID). Returns null if the phone number was purchased with Wako.")
    auth_token: Optional[StrictStr] = Field(default=None, description="The auth token of the telephony provider (i.e Twilio Auth Token). Returns null if the phone number was purchased with Wako.")
    __properties: ClassVar[List[str]] = ["provider", "phone_number_sid", "account_sid", "auth_token"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['twilio']):
            raise ValueError("must be one of enum values ('twilio')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TwilioTelephony from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TwilioTelephony from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider") if obj.get("provider") is not None else 'twilio',
            "phone_number_sid": obj.get("phone_number_sid"),
            "account_sid": obj.get("account_sid"),
            "auth_token": obj.get("auth_token")
        })
        return _obj


