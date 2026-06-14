# Tableau Public build guide — FIFA World Cup 2026 Base Camps

**Target output:** Interactive geospatial dashboard published to Tableau Public
**Estimated build time:** 45–60 minutes
**Skill level required:** Beginner–Intermediate

---

## Prerequisites

- [ ] Download and install [Tableau Public (free)](https://public.tableau.com/en-us/s/download)
- [ ] Download `data/raw/wc2026_base_camps_raw.csv` from this repo
- [ ] Create a free [Tableau Public account](https://public.tableau.com/en-us/s/signup)

---

## Step 1 — Connect to data

1. Open Tableau Public
2. Under **Connect**, click **Text File**
3. Navigate to and select `wc2026_base_camps_raw.csv`
4. In the Data Source preview, verify all 48 rows loaded and column types are correct:
   - `FIFA_Rank` → Number (whole)
   - `Latitude` → Number (decimal)
   - `Longitude` → Number (decimal)
   - All others → String
5. Click **Sheet 1** tab at the bottom to begin building

---

## Step 2 — Build Sheet 1: Base camp map (main viz)

1. In the Data pane, right-click `Latitude` → **Geographic Role → Latitude**
2. Right-click `Longitude` → **Geographic Role → Longitude**
3. Drag `Longitude` to the **Columns** shelf
4. Drag `Latitude` to the **Rows** shelf
5. Both pills should say **AVG(Longitude)** and **AVG(Latitude)** — change both to **Dimension**
6. Tableau will now show a dot for every team on a map

**Color by confederation:**
- Drag `Confederation` to the **Color** mark
- Click Color → Edit Colors → manually assign:
  - UEFA → `#185FA5` (blue)
  - CONMEBOL → `#3B6D11` (green)
  - CAF → `#854F0B` (amber)
  - AFC → `#993C1D` (coral)
  - CONCACAF → `#534AB7` (purple)
  - OFC → `#72243E` (pink)

**Size by FIFA rank:**
- Drag `FIFA_Rank` to the **Size** mark
- Click Size mark → Reversed (so rank #1 = largest dot)
- Adjust size range: min 6px, max 18px

**Labels:**
- Drag `Team` to the **Label** mark
- Click Label → uncheck "Show mark labels" (too cluttered on map)
- Keep labels OFF by default — tooltip will handle detail

**Tooltip:**
- Click the **Tooltip** mark → edit to read:
```
<Team>  <Flag>
Group: <Group>   FIFA Rank: #<FIFA_Rank>
Confederation: <Confederation>
Base Camp: <Base_Camp_City>, <Base_Camp_State_Region>
Facility: <Training_Facility>
Host Country: <Host_Country>
World Cup Debut: <World_Cup_Debut>
```

**Title:** Rename Sheet 1 to "Base Camp Map"

---

## Step 3 — Build Sheet 2: Teams per host country (bar chart)

1. Right-click the Sheet tab → **New Sheet**
2. Drag `Host_Country` to **Columns**
3. Drag `Team` to **Rows** → change to **COUNT(Team)**
4. Drag `Host_Country` to **Color**
5. Sort bars descending by count
6. Add `COUNT(Team)` to **Label**
7. Title: "Teams per host country"

---

## Step 4 — Build Sheet 3: Confederation breakdown (bar)

1. New sheet
2. Drag `Confederation` to **Rows**
3. Drag `Team` to **Columns** → COUNT
4. Drag `Confederation` to **Color**
5. Sort descending
6. Title: "Teams by confederation"

---

## Step 5 — Build Sheet 4: FIFA rank vs host country (box plot)

1. New sheet
2. Drag `Host_Country` to **Columns**
3. Drag `FIFA_Rank` to **Rows**
4. In the Marks card, change mark type to **Circle**
5. Add a reference line: Analytics pane → drag **Average Line** to the view
6. Title: "FIFA rank distribution by host country"

---

## Step 6 — Build the dashboard

1. Click **New Dashboard** (icon at bottom tab bar)
2. Set size: **Fixed → 1200 x 800**
3. Drag sheets onto the canvas:
   - **Base Camp Map** — top, full width (large)
   - **Teams per host country** — bottom left
   - **Teams by confederation** — bottom center
   - **FIFA rank distribution** — bottom right
4. Add a **Text** object at the top:
   - Title: `FIFA World Cup 2026 — Team Base Camp Locations`
   - Subtitle: `48 nations · 3 host countries · 25 non-host communities`
5. Add **Filters** (drag from Sheets panel):
   - `Confederation`
   - `Host_Country`
   - `Group`
   - Set filter display to "Single value (dropdown)"
6. Check **"Use as Filter"** on the bar charts so clicking a bar filters the map

---

## Step 7 — Polish and publish

**Formatting:**
- Dashboard → Format → Shading → set to white
- Remove all borders and gridlines for a clean look
- Font: Tableau Book or Calibri throughout

**Add a source note:**
- Insert → Text object at the bottom:
  `Data: FIFA Official · U.S. Soccer · Sports Illustrated · Analysis by Astonish / MEK Consult LLC`

**Publish:**
1. File → **Save to Tableau Public**
2. Sign in with your Tableau Public account
3. Name the workbook: `FIFA World Cup 2026 — Team Base Camp Locations`
4. Check "Show sheets as tabs" → Save
5. Copy the public URL once published

**Share the URL:**
- Paste into your GitHub README (replace the placeholder link)
- Embed in LinkedIn post
- Add to MEK Consult website if applicable

---

## Tableau Public embed code for README

Once published, Tableau gives you an embed script. Add this to your README:

```html
<div class='tableauPlaceholder'>
  <noscript>
    <a href='YOUR_TABLEAU_URL'>
      <img src='thumbnail.png' alt='FIFA World Cup 2026 Base Camp Map' />
    </a>
  </noscript>
  <object class='tableauViz' style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='name' value='YOUR_WORKBOOK_NAME' />
    <param name='tabs' value='yes' />
    <param name='toolbar' value='yes' />
  </object>
</div>
```
