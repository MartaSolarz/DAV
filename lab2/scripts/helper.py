HATCH_PATTERNS = ['/', '\\', '|', '-', '+']

COUNTRY_NAMES_A = {
    "USA": "United States",
    "CHN": "China",
    "IND": "India",
    "PAK": "Pakistan",
    "IDN": "Indonesia"
}

AREA_A = {
    "USA": 9147420,
    "CHN": 9388211,
    "IND": 2973190,
    "PAK": 770880,
    "IDN": 1811570
}

COUNTRY_NAMES_B = {
    "PER": "Peru",
    "LKA": "Sri Lanka",
    "NPL": "Nepal",
    "TZA": "Tanzania",
    "AUS": "Australia"
}

AREA_B = {
    "PER": 1280000,
    "LKA": 62710,
    "NPL": 143350,
    "TZA": 885800,
    "AUS": 7682300
}

COUNTRY_NAMES_C = {
    "POL": "Poland",
    "ARG": "Argentina",
    "COL": "Colombia",
    "TZA": "Tanzania",
    "ESP": "Spain"
}

AREA_C = {
    "POL": 306230,
    "ARG": 2736690,
    "COL": 1109500,
    "TZA": 885800,
    "ESP": 498800
}


def million_formatter(x, pos):
    return f'{int(x)}M'
