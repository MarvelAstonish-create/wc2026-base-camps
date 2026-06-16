# FIFA World Cup 2026 — Team Base Camp Locations

**A data analytics and geospatial visualization project by Astonish | MEK Consult LLC**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Data: FIFA Official](https://img.shields.io/badge/Data-FIFA%20Official-blue)
![Status: Complete](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## Project overview

The 2026 FIFA World Cup is the largest in history — 48 nations, 3 host countries (USA, Mexico, Canada), 16 host cities, and 104 matches across 39 days. But the tournament's geographic footprint extends far beyond those 16 cities.

This project maps and analyzes the **official Team Base Camp (TBC) Training Sites** for all 48 qualified nations — the facilities where squads train, recover, and prepare between matches. The data reveals a rich logistics story: 39 teams in the USA, 7 in Mexico, 2 in Canada, spanning 25 communities that will never host a match but play a critical role in the tournament.

---

## Business questions answered

1. Which host country attracts the most teams to its base camps, and why?
2. How does confederation membership influence base camp geography?
3. Which U.S. cities emerge as multi-team hubs, and what does that mean economically?
4. Are higher-ranked teams choosing better-resourced facilities?
5. What was the one notable last-minute base camp switch, and what drove it?

---

## Key findings

| Insight | Detail |
|---|---|
| USA dominates | 39 of 48 teams (81%) are based in the United States |
| Kansas City is a football city | 4 teams based there: Argentina, England, Netherlands, Algeria |
| California hosts 7 | Highest state count: Australia, Qatar, Switzerland, Austria, Paraguay, New Zealand, USA |
| Mexico's 7 teams | Colombia, South Korea, Iran, Uruguay, Tunisia, South Africa, and host Mexico |
| Canada has 2 | Only Canada and Panama base there |
| Debut nations | Cape Verde, Curaçao, Jordan, Uzbekistan — all making their World Cup debut |
| Iran's last-minute switch | Moved from Tucson, AZ to Tijuana, Mexico due to visa concerns |
| 25 non-host communities | Benefit economically from hosting national teams |

---

## Repository structure

```
wc2026-base-camps/
│
├── data/
│   ├── raw/
│   │   └── wc2026_base_camps_raw.csv       # Source dataset — 48 teams, all fields
│   └── processed/
│       └── wc2026_base_camps_clean.csv     # Cleaned, analysis-ready dataset
│
├── notebooks/
│   └── wc2026_analysis.ipynb               # Python EDA: distributions, clusters, rankings
│
├── visualizations/
│   ├── wc2026_basemap.html                 # Interactive D3.js base camp map
│   └── tableau_workbook_guide.md           # Step-by-step Tableau Public build guide
│
├── docs/
│   └── data_dictionary.md                  # Field definitions and data sources
│
├── assets/
│   └── project_banner.png                  # LinkedIn/social preview image
│
├── README.md                               # This file
└── LICENSE                                 # MIT License
```

---

## Dataset fields

| Field | Description |
|---|---|
| `Team` | National team name |
| `Flag` | Emoji flag |
| `Confederation` | FIFA confederation (UEFA, CAF, AFC, CONMEBOL, CONCACAF, OFC) |
| `Group` | World Cup group (A–L) |
| `FIFA_Rank` | Official FIFA ranking as of June 11, 2026 |
| `Host_Country` | Which host country the base camp is in (USA / Mexico / Canada) |
| `Base_Camp_City` | City of the training base |
| `Base_Camp_State_Region` | State or region |
| `Training_Facility` | Name of the specific training facility |
| `Latitude` | Decimal latitude |
| `Longitude` | Decimal longitude |
| `World_Cup_Debut` | Yes/No — is this the team's first World Cup? |
| `Host_Nation` | Yes/No — is this team one of the 3 hosts? |

---

## Tools and technologies

| Tool | Purpose |
|---|---|
| Python (pandas, folium, matplotlib, seaborn) | Data cleaning and EDA |
| Tableau Public | Interactive geospatial dashboard |
| D3.js | In-browser interactive map |
| GitHub Pages | Project hosting |
| CSV | Raw and processed data storage |

---

## Data sources

- [FIFA Official — Team Base Camp Training Sites](https://inside.fifa.com/media-releases/world-cup-2026-team-base-camps-tbc-48-nations-usa-mexico-canada)
- [U.S. Soccer Federation — Base Camp Confirmations](https://www.ussoccer.com/stories/2026/06/usmnt/where-are-fifa-world-cup-2026-team-base-camp-training-sites)
- [Sports Illustrated — Full Base Camp Breakdown](https://www.si.com/soccer/where-each-team-2026-world-cup-based)
- [RotoWire — Complete Base Camp List](https://www.rotowire.com/soccer/article/2026-world-cup-base-camps-where-all-48-teams-will-train-116134)

---

## Author

**Astonish** | CA, MBA  
Co-Founder & Managing Consultant, MEK Consult LLC  
Multi-Unit Team Leader & Tax Professional, H&R Block  
Kansas City, Missouri | Accra, Ghana

[LinkedIn](https://www.linkedin.com/in/) · [GitHub](https://github.com/)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Data is sourced from publicly available FIFA and sports media sources for educational and analytical purposes.

## 📊 Live Dashboard

🔗 [View Live Dashboard on Tableau Public](https://public.tableau.com/app/profile/marvel.astonish/viz/dashboard_preview_png_17816349811200/Dashboard1)
