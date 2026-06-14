# FIFA World Cup 2026 — Base Camp Analysis
# Author: Astonish | MEK Consult LLC
# Description: Exploratory data analysis of all 48 team base camp locations
#
# To run: jupyter notebook  OR  python wc2026_analysis.py
# To convert to notebook: jupytext --to notebook wc2026_analysis.py

# ── 0. Imports ────────────────────────────────────────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# ── 1. Load data ──────────────────────────────────────────────────────────────
df = pd.read_csv("../data/raw/wc2026_base_camps_raw.csv")

print(f"Dataset shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nSample rows:")
print(df.head(3).to_string())

# ── 2. Basic validation ───────────────────────────────────────────────────────
print("\n── Null check ──")
print(df.isnull().sum())

print(f"\n── Unique teams: {df['Team'].nunique()} ──")
print(f"── Groups covered: {sorted(df['Group'].unique())} ──")
print(f"── Confederations: {sorted(df['Confederation'].unique())} ──")

# ── 3. Host country distribution ──────────────────────────────────────────────
print("\n── Base camps by host country ──")
hc_counts = df['Host_Country'].value_counts()
print(hc_counts)
print(f"\nUSA share: {hc_counts['USA']/len(df)*100:.1f}%")

# ── 4. Confederation breakdown ───────────────────────────────────────────────
conf_hc = pd.crosstab(df['Confederation'], df['Host_Country'])
print("\n── Confederation × Host Country ──")
print(conf_hc)

# ── 5. State/Region clustering (USA only) ────────────────────────────────────
usa = df[df['Host_Country'] == 'USA']
state_counts = usa['Base_Camp_State_Region'].value_counts()
print(f"\n── Top 10 US states by team count ──")
print(state_counts.head(10))

# ── 6. City clustering ────────────────────────────────────────────────────────
city_counts = df['Base_Camp_City'].value_counts()
multi_city = city_counts[city_counts > 1]
print(f"\n── Cities hosting multiple teams ──")
print(multi_city)

# ── 7. FIFA rank analysis by host country ────────────────────────────────────
print("\n── Average FIFA rank by host country ──")
print(df.groupby('Host_Country')['FIFA_Rank'].agg(['mean','min','max']).round(1))

print("\n── Average FIFA rank by confederation ──")
print(df.groupby('Confederation')['FIFA_Rank'].mean().sort_values().round(1))

# ── 8. Debut nations ─────────────────────────────────────────────────────────
debuts = df[df['World_Cup_Debut'] == 'Yes']
print(f"\n── Debut nations ({len(debuts)}) ──")
print(debuts[['Team','Confederation','Host_Country','Base_Camp_City']].to_string(index=False))

# ── 9. VISUALIZATIONS ────────────────────────────────────────────────────────

CONF_COLORS = {
    'UEFA':     '#185FA5',
    'CONMEBOL': '#3B6D11',
    'CAF':      '#854F0B',
    'AFC':      '#993C1D',
    'CONCACAF': '#534AB7',
    'OFC':      '#72243E',
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('FIFA World Cup 2026 — Base Camp Analytics', fontsize=14, fontweight='normal', y=1.01)

# Plot 1: Teams per host country
ax1 = axes[0, 0]
hc_data = df['Host_Country'].value_counts()
bars = ax1.bar(hc_data.index, hc_data.values,
               color=['#185FA5', '#3B6D11', '#993C1D'], width=0.5)
ax1.set_title('Teams per host country', fontsize=12)
ax1.set_ylabel('Number of teams')
for bar, val in zip(bars, hc_data.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(val), ha='center', va='bottom', fontsize=11)
ax1.set_ylim(0, 45)
ax1.spines[['top','right']].set_visible(False)

# Plot 2: Confederation breakdown
ax2 = axes[0, 1]
conf_data = df['Confederation'].value_counts()
colors = [CONF_COLORS.get(c, '#888') for c in conf_data.index]
wedges, texts, autotexts = ax2.pie(
    conf_data.values, labels=conf_data.index,
    colors=colors, autopct='%1.0f%%',
    pctdistance=0.82, startangle=140
)
for at in autotexts:
    at.set_fontsize(9)
ax2.set_title('Teams by confederation', fontsize=12)

# Plot 3: Top US states
ax3 = axes[1, 0]
top_states = state_counts.head(8)
ax3.barh(top_states.index[::-1], top_states.values[::-1], color='#185FA5', height=0.6)
ax3.set_title('Top US states by team count', fontsize=12)
ax3.set_xlabel('Number of teams')
ax3.spines[['top','right']].set_visible(False)
for i, (idx, val) in enumerate(zip(top_states.index[::-1], top_states.values[::-1])):
    ax3.text(val + 0.05, i, str(val), va='center', fontsize=10)

# Plot 4: FIFA rank distribution by host country
ax4 = axes[1, 1]
for hc, color in [('USA','#185FA5'),('Mexico','#3B6D11'),('Canada','#993C1D')]:
    subset = df[df['Host_Country'] == hc]['FIFA_Rank']
    ax4.hist(subset, bins=10, alpha=0.65, label=hc, color=color)
ax4.set_title('FIFA rank distribution by host country', fontsize=12)
ax4.set_xlabel('FIFA Rank (lower = better)')
ax4.set_ylabel('Number of teams')
ax4.legend()
ax4.spines[['top','right']].set_visible(False)

plt.tight_layout()
plt.savefig('../visualizations/wc2026_analytics_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nChart saved to visualizations/wc2026_analytics_dashboard.png")

# ── 10. Export clean/processed dataset ───────────────────────────────────────
df_clean = df.copy()
df_clean['FIFA_Rank'] = df_clean['FIFA_Rank'].astype(int)
df_clean['World_Cup_Debut'] = df_clean['World_Cup_Debut'].map({'Yes': True, 'No': False})
df_clean['Host_Nation'] = df_clean['Host_Nation'].map({'Yes': True, 'No': False})
df_clean.to_csv('../data/processed/wc2026_base_camps_clean.csv', index=False)
print("Clean dataset exported to data/processed/wc2026_base_camps_clean.csv")
print(f"\nFinal dataset: {df_clean.shape[0]} teams, {df_clean.shape[1]} fields")
