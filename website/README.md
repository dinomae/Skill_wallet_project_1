# Global Electric Vehicle Market Intelligence Web Portal
> Python Flask application embedding interactive Tableau Dashboards and Stories.

## Structure
```
website/
├── app.py                  # Main Flask application and routing
├── requirements.txt        # Python package dependencies
├── templates/              # HTML5 Jinja2 Templates
│   ├── base.html           # Core layout with modern navbar & footer
│   ├── index.html          # Executive home with KPI scorecards
│   ├── dashboard.html      # Tableau Executive Dashboard embed page
│   ├── story.html          # 10-Scene Story narrative embed page
│   ├── visualizations.html # 9 Unique Visualizations catalog
│   └── insights.html       # Market intelligence analysis report
└── static/
    └── css/
        └── style.css       # Executive dark-mode design system
```

## Setup & Running

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python app.py
```

### 3. Open in Browser
Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## Configuration
To point the application to your custom Tableau Public URL, update the constants at the top of `app.py`:
- `TABLEAU_DASHBOARD_URL`
- `TABLEAU_STORY_URL`
