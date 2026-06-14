# Data dictionary — FIFA World Cup 2026 Base Camps

## Source

All base camp data is sourced from official FIFA announcements and confirmed
reporting from U.S. Soccer, Sports Illustrated, RotoWire, and FOX Sports.
Data reflects confirmed assignments as of June 10–11, 2026.

---

## File: wc2026_base_camps_raw.csv

| Field | Type | Description | Example |
|---|---|---|---|
| `Team` | string | Full national team name | Argentina |
| `Flag` | string | Unicode emoji flag | 🇦🇷 |
| `Confederation` | categorical | FIFA continental confederation | CONMEBOL |
| `Group` | categorical | World Cup group stage group (A–L) | J |
| `FIFA_Rank` | integer | Official FIFA Men's World Ranking, June 11 2026 update | 1 |
| `Host_Country` | categorical | Which of the 3 host nations the base camp is in | USA |
| `Base_Camp_City` | string | City name of the training base | Kansas City |
| `Base_Camp_State_Region` | string | U.S. state, Canadian province, or Mexican state | Kansas |
| `Training_Facility` | string | Name of the specific training facility used | Sporting KC Training Center |
| `Latitude` | float | WGS84 decimal latitude of the facility | 39.0997 |
| `Longitude` | float | WGS84 decimal longitude of the facility | -94.5786 |
| `World_Cup_Debut` | boolean | Whether this is the team's first-ever World Cup appearance | No |
| `Host_Nation` | boolean | Whether this team is one of the 3 co-host nations | No |

---

## Confederation codes

| Code | Full name | Region | Teams in 2026 |
|---|---|---|---|
| UEFA | Union of European Football Associations | Europe | 16 |
| CAF | Confederation of African Football | Africa | 10 |
| AFC | Asian Football Confederation | Asia | 9 |
| CONMEBOL | South American Football Confederation | South America | 6 |
| CONCACAF | Confederation of North/Central America & Caribbean | North/Central America & Caribbean | 6 |
| OFC | Oceania Football Confederation | Oceania | 1 |

---

## Host country distribution

| Host_Country | Teams | % of total |
|---|---|---|
| USA | 39 | 81.25% |
| Mexico | 7 | 14.58% |
| Canada | 2 | 4.17% |

---

## Notable data notes

- **Iran** originally confirmed Tucson, AZ (USA) as its base camp, then
  switched to Tijuana, Mexico (Centro Xoloitzcuintle) in late May 2026
  due to visa logistics and geopolitical tensions.
- **Colombia and South Korea** share Zapopan (Guadalajara metro area)
  as a base camp city but use different facilities.
- **Argentina, England, and Netherlands** are all in the Kansas City
  metro area but at separate facilities.
- Coordinates represent the approximate location of the training facility,
  not the team hotel (which in some cases differs).
- **Debut nations** (first-ever World Cup appearance): Cape Verde, Curaçao,
  Jordan, Uzbekistan.
