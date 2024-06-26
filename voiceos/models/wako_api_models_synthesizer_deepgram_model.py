# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WakoApiModelsSynthesizerDeepgramModel(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    AURA_MINUS_ASTERIA_MINUS_EN = 'aura-asteria-en'
    AURA_MINUS_LUNA_MINUS_EN = 'aura-luna-en'
    AURA_MINUS_STELLA_MINUS_EN = 'aura-stella-en'
    AURA_MINUS_ATHENA_MINUS_EN = 'aura-athena-en'
    AURA_MINUS_HERA_MINUS_EN = 'aura-hera-en'
    AURA_MINUS_ORION_MINUS_EN = 'aura-orion-en'
    AURA_MINUS_ARCAS_MINUS_EN = 'aura-arcas-en'
    AURA_MINUS_PERSEUS_MINUS_EN = 'aura-perseus-en'
    AURA_MINUS_ANGUS_MINUS_EN = 'aura-angus-en'
    AURA_MINUS_ORPHEUS_MINUS_EN = 'aura-orpheus-en'
    AURA_MINUS_HELIOS_MINUS_EN = 'aura-helios-en'
    AURA_MINUS_ZEUS_MINUS_EN = 'aura-zeus-en'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WakoApiModelsSynthesizerDeepgramModel from a JSON string"""
        return cls(json.loads(json_str))


