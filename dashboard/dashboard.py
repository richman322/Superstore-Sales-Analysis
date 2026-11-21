import pandas as pd
import matplotlib as plt
import plotly.express as px
from dash import html,dcc,Dash,Input,Output

df=pd.read_csv('./data/superstore_processed.csv',parse_dates=['Order Date', 'Ship Date'])

app=Dash(__name__)

Total_Sales=df['Sales'].sum()
Total_Profit=df['Profit'].sum()
Profit_Margin=(Total_Profit/Total_Sales)*100
Total_Orders=df['Order ID'].nunique()

category_data=df.groupby('Category')[['Sales','Profit']].sum().reset_index()
category_fig=px.bar(category_data,x='Category',y=['Sales','Profit'],title="Sales by Category")

year_month=df['Order Date'].dt.strftime('%Y-%m')
month_names=df.groupby(year_month)[['Sales','Profit']].sum().reset_index()
monthly_fig=px.line(month_names,x="Order Date",y=['Sales','Profit'],title="Monthly Sales & Profit Trend")
monthly_fig.update_xaxes(
    tickmode="linear",
    dtick="M3",
    tickangle=45)

Top_10_products_DataFrame=df.groupby(df["Product Name"])["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
products_fig=px.bar(Top_10_products_DataFrame,y="Product Name",x="Sales",orientation="h",title="Top 10 Products")

scatter_fig=px.scatter(df,x="Sales",y="Profit",color="Category",size="Quantity",title="Sales vs Profit Analysis")

def selector(Region=None,Segment=None,Category=None):
        filtered_df=df.copy()
        if Region is not None:
            filtered_df=filtered_df[filtered_df['Region']==Region]
        if Segment is not None:
            filtered_df=filtered_df[filtered_df['Segment']==Segment]
        if Category is not None:
            filtered_df=filtered_df[filtered_df['Category']==Category]
        return filtered_df  


# Export Charts

category_fig.write_html("./exports/category_sales_profit.html")

monthly_fig.write_html("./exports/monthly_sales_profit.html")

products_fig.write_html("./exports/top_10_products.html")

scatter_fig.write_html("./exports/sales_vs_profit.html")

app.layout = html.Div([
    html.H1(
        "Superstore Executive Dashboard",
        style={"textAlign": "center", "marginBottom": "30px"}
    ),

    html.Div([
        html.Div([
            html.H4("Total Sales"),
            html.H2(f"${Total_Sales:,.2f}",id="total-sales")
        ], style={
            "backgroundColor": "#e8f0fe",
            "padding": "20px",
            "borderRadius": "10px",
            "textAlign": "center",
            "flex": "1"
        }),

        html.Div([
            html.H4("Total Profit"),
            html.H2(f"${Total_Profit:,.2f}",id="total-profit")
        ], style={
            "backgroundColor": "#e8f5e9",
            "padding": "20px",
            "borderRadius": "10px",
            "textAlign": "center",
            "flex": "1"
        }),

        html.Div([
            html.H4("Profit Margin"),
            html.H2(f"{Profit_Margin:.2f}%",id="profit-margin")
        ], style={
            "backgroundColor": "#fff3e0",
            "padding": "20px",
            "borderRadius": "10px",
            "textAlign": "center",
            "flex": "1"
        }),

        html.Div([
            html.H4("Total Orders"),
            html.H2(f"{Total_Orders:,}",id="total-orders")
        ], style={
            "backgroundColor": "#f3e5f5",
            "padding": "20px",
            "borderRadius": "10px",
            "textAlign": "center",
            "flex": "1"
        })

    ], style={
        "display": "flex",
        "gap": "20px",
        "margin": "20px"
    }),
    html.Div([
    dcc.Dropdown(
        id="region-filter",
        options=[
            {"label": r, "value": r}
            for r in sorted(df["Region"].unique())
        ],
        placeholder="Select Region",
        value=None,
        clearable=True
    ),

    dcc.Dropdown(
        id="category-filter",
        options=[
            {"label": c, "value": c}
            for c in sorted(df["Category"].unique())
        ],
        placeholder="Select Category",
        value=None,
        clearable=True
    ),

    dcc.Dropdown(
        id="segment-filter",
        options=[
            {"label": s, "value": s}
            for s in sorted(df["Segment"].unique())
        ],
        placeholder="Select Segment",
        value=None,
        clearable=True
    )
    ], style={
        "display": "flex",
        "gap": "20px",
        "margin": "20px"
    }),

    html.Div([
        html.Div([
            dcc.Graph(
                id="category-chart",
                figure=category_fig
            ),
            dcc.Graph(
                id="monthly-chart",
                figure=monthly_fig
            )
        ], style={
            "display": "grid",
            "gridTemplateColumns": "1fr 1fr",
            "gap": "20px",
            "margin": "20px"
        }),

        html.Div([
            dcc.Graph(
                id="products-chart",
                figure=products_fig
            ),
            dcc.Graph(
                id="scatter-chart",
                figure=scatter_fig
            )
        ], style={
            "display": "grid",
            "gridTemplateColumns": "1fr 1fr",
            "gap": "20px",
            "margin": "20px"
        })
    ])

])    


@app.callback(
    Output("total-sales", "children"),
    Output("total-profit", "children"),
    Output("profit-margin", "children"),
    Output("total-orders", "children"),

    Output("category-chart", "figure"),
    Output("monthly-chart", "figure"),
    Output("products-chart", "figure"),
    Output("scatter-chart", "figure"),

    Input("region-filter", "value"),
    Input("segment-filter", "value"),
    Input("category-filter", "value")
)
def update_dashboard(region, segment, category):

    filtered_df = selector(region, segment, category)

    # KPI Calculations
    Total_Sales = filtered_df["Sales"].sum()
    Total_Profit = filtered_df["Profit"].sum()

    Profit_Margin = (
        (Total_Profit / Total_Sales) * 100
        if Total_Sales != 0 else 0
    )

    Total_Orders = filtered_df["Order ID"].nunique()

    # Category Chart
    category_data = filtered_df.groupby(
        "Category"
    )[["Sales", "Profit"]].sum().reset_index()

    category_fig = px.bar(
        category_data,
        x="Category",
        y=["Sales", "Profit"],
        title="Sales by Category"
    )

    # Monthly Chart
    monthly_data = filtered_df.assign(
        Month=filtered_df["Order Date"].dt.strftime('%Y-%m')
    ).groupby("Month")[["Sales", "Profit"]].sum().reset_index()

    monthly_fig = px.line(
        monthly_data,
        x="Month",
        y=["Sales", "Profit"],
        title="Monthly Sales & Profit Trend"
    )

    monthly_fig.update_xaxes(
        tickmode="linear",
        dtick="M3",
        tickangle=45
    )

    # Top 10 Products
    top_10_data = (
        filtered_df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    products_fig = px.bar(
        top_10_data,
        y="Product Name",
        x="Sales",
        orientation="h",
        title="Top 10 Products"
    )

    # Scatter Chart
    scatter_fig = px.scatter(
        filtered_df,
        x="Sales",
        y="Profit",
        color="Category",
        size="Quantity",
        title="Sales vs Profit Analysis"
    )

    return (
        f"${Total_Sales:,.2f}",
        f"${Total_Profit:,.2f}",
        f"{Profit_Margin:.2f}%",
        f"{Total_Orders:,}",

        category_fig,
        monthly_fig,
        products_fig,
        scatter_fig
    )


if __name__=="__main__":
    app.run(debug=True)
