# NFL 2024 Season: Salary vs. Performance Analysis

A Python data analysis project examining whether NFL teams are getting value from their player contracts using pandas and matplotlib.

---

## Overview

Using performance and salary data from the **2024 NFL regular season**, this project analyzes the relationship between player cap hits and on-field production across all four skill positions (QB, RB, WR, TE). Fantasy points are used as a standardized cross-position performance metric, allowing apples-to-apples comparisons regardless of position.

---

## Tools & Skills

- **Python** — core analysis language
- **pandas** — data loading, cleaning, transformation, and aggregation
- **matplotlib** — multi-panel data visualization
- **CSV** — data storage and portability

---

## Dataset

- 43 of the NFL's highest-profile skill position players from the 2024 season
- Columns include: player name, team, position, cap hit, passing yards, rushing yards, receiving yards, touchdowns, interceptions
- Derived columns: `fantasy_points`, `cap_hit_millions`, `value_score` (fantasy pts per $1M), `fp_per_game`

**Fantasy point scoring used:**
- QB: passing yards/25 + passing TDs×4 − interceptions×2 + rushing yards/10 + rushing TDs×6
- RB: rushing yards/10 + rushing TDs×6 + receiving yards/10
- WR/TE: receiving yards/10 + receiving TDs×6

---

## Key Questions Explored

1. Which players generate the most production per dollar?
2. Which expensive players underperformed their contracts?
3. How does value differ by position?
4. Is there a correlation between cap hit and performance?

---

## Visualizations

The project produces a 4-panel dashboard:

**1. Cap Hit vs. Fantasy Points (Scatter)**
Shows the relationship between salary and production by position. Notable outliers like Brock Purdy ($5.4M, top-10 QB production) and Dak Prescott ($60M, missed 5 games) are clearly visible.

**2. Top 10 Value Players (Bar Chart)**
Ranks players by fantasy points per $1M cap hit. Rookies and late-round finds — Derrick Henry, Kyren Williams, Puka Nacua — dominate this list.

**3. Position Comparison (Grouped Bar)**
Compares average cap hit vs. average fantasy points by position. QBs are by far the most expensive; RBs deliver strong production at relatively low cost.

**4. Most Overpaid Players (Bar Chart)**
Among players earning $10M+, identifies those with the lowest value scores. Highlights the risk of paying top dollar for players who underperform or miss games.

---

## Key Findings

- **Rookie and cheap contracts are massively efficient.** De'Von Achane ($1M), Kyren Williams ($1.2M), and Brock Purdy ($5.4M) all delivered elite production at a fraction of the cost of established stars.
- **Cap hit does not predict performance.** The scatter plot shows a weak correlation — several $50M+ players underperformed while multiple players under $6M outperformed them.
- **RBs offer the best positional value.** Despite being among the least-paid skill positions, running backs generated competitive fantasy production relative to their contracts.
- **Injury risk amplifies overpayment.** Players like Tua Tagovailoa and Trevor Lawrence missed significant time, making their large contracts look even worse in a per-dollar analysis.

---

