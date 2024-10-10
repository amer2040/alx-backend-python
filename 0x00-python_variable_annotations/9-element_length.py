#!/usr/bin/env python3
""" Mod doc """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """def doc"""
    return [(i, len(i)) for i in lst]
