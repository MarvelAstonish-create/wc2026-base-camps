# Step-by-step GitHub publication guide
# FIFA World Cup 2026 — Base Camp Locations Project

---

## PHASE 1 — Set up GitHub (if you haven't already)

### Step 1.1 — Create a GitHub account
1. Go to https://github.com
2. Click "Sign up"
3. Username recommendation: use your professional name or initials
   e.g. `astonish-mek` or `mek-consult`
4. Verify your email address

### Step 1.2 — Install Git on your computer
- macOS: open Terminal, type `git --version`
  If not installed, macOS will prompt you to install it
- Windows: download from https://git-scm.com/download/win
  Use all default settings during install
- Verify install: open Terminal/Command Prompt → type `git --version`
  You should see something like: git version 2.x.x

### Step 1.3 — Configure Git with your identity (one-time setup)
Open Terminal (Mac) or Git Bash (Windows) and run:

    git config --global user.name "Your Full Name"
    git config --global user.email "your@email.com"

---

## PHASE 2 — Create the GitHub repository

### Step 2.1 — Create a new repository on GitHub
1. Log into github.com
2. Click the "+" icon (top right) → "New repository"
3. Fill in the form:
   - Repository name: `wc2026-base-camps`
   - Description: `FIFA World Cup 2026 — Geospatial analysis of all 48 team base camp locations across USA, Mexico & Canada`
   - Visibility: Public (required for Tableau Public embed and LinkedIn sharing)
   - Check: "Add a README file" → UNCHECK this (we have our own README)
   - Add .gitignore: None (we have our own)
   - License: None (we have our own)
4. Click "Create repository"
5. GitHub will show you the empty repo page — leave this browser tab open

---

## PHASE 3 — Set up the project locally

### Step 3.1 — Download the project files from Claude
From this conversation, download:
- `wc2026_base_camps.csv` → save to a folder called `wc2026-base-camps`

The full folder structure you need to create:

    wc2026-base-camps/
    ├── data/
    │   ├── raw/
    │   │   └── wc2026_base_camps_raw.csv
    │   └── processed/              ← empty folder for now
    ├── notebooks/
    │   └── wc2026_analysis.py
    ├── visualizations/
    │   └── tableau_workbook_guide.md
    ├── docs/
    │   └── data_dictionary.md
    ├── assets/                     ← empty folder for now
    ├── README.md
    ├── .gitignore
    └── LICENSE

### Step 3.2 — Copy the CSV to the right location
Move `wc2026_base_camps.csv` into the `data/raw/` subfolder.
Rename it: `wc2026_base_camps_raw.csv`

### Step 3.3 — Create the README, .gitignore, LICENSE, and other files
Copy all files from the project package Claude built.
Each file's content is in this repository's file list.

---

## PHASE 4 — Initialize Git and connect to GitHub

### Step 4.1 — Open Terminal in your project folder

Mac:
1. Open Finder → navigate to the `wc2026-base-camps` folder
2. Right-click the folder → "New Terminal at Folder"

Windows:
1. Open File Explorer → navigate to the `wc2026-base-camps` folder
2. Right-click in the folder → "Open Git Bash here"

### Step 4.2 — Initialize the Git repository
Run these commands one at a time, pressing Enter after each:

    git init

You should see: Initialized empty Git repository in .../wc2026-base-camps/.git/

### Step 4.3 — Add all files to Git tracking

    git add .

This stages every file in the folder (the dot means "everything").

### Step 4.4 — Make your first commit

    git commit -m "Initial commit: 48-team base camp dataset, README, analysis script, docs"

You should see a list of files being committed.

### Step 4.5 — Rename the branch to "main"

    git branch -M main

### Step 4.6 — Connect to your GitHub repository
Go back to your GitHub tab. Copy the URL shown — it looks like:
  https://github.com/YOUR-USERNAME/wc2026-base-camps.git

Then run (paste your actual URL):

    git remote add origin https://github.com/YOUR-USERNAME/wc2026-base-camps.git

### Step 4.7 — Push your files to GitHub

    git push -u origin main

Git will ask for your GitHub username and password.
NOTE: GitHub no longer accepts regular passwords for Git push.
You need a Personal Access Token (PAT) instead of your password.

To create a PAT:
1. GitHub.com → click your profile photo → Settings
2. Scroll down → "Developer settings" (left sidebar)
3. Personal access tokens → Tokens (classic) → Generate new token
4. Note: "Git push for wc2026 project"
5. Expiration: 90 days
6. Check the "repo" scope (full control of repositories)
7. Click "Generate token"
8. COPY the token immediately — you won't see it again
9. Use this token as your password when Git asks

