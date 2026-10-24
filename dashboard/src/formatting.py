from __future__ import annotations

import math

EMPTY = "N/A"


def _is_missing(value) -> bool:
    if value is None:
        return True
    try:
        return math.isnan(float(value))
    except (TypeError, ValueError):
        return False


def _group_id(value: float, decimals: int) -> str:
    text = f"{value:,.{decimals}f}"
    return text.replace(",", "\u00a7").replace(".", ",").replace("\u00a7", ".")


def format_rupiah(value, decimals: int = 0) -> str:
    if _is_missing(value):
        return EMPTY
    return f"Rp{_group_id(float(value), decimals)}"


def format_int(value) -> str:
    if _is_missing(value):
        return EMPTY
    return _group_id(float(value), 0)


def format_percent(value, decimals: int = 2) -> str:
    if _is_missing(value):
        return EMPTY
    return f"{_group_id(float(value) * 100, decimals)}%"
