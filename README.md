# ENERGOPRO Bulgaria Prices for Home Assistant

A Home Assistant custom integration that retrieves regulated electricity prices from ENERGOPRO Bulgaria.

The integration automatically determines whether the current tariff is Дневна (Day) or Нощна (Night) according to ENERGOPRO's published seasonal schedule.

# Features
 * Retrieves ENERGOPRO regulated electricity prices automatically.
 * Checks the ENERGOPRO website once every 24 hours.
 * Day and Night prices are exposed as separate sensors.
 * Prices are provided in EUR/kWh.
 * Provides prices excluding VAT and including VAT.
 * Automatically switches the current price between Day and Night.
 * Uses Home Assistant's configured timezone.
 * No helpers or automations are required.
 * Keeps the last successfully retrieved price if a later website request fails.
 * Can manually refresh prices and recalculate current tariff and price.

# Sensors

The integration creates:

| Entity | Description |
|--------|-------------|
| Day Price | Day tariff excluding VAT |
| Day Price incl VAT | Day tariff including VAT |
| Night Price | Night tariff excluding VAT |
| Night Price incl VAT | Night tariff including VAT |
| Current Price | Current tariff excluding VAT |
| Current Price incl VAT | Current tariff including VAT |
| Current Tariff | Дневна or Нощна |

Prices use EUR/kWh.

The VAT calculation uses the Bulgarian standard VAT rate of 20%.

# Tariff schedule
## April 1 – October 31
| Time | Tariff|
|------|--------|
| 07:00 – 23:00 | Дневна |
| 23:00 – 07:00 | Нощна |
## November 1 – March 31
| Time | Tariff |
|------|--------|
| 06:00 – 22:00 | Дневна |
| 22:00 – 06:00 | Нощна |

The tariff calculation is performed locally in Home Assistant. The ENERGOPRO website does not need to be contacted when the tariff changes.

# Installation with HACS

Open HACS in Home Assistant and search for:

**ENERGOPRO Bulgaria**

If the repository has not yet been added to the HACS default repository list, add it as a custom repository [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=zeridon&repository=ha-energopro-bulgaria&category=integration).

Select:

Repository type: **Integration**

Install the integration and restart Home Assistant.

Then go to:

Settings → Devices & services → Add integration

Search for:

**ENERGOPRO Bulgaria**

# Source

Electricity prices are retrieved from the ENERGOPRO Bulgaria regulated-price page:

https://energopro.bg/bg/sales/domakinstva/snabdyavane-po-regulirani-ceni/

The integration uses the final regulated electricity price including network services but excluding VAT as published by ENERGOPRO.

# Disclaimer

This is an unofficial Home Assistant integration and is not affiliated with or endorsed by ENERGOPRO Bulgaria.

Always verify electricity prices against your electricity bill and the current information published by ENERGOPRO.