After pushing, go to github.com/YOUR-USERNAME/wc2026-base-camps
You should see all your files live on GitHub.

---

## PHASE 5 — Verify and polish the repository

### Step 5.1 — Check your README renders correctly
1. On your GitHub repo page, scroll down
2. The README.md should display as a formatted page
3. Check: table formatting, badges, and section headers look correct

### Step 5.2 — Add repository topics (tags)
On your repo page:
1. Click the gear icon next to "About" (right side)
2. Add topics: `data-analytics`, `world-cup-2026`, `tableau`, `geospatial`,
   `soccer`, `fifa`, `python`, `visualization`, `sports-analytics`
3. Add the description if not already there
4. Save changes

### Step 5.3 — Create empty placeholder folders
GitHub does not track empty folders. To keep your structure visible:

    touch data/processed/.gitkeep
    touch assets/.gitkeep
    git add .
    git commit -m "Add placeholder files for empty directories"
    git push

---

## PHASE 6 — Add the Tableau visualization

### Step 6.1 — Build and publish in Tableau Public
Follow the full guide in `visualizations/tableau_workbook_guide.md`

### Step 6.2 — Add the Tableau link to your README
Once published, get the URL from Tableau Public.
Edit your README.md:

    ## Live visualization
    
    [View interactive dashboard on Tableau Public](YOUR_TABLEAU_URL)

Then push the update:

    git add README.md
    git commit -m "Add Tableau Public visualization link to README"
    git push

### Step 6.3 — Take a screenshot of the Tableau dashboard
1. Save the screenshot as `assets/dashboard_preview.png`
2. Add it to README.md above the Tableau link:

    ## Live visualization
    
    [![Dashboard Preview](assets/dashboard_preview.png)](YOUR_TABLEAU_URL)
    
    [View interactive dashboard on Tableau Public](YOUR_TABLEAU_URL)

Then push:

    git add assets/dashboard_preview.png README.md
    git commit -m "Add dashboard screenshot preview to README"
    git push

---

## PHASE 7 — Enable GitHub Pages (optional but impressive)

GitHub Pages turns your repository into a public website — great for
hosting the interactive D3.js map directly.

1. Go to your repo → Settings → Pages (left sidebar)
2. Source: Deploy from a branch
3. Branch: main → /root → Save
4. Wait 2–3 minutes
5. Your project is now live at:
   https://YOUR-USERNAME.github.io/wc2026-base-camps/

Add this link to your README and LinkedIn post.

---

## PHASE 8 — LinkedIn post (publish the project)

Copy this post template and fill in your links:

---

I just published a new data analytics project on GitHub:

FIFA World Cup 2026 — Team Base Camp Locations

PROBLEM:
With 48 teams across 3 host nations for the first-ever expanded World Cup,
understanding where each country chose to train — and why — reveals a
fascinating logistics story behind the football spectacle.

DATA PROCESS:
I compiled official FIFA-confirmed Team Base Camp Training Sites for all 48
qualified nations, geocoded each location, and enriched the dataset with
confederation, group draw, FIFA ranking, and debut-nation flags.
Tools: Python (pandas) · Tableau Public · D3.js

KEY INSIGHTS:
- 39 of 48 teams (81%) are based in the USA
- Kansas City alone hosts 4 teams: Argentina, England, Netherlands, Algeria
- California hosts 7 teams — the most of any single state
- Iran switched base camps mid-tournament from Tucson, AZ to Tijuana, Mexico
- 25 non-host communities benefit economically from the tournament

RECOMMENDATION:
FIFA's base camp model creates significant economic spillover beyond the
16 host cities. Tournament organizers should formalize this as a "host
community" tier with dedicated budgets and fan access programs for future
editions.

GitHub repo: [LINK]
Tableau dashboard: [LINK]

#DataAnalytics #FIFA2026 #WorldCup2026 #Tableau #Python #Geospatial
#BusinessIntelligence #DataVisualization #SportsAnalytics #MEKConsult

---

## Quick command reference

    # Check status of your files
    git status

    # Add a specific file
    git add filename.csv

    # Add all changed files
    git add .

    # Commit with a message
    git commit -m "Your message here"

    # Push to GitHub
    git push

    # Pull latest from GitHub (if editing online)
    git pull

    # Check your remote connection
    git remote -v
