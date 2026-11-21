# Superstore Sales Analysis & Interactive Dashboard

## Project Overview

This project focuses on analyzing the Superstore sales dataset to understand sales performance, profitability, customer segments, product categories, regional performance, and shipping trends.

The project combines exploratory data analysis (EDA), data visualization, feature engineering, and an interactive dashboard to transform raw sales data into meaningful business insights.

## Project Objectives

- Understand and explore the Superstore dataset.
- Perform data cleaning and preprocessing.
- Apply feature engineering to create meaningful analytical variables.
- Analyze sales, profit, discounts, and other business metrics.
- Identify trends and patterns through data visualization.
- Build an interactive dashboard for exploring business performance.
- Present findings and recommendations based on the analysis.

## Dataset Information

The project uses the Superstore sales dataset.

| Dataset Detail | Information |
|---|---|
| Total Records | 9,994 |
| Original Columns | 21 |
| Processed Columns | 31 |
| Missing Values | None |
| Duplicate Records | None |
| Rows Removed | None |
| Data Period | 2014–2017 |

Two dataset files are maintained:

- `Dataset-Superstore.csv` – Original dataset.
- `superstore_processed.csv` – Processed dataset used for analysis and dashboard development.

## Core Libraries & Technologies

The project was developed using the following Python libraries and tools:

- **Python** – Main programming language.
- **Pandas** – Data manipulation and analysis.
- **NumPy** – Numerical operations.
- **Matplotlib** – Data visualization.
- **Seaborn** – Statistical data visualization.
- **Plotly Express** – Interactive charts and visualizations.
- **Dash** – Interactive web-based dashboard.
- **Jupyter Notebook** – Exploratory data analysis and experimentation.

**Development Tools:** VS Code, Git and GitHub.

For the complete list of project dependencies, refer to `requirements.txt`.

## Data Cleaning & Preprocessing

The dataset was examined and prepared before performing the analysis.

Key activities included:

- Inspecting dataset structure and data types.
- Checking for missing values.
- Identifying duplicate records.
- Converting date columns into appropriate datetime formats.
- Preparing the processed dataset for further analysis.

No missing values, duplicate records, or rows requiring removal were identified.

## Feature Engineering

Additional analytical columns were created to support deeper analysis:

- **Shipping Duration** – Measures the time taken between order and shipping dates.
- **Profit Margin** – Represents profitability relative to sales.
- **Sales Per Unit** – Calculates sales value per unit.
- **Profitability Status** – Classifies records as Profit, Loss, or Break-even.
- **Discount Bands** – Groups discounts into meaningful categories.

## Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand the dataset and identify important patterns.

The analysis covered:

- Descriptive statistics.
- Distribution of sales and profit.
- Outlier identification using the IQR method.
- Regional sales distribution.
- Product category analysis.
- Customer segment analysis.
- Shipping mode distribution.
- Correlation analysis.
- Discount and profitability patterns.

## Key Performance Indicators (KPIs)

The following business metrics were calculated:

| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Total Quantity | 37,873 |
| Overall Profit Margin | 12.47% |

These KPIs provide an overview of the overall business performance.

## Business Insights

Some important observations from the analysis include:

- Technology generated the highest total profit among the three product categories.
- The West region recorded the highest sales and profit.
- Consumer customers contributed the largest share of sales.
- Office Supplies had the highest order-record count among the product categories.
- High discounts were not always associated with higher profitability.
- Sales and profit showed a moderate positive correlation in the dataset.

These observations describe patterns in the available data and do not establish cause-and-effect relationships.

## Data Visualizations

Different visualization techniques were used to explore and communicate the findings.

The project includes:

- Histograms and KDE plots.
- Box plots.
- Count plots.
- Bar charts.
- Line charts.
- Scatter plots.
- Category and regional comparisons.
- Product performance visualizations.

Plotly was also used to create interactive charts with features such as hover information and zooming.

## Interactive Dashboard

An interactive dashboard was developed using **Dash** and **Plotly Express**.

### KPI Cards

The dashboard displays four key metrics:

- Total Sales
- Total Profit
- Profit Margin
- Total Orders

### Interactive Filters

Users can filter the dashboard using:

- Region
- Category
- Segment

The selected filters dynamically update the KPI cards and all four visualizations.

### Dashboard Charts

1. **Sales by Category** – Compares sales and profit across product categories.
2. **Monthly Sales & Profit Trend** – Displays monthly sales and profit trends.
3. **Top 10 Products** – Highlights the top ten products based on sales.
4. **Sales vs Profit Analysis** – Explores the relationship between sales and profit.

## Exported Visualizations

The project also includes four standalone HTML chart exports:

- `category_sales_profit.html`
- `monthly_sales_profit.html`
- `top_10_products.html`
- `sales_vs_profit.html`

These files allow individual interactive charts to be viewed separately in a web browser.

Note: Standalone chart exports do not contain the complete Dash dashboard or its interactive filters.

## Project Structure

```text
Superstore-Dashboard/
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   ├── Dataset-Superstore.csv
│   └── superstore_processed.csv
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── exports/
│   ├── category_sales_profit.html
│   ├── monthly_sales_profit.html
│   ├── top_10_products.html
│   └── sales_vs_profit.html
│
├── reports/
│   └── Superstore_Sales_Analysis_Report.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Superstore-Dashboard
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Dashboard

```bash
python dashboard/dashboard.py
```

Open the local URL displayed in the terminal to access the dashboard.

## Project Conclusion

This project demonstrates the use of Python-based data analysis and visualization techniques to examine business sales data.

Through data preprocessing, feature engineering, exploratory analysis, and an interactive dashboard, the project provides a structured view of sales performance and profitability.

It also demonstrates how analytical findings can be presented through interactive visualizations to support better understanding of business data.

---

**Project Focus:** Data Analysis | Exploratory Data Analysis | Data Visualization | Business Intelligence | Interactive Dashboard