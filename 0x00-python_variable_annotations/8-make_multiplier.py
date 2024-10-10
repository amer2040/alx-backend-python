#!/usr/bin/env python3
""" Mod doc """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """def doc"""

    def mult(m: float) -> float:
        """def doc"""
        return m * multiplier

    return mult
