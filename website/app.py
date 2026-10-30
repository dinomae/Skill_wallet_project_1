#!/usr/bin/env python3
"""
Global Electric Vehicle Market Intelligence Platform
Flask Web Application for Embedding Interactive Tableau Dashboards and Stories.
"""

import os
from flask import Flask, render_template, jsonify

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Tableau Public embed URLs — configure with your published URLs
TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/EV_Market_Performance_Market_Story_2026-10-25/EVExecutiveDashboard"
TABLEAU_STORY_URL = "https://public.tableau.com/views/EV_Market_Performance_Market_Story_2026-10-25/EVMarketJourney"

# Core Project Metrics
PROJECT_METRICS = {
    "total_models": 17980,
    "total_manufacturers": 200,
    "total_sales_units": "1.55B",
    "avg_rating": "4.09 / 5.0",
    "avg_range_km": "324.5 km",
    "avg_battery_kwh": "78.2 kWh",
    "dataset_records": 200000,
    "dataset_features": 39,
    "unique_visualizations": 9,
    "story_scenes": 10,
    "calculated_fields_used": 0
}

VISUALIZATIONS_CATALOG = [
    {
        "id": 1,
        "title": "EV Market Performance at a Glance",
        "type": "Executive KPI Scorecard",
        "description": "High-level summary cards showing active manufacturers (200), vehicle models (17,980), cumulative sales volume (1.55B units), customer satisfaction (4.09/5), average range (324.5 km), and battery capacity (78.2 kWh).",
        "fields": ["MFRS Count", "EV Count", "Total Annual Sales", "Average Customer Rating", "Average Range (km)", "Average Battery Capacity (kWh)"],
        "chart_family": "KPI Cards"
    },
    {
        "id": 2,
        "title": "Market Share by Manufacturer",
        "type": "Horizontal Bar Chart",
        "description": "Displays annual sales distribution across top automotive manufacturers. Evaluates competitive density and market volume leaders with descending ranking.",
        "fields": ["Manufacturer (Dimension)", "SUM(Annual Sales Units) (Measure)"],
        "chart_family": "Horizontal Bar Chart"
    },
    {
        "id": 3,
        "title": "Customer Rating Records by EV Category",
        "type": "Horizontal Bar Chart with Reference Benchmarks",
        "description": "Measures average customer satisfaction scores across vehicle segments, highlighting high user acceptance in Hatchbacks, SUVs, and Two-Wheelers.",
        "fields": ["Vehicle Category (Dimension)", "AVG(Customer Rating) (Measure)"],
        "chart_family": "Bar Chart"
    },
    {
        "id": 4,
        "title": "Annual Sales by Vehicle Type",
        "type": "Horizontal Bar Chart",
        "description": "Breaks down total unit deliveries across Hatchbacks, Two-Wheeler Scooters, Pickups, Vans, Micro City Cars, and Electric Buses, reflecting urban mobility demand.",
        "fields": ["Category (Dimension)", "SUM(Annual Sales Units) (Measure)"],
        "chart_family": "Horizontal Bar Chart"
    },
    {
        "id": 5,
        "title": "Regional Market Comparison",
        "type": "Horizontal Bar Chart",
        "description": "Compares EV adoption, charging infrastructure penetration, and sales volume across APAC, Europe, North America, and emerging geographical regions.",
        "fields": ["Market Region (Dimension)", "SUM(Annual Sales Units) (Measure)"],
        "chart_family": "Horizontal Bar Chart"
    },
    {
        "id": 6,
        "title": "Battery Technology Market Share",
        "type": "Horizontal / Stacked Bar Chart",
        "description": "Evaluates the market dominance of battery chemistries, demonstrating the overwhelming prevalence of NMC (Nickel Manganese Cobalt) and LFP (Lithium Iron Phosphate).",
        "fields": ["Battery Type (Dimension)", "SUM(Annual Sales Units) (Measure)"],
        "chart_family": "Bar Chart"
    },
    {
        "id": 7,
        "title": "Driving Range by Vehicle Category",
        "type": "Horizontal Bar Chart",
        "description": "Analyzes the average driving range in kilometers per full charge across categories, showing maturity in commercial and passenger vehicles.",
        "fields": ["Category (Dimension)", "AVG(Range Km) (Measure)"],
        "chart_family": "Bar Chart"
    },
    {
        "id": 8,
        "title": "Electric Vehicle Distribution by Manufacturing Country",
        "type": "Geographic Bubble Map",
        "description": "Interactive world map depicting manufacturing facility distribution and production density across key industrial countries, tracing supply chain hubs.",
        "fields": ["Manufacturing Country (ISO-3166)", "Latitude / Longitude (Generated)", "SUM(Annual Sales Units) (Size)"],
        "chart_family": "Geographic Map"
    },
    {
        "id": 9,
        "title": "Annual EV Sales Trend by Model Year",
        "type": "Multi-Year Line Chart",
        "description": "Tracks historic and modern EV unit delivery trajectories across model years, visualizing steep commercial adoption acceleration.",
        "fields": ["Model Year (Dimension / Time)", "SUM(Annual Sales Units) (Measure)"],
        "chart_family": "Line Chart"
    },
    {
        "id": 10,
        "title": "EV Category Performance & Distribution",
        "type": "Donut / Pie Chart",
        "description": "Visualizes categorical distribution and model variety share across segments, illustrating the dominant urban mobility categories.",
        "fields": ["Category (Dimension / Color)", "CNTD(Model Name) / SUM(Sales) (Angle/Wedge)"],
        "chart_family": "Pie / Donut Chart"
    }
]

