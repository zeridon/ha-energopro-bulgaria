# Copyright (c) 2026 @Zeridon
# SPDX-License-Identifier: MIT

"""Tests for ENERGOPRO tariff calculation."""

from datetime import datetime
from zoneinfo import ZoneInfo

from custom_components.energopro.const import TARIFF_DAY, TARIFF_NIGHT
from custom_components.energopro.sensor import get_current_tariff

TZ = ZoneInfo("Europe/Sofia")


def test_summer_day_start() -> None:
    """Summer Day tariff starts at 07:00."""
    assert get_current_tariff(datetime(2026, 4, 1, 6, 59, tzinfo=TZ)) == TARIFF_NIGHT

    assert get_current_tariff(datetime(2026, 4, 1, 7, 0, tzinfo=TZ)) == TARIFF_DAY


def test_summer_day_end() -> None:
    """Summer Day tariff ends at 23:00."""
    assert get_current_tariff(datetime(2026, 10, 31, 22, 59, tzinfo=TZ)) == TARIFF_DAY

    assert get_current_tariff(datetime(2026, 10, 31, 23, 0, tzinfo=TZ)) == TARIFF_NIGHT


def test_winter_day_start() -> None:
    """Winter Day tariff starts at 06:00."""
    assert get_current_tariff(datetime(2026, 11, 1, 5, 59, tzinfo=TZ)) == TARIFF_NIGHT

    assert get_current_tariff(datetime(2026, 11, 1, 6, 0, tzinfo=TZ)) == TARIFF_DAY


def test_winter_day_end() -> None:
    """Winter Day tariff ends at 22:00."""
    assert get_current_tariff(datetime(2026, 3, 31, 21, 59, tzinfo=TZ)) == TARIFF_DAY

    assert get_current_tariff(datetime(2026, 3, 31, 22, 0, tzinfo=TZ)) == TARIFF_NIGHT
