#!/usr/bin/env python3
""" Mod doc """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """def doc"""
    if lst:
        return lst[0]
    else:
        return None