STORY_SCENES = [
    {"scene": 1, "caption": "Market Snapshot", "sheet": "EV Executive Dashboard", "description": "Consolidated executive overview displaying KPI metrics, market leaders, regional breakdown, and map."},
    {"scene": 2, "caption": "Manufacturer Sales", "sheet": "Manufacturer Sales", "description": "Competitive analysis showing volume dominance across 200 global original equipment manufacturers."},
    {"scene": 3, "caption": "Battery Technology Mix", "sheet": "EV Sales by Battery type", "description": "Chemical composition adoption landscape, highlighting NMC and LFP efficiency advantages."},
    {"scene": 4, "caption": "Regional Comparison", "sheet": "Regional Sales", "description": "Geographical adoption velocity comparing continental market penetration rates."},
    {"scene": 5, "caption": "Manufacturing Footprint", "sheet": "Manufacturing Map", "description": "Global assembly distribution and geographic density of EV factories."},
    {"scene": 6, "caption": "Annual Sales by Vehicle Type", "sheet": "Vehicle Sales by Category", "description": "Vehicle segmentation showing how hatchbacks and two-wheelers drive mass adoption."},
    {"scene": 7, "caption": "Customer Ratings", "sheet": "Customer Rating", "description": "Consumer satisfaction metrics across segments reflecting high confidence in EV reliability."},
    {"scene": 8, "caption": "Driving Range by Category", "sheet": "Range Category", "description": "Autonomy benchmarks per battery charge, showing average ranges exceeding 324 km."},
    {"scene": 9, "caption": "Annual Sales Trend by Model Year", "sheet": "Annual EV Sales Trend by Model Year", "description": "Longitudinal growth curve illustrating multi-year sales compounding."},
    {"scene": 10, "caption": "EV Category Performance & Distribution", "sheet": "EV Category Performance & Distribution", "description": "Proportional distribution of EV models and categories in the modern market."}
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        metrics=PROJECT_METRICS,
        dashboard_url=TABLEAU_DASHBOARD_URL,
        story_url=TABLEAU_STORY_URL,
        page="home"
    )


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        metrics=PROJECT_METRICS,
        dashboard_url=TABLEAU_DASHBOARD_URL,
        page="dashboard"
    )


@app.route("/story")
def story():
    return render_template(
        "story.html",
        metrics=PROJECT_METRICS,
        story_url=TABLEAU_STORY_URL,
        scenes=STORY_SCENES,
        page="story"
    )


@app.route("/visualizations")
def visualizations():
    return render_template(
        "visualizations.html",
        metrics=PROJECT_METRICS,
        visualizations=VISUALIZATIONS_CATALOG,
        page="visualizations"
    )


@app.route("/insights")
def insights():
    return render_template(
        "insights.html",
        metrics=PROJECT_METRICS,
        page="insights"
    )


@app.route("/api/stats")
def api_stats():
    return jsonify({
        "status": "success",
        "metrics": PROJECT_METRICS,
        "visualizations_count": len(VISUALIZATIONS_CATALOG),
        "scenes_count": len(STORY_SCENES)
    })


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
