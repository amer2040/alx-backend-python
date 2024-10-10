#!/usr/bin/env python3
""" Mod doc """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """def doc"""
    return (k, v**2)
