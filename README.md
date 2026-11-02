# ⚡ Global Electric Vehicle Market Intelligence Platform

> **An end-to-end data analytics project** analyzing **200,000+ global EV records** across **200 automotive manufacturers**, featuring interactive **Tableau dashboards**, a **10-scene data story**, and a modern **Flask web portal** — all powered by Snowflake and Tableau.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask)](https://flask.palletsprojects.com)
[![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/uday.ksuwhaha/viz/EV_Market_Performance_Market_Story_2026-10-25_17933746131570/EVExecutiveDashboard)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data_Warehouse-29B5E8?logo=snowflake&logoColor=white)](https://snowflake.com)

---

## 📊 Core KPI Highlights

| Metric | Value |
|---|---|
| Active Manufacturers | **200** global OEMs |
| Vehicle Models Tracked | **17,980** |
| Cumulative Sales Volume | **1.55 Billion** units |
| Average Customer Rating | **4.09 / 5.0** |
| Average Driving Range | **324.5 km** per charge |
| Average Battery Capacity | **78.2 kWh** |
| Dataset Records | **200,000** rows × **39** features |

---

## 🗂️ Project Structure

```
Skill_wallet_project_1/
│
├── README.md                              # This file
├── Final_Project_Report.pdf               # Comprehensive final project report
├── Global_EV_Market_Intelligence_Comprehensive_Report.pdf
│
├── dataset/
│   └── ev_market_train.xlsx               # Primary dataset (200K records, 39 features)
│
├── documants/                             # Full SDLC documentation (8 phases)
│   ├── 1. Ideation Phase/
│   │   ├── Brainstorm & Idea Prioritization.docx
│   │   ├── Define Problem Statements.docx
│   │   └── Empathy Map Canvas.docx
│   ├── 2. Requirement Analysis/
│   │   ├── Customer Journey Map.docx/.pdf
│   │   ├── Data Flow Diagrams and User Stories.docx
│   │   ├── Solution Requirements.docx
│   │   └── Technology Stack.docx
│   ├── 3. Project Design Phase/
│   │   ├── Project Proposal (Proposed Solution).docx
│   │   └── Solution Architecture.docx
│   ├── 4. Project Planning Phase/
│   │   └── Project Planning.docx
│   ├── 5. Project Development Phase/
│   │   ├── Snowflake/   (Business Questions, Code & Solution, Dashboard Design, Data Preparation)
│   │   └── Tableau/     (Business Questions, Dashboard Design, Story Design)
│   ├── 6. Performance Testing/
│   │   ├── Snowflake.docx
│   │   └── Tableau.docx
│   ├── 7. Project Documentation/
│   │   └── Final Report.docx/.pdf
│   └── 8. Project Demonstration/
│       ├── Communication.docx/.pdf
│       ├── Demonstration of Proposed Features.docx/.pdf
│       ├── Project Demo Planning.docx/.pdf
│       ├── Scalability & Future Plan.docx/.pdf
│       └── Team Involvement in Demonstration.docx/.pdf
│
├── tableau files/
│   └── EV_Market_Performance.twbx         # Packaged Tableau workbook
│
├── Screenshots/                           # Dashboard & visualization screenshots (8 images)
│
├── Links/
│   ├── tableau_public.txt                 # Tableau Public published URL
│   ├── Documents.txt                      # Shared document links
│   └── Demo_video.txt                     # Demo video link
│
└── website/                               # Flask web application
    ├── app.py                             # Main Flask app with routes & data config
    ├── requirements.txt                   # Python dependencies
    ├── README.md                          # Website-specific readme
    ├── Html files/                        # Jinja2 HTML templates
    │   ├── base.html                      # Base layout (navbar, footer)
    │   ├── index.html                     # Home page with KPI scorecards
    │   ├── dashboard.html                 # Tableau Executive Dashboard embed
    │   ├── story.html                     # 10-Scene Story embed
    │   ├── visualizations.html            # 9 Visualizations catalog
    │   └── insights.html                  # Market intelligence report
    └── static/
        └── css/
            └── style.css                  # Executive dark-mode design system
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Data Warehouse** | Snowflake (cloud SQL analytics) |
| **Visualization** | Tableau Desktop & Tableau Public |
| **Web Framework** | Python Flask 3.0+ |
| **Frontend** | HTML5, CSS3 (custom dark-mode), Jinja2 templating |
| **Icons** | Font Awesome 6.5 |
| **Dataset Format** | Excel (.xlsx) — 200K rows × 39 columns |
| **Version Control** | Git / GitHub |

---

## 🔧 Getting Started

### Prerequisites

- **Python 3.10+** installed
- **pip** package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dinomae/Skill_wallet_project_1.git
   cd Skill_wallet_project_1
   ```

2. **Install Python dependencies**
   ```bash
   cd website
   pip install -r requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🌐 Web Application Pages

| Route | Page | Description |
|---|---|---|
| `/` | **Home** | Executive overview with KPI scorecards and navigation cards |
| `/dashboard` | **Dashboard** | Embedded interactive Tableau Executive Dashboard |
| `/story` | **Story** | Guided 10-scene Tableau data story narrative |
| `/visualizations` | **Catalog** | Detailed catalog of all 9 unique visualizations |
| `/insights` | **Insights** | Market intelligence analysis and key findings |
| `/api/stats` | **API** | RESTful JSON endpoint returning project metrics |

---

## 📈 Visualizations (9 Unique Charts)

| # | Visualization | Chart Type |
|---|---|---|
| 1 | EV Market Performance at a Glance | KPI Scorecard |
| 2 | Market Share by Manufacturer | Horizontal Bar Chart |
| 3 | Customer Rating by EV Category | Bar Chart with Benchmarks |
| 4 | Annual Sales by Vehicle Type | Horizontal Bar Chart |
| 5 | Regional Market Comparison | Horizontal Bar Chart |
| 6 | Battery Technology Market Share | Stacked Bar Chart |
| 7 | Driving Range by Vehicle Category | Horizontal Bar Chart |
| 8 | EV Distribution by Manufacturing Country | Geographic Bubble Map |
| 9 | Annual EV Sales Trend by Model Year | Multi-Year Line Chart |

---

## 🎬 Data Story — 10 Scenes

| Scene | Caption | Focus Area |
|---|---|---|
| 1 | Market Snapshot | Executive KPI overview & global map |
| 2 | Manufacturer Sales | Competitive volume analysis across 200 OEMs |
| 3 | Battery Technology Mix | NMC vs LFP adoption landscape |
| 4 | Regional Comparison | Continental market penetration rates |
| 5 | Manufacturing Footprint | Global factory distribution density |
| 6 | Annual Sales by Vehicle Type | Hatchback & two-wheeler mass adoption |
| 7 | Customer Ratings | Consumer satisfaction across segments |
| 8 | Driving Range by Category | Autonomy benchmarks per charge |
| 9 | Annual Sales Trend | Multi-year sales growth trajectory |
| 10 | Category Performance | Proportional model & category distribution |

---

## 🏗️ Data Pipeline Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌────────────────┐
│  Raw Dataset │────▶│    Snowflake     │────▶│  Tableau Desktop │────▶│  Tableau Public │
│  (.xlsx)     │     │  Data Warehouse  │     │  .twbx Workbook  │     │  (Published)    │
│  200K × 39   │     │  SQL Analytics   │     │  9 Visuals +     │     │  Live Embeds    │
│              │     │  & Validation    │     │  10-Scene Story  │     │                 │
└──────────────┘     └──────────────────┘     └──────────────────┘     └───────┬────────┘
                                                                               │
                                                                               ▼
                                                                      ┌────────────────┐
                                                                      │  Flask Web App  │
                                                                      │  (Python 3.10+) │
                                                                      │  Dark-Mode UI   │
                                                                      │  Embed + API    │
                                                                      └────────────────┘
```

---

## 📝 Project Development Phases (SDLC)

1. **Ideation Phase** — Brainstorming, problem statements, empathy mapping
2. **Requirement Analysis** — Customer journeys, data flows, user stories, tech stack selection
3. **Project Design** — Solution architecture, project proposal
4. **Project Planning** — Timeline, milestones, and resource allocation
5. **Project Development** — Snowflake SQL analytics + Tableau visualization builds
6. **Performance Testing** — Snowflake query optimization + Tableau rendering benchmarks
7. **Project Documentation** — Final report compilation
8. **Project Demonstration** — Demo planning, feature showcase, scalability roadmap

---

## ⚙️ Configuration

To point the web app to your own Tableau Public dashboards, update the constants in [`website/app.py`](website/app.py):

```python
TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YOUR_WORKBOOK/YOUR_DASHBOARD"
TABLEAU_STORY_URL     = "https://public.tableau.com/views/YOUR_WORKBOOK/YOUR_STORY"
```

---

## 📸 Screenshots

Dashboard and visualization screenshots are available in the [`Screenshots/`](Screenshots/) directory.

---

## 🔗 Live Tableau Public Links

- 📊 **[EV Executive Dashboard](https://public.tableau.com/app/profile/uday.ksuwhaha/viz/EV_Market_Performance_Market_Story_2026-10-25_17933746131570/EVExecutiveDashboard)**
- 🎬 **[EV Market Journey Story](https://public.tableau.com/app/profile/uday.ksuwhaha/viz/EV_Market_Performance_Market_Story_2026-10-25_17933746131570/EVMarketJourney?publish=yes)**

---

## 📄 Reports

- [**Final Project Report**](Final_Project_Report.pdf) — Comprehensive end-to-end project documentation
- [**Global EV Market Intelligence Report**](Global_EV_Market_Intelligence_Comprehensive_Report.pdf) — Detailed market analysis findings

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is for educational and analytical purposes.

---

<p align="center">
  <b>Built with ❤️ using Snowflake · Tableau · Python Flask</b>
</p>

