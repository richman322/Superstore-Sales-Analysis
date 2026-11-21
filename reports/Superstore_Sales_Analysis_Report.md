# Superstore Sales Analysis & Business Intelligence Report

**Project:** Superstore Sales Analysis\
**Dataset:** Superstore\
**Records:** 9,994\
**Original Columns:** 21\
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly and
Jupyter Notebook

------------------------------------------------------------------------

## Table of Contents

1.  Data Understanding
2.  Data Cleaning
3.  Data Transformation & Feature Engineering
4.  Descriptive Statistics & Exploratory Data Analysis
5.  Revenue & Profitability Analysis
6.  Product & Category Analysis
7.  Customer, Segment, Regional & Shipping Analysis
8.  Time-Based Analysis
9.  Data Visualization
10. Seaborn Visualizations

------------------------------------------------------------------------

## Report Notes

This consolidated report combines the project's original ten part-wise
reports into one document. The analytical findings, tables, terminology
and reported values have been retained from those source reports. The
sections are arranged in the original project sequence. Where a source
section reports a specific result, that result is presented as recorded
in that section.

------------------------------------------------------------------------

# Part 1 --- 1. Data Understanding

**Project Title:** Comprehensive Superstore Sales Analysis and Business
Intelligence

**Dataset:** Superstore (2015--2018)\
**Total Records:** 9,994\
**Total Columns:** 21\
**Analysis Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn and
Plotly

------------------------------------------------------------------------

## 1.1 Project Structure

### Purpose

To establish an organized project environment for data analysis,
visualization and documentation.

### Method

The project is organized into separate directories for the original
dataset, notebooks, visualizations, dashboard and reports.

### Expected Outcome

A structured working environment that supports project maintenance and
reproducibility.

## 1.2 Dataset Loading

### Purpose

To import the Superstore dataset into the Python environment for further
analysis.

### Method

The CSV dataset was loaded using the Pandas library.

### Observation

The dataset contains 9,994 records and 21 columns, representing retail
sales transactions and related business information.

## 1.3 Dataset Preview

### Purpose

To understand the general structure and contents of the dataset.

### Method

The first five, last five and randomly selected records were inspected.

### Interpretation

The dataset contains information about customer orders, products,
geographical locations, sales, discounts, quantities and profits.

Each row represents an order line item rather than necessarily
representing an independent customer order.

## 1.4 Dataset Structure

The dataset contains the following types of information:

-   Numerical data: Sales, Quantity, Discount and Profit.
-   Categorical data: Category, Sub-Category, Region, Segment and Ship
    Mode.
-   Date information: Order Date and Ship Date.
-   Identification fields: Row ID, Order ID, Customer ID and Product ID.
-   Geographical information: Country, State, City and Postal Code.

### Initial Data Types

Sales, Profit and Discount are represented as floating-point values,
while Quantity is stored as an integer.

Order Date and Ship Date were initially loaded as text and require
datetime conversion during data preparation.

## 1.5 Data Dictionary

  Column          Description
  --------------- -----------------------------------------------
  Row ID          Unique row identifier
  Order ID        Customer order identifier
  Order Date      Date of order placement
  Ship Date       Date of shipment
  Ship Mode       Shipping method
  Customer ID     Customer identifier
  Customer Name   Customer name
  Segment         Customer classification
  Country         Customer country
  City            Customer city
  State           Customer state
  Postal Code     Postal area identifier
  Region          Business geographical region
  Product ID      Product identifier
  Category        Main product category
  Sub-Category    Product subcategory
  Product Name    Product description
  Sales           Revenue associated with the order line
  Quantity        Number of units sold
  Discount        Applied discount rate
  Profit          Profit or loss associated with the order line

## 1.6 Categorical Data Exploration

The following unique-value counts were identified:

  Variable         Unique Values
  -------------- ---------------
  Category                     3
  Sub-Category                17
  Region                       4
  Segment                      3
  Ship Mode                    4
  State                       49
  City                       531
  Customer ID                793
  Order ID                 5,009

### Interpretation

The dataset supports analysis across multiple business dimensions,
including product performance, customer segments, shipping methods and
geographical regions.

The difference between total rows and unique Order IDs indicates that
some orders contain multiple line items.

## 1.7 Initial Observations

The initial inspection produced the following observations:

1.  The dataset contains 9,994 records and 21 columns.
2.  Sales, Quantity, Discount and Profit are suitable for numerical
    analysis.
3.  Order Date and Ship Date require datetime conversion before
    time-series analysis.
4.  Multiple product categories and subcategories allow detailed product
    performance comparisons.
5.  Customer and geographical information supports segment-wise and
    regional analysis.
6.  Repeated Order IDs may represent multiple products purchased within
    the same order and should not automatically be treated as duplicate
    records.
7.  The dataset contains sufficient information for revenue,
    profitability, discount and historical sales analysis.

## Conclusion

The initial data understanding phase established the structure, content
and analytical potential of the Superstore dataset.

The dataset provides sufficient information to conduct a comprehensive
retail business analysis using Python and

------------------------------------------------------------------------

# Part 2 --- 2. Data Cleaning

**Project:** Superstore Sales Analysis\
**Dataset:** Superstore (2015--2018)

### 1. Dataset Overview

-   Original Rows: 9,994
-   Original Columns: 21
-   Total Missing Values: 0
-   Duplicate Rows: 0
-   Removed Rows: 0

### 2. Missing Values Analysis

No missing values were identified in the dataset. Therefore, no
imputation or row removal was required.

### 3. Duplicate Records Analysis

No complete duplicate rows were found. Therefore, no duplicate records
were removed.

### 4. Data Validation

Numerical, categorical and date columns were inspected. Negative profit
values were treated as valid business losses rather than automatically
classified as data errors.

### 5. Outlier Investigation

The IQR method and Box Plots were used to identify potential outliers.

  Column       Outliers   Percentage
  ---------- ---------- ------------
  Sales           1,167       11.68%
  Profit          1,881       18.82%
  Quantity          170        1.70%
  Discount          856        8.57%

### 6. Important Observations

-   Some high-sales transactions generated negative profit.
-   Significant losses were observed in Machines and Binders.
-   Transactions with 70% and 80% discounts showed substantial negative
    profits.
-   Unusual values may represent genuine business transactions rather
    than data-entry errors.

### 7. Outlier Treatment Decision

Potential outliers were retained for further investigation. No rows were
removed solely because of their unusual values.

### 8. Final Dataset Status

-   Original Rows: 9,994
-   Final Rows: 9,994
-   Original Columns: 21
-   Removed Rows: 0
-   Missing Values: 0
-   Duplicate Rows: 0

### Conclusion

The dataset was inspected for missing values, duplicate records, invalid
values and potential outliers.

No row removal was required. All 9,994 records were preserved for
subsequent analysis. Identified outliers will be investigated further
during revenue, profitability and discount analysis.

------------------------------------------------------------------------

# Part 3 --- 3. Data Transformation & Feature Engineering

**Project:** Superstore Sales Analysis\
**Original Dataset:** 9,994 Rows × 21 Columns

## 3.1 Date Feature Extraction

The Order Date column was used to extract five additional features:
Year, Month, Quarter, Month Name and Day of Week.

These features were created to support yearly, monthly, quarterly and
weekday-based sales analysis.

The original Order Date column was preserved.

## 3.2 Shipping Duration

A new feature, Shipping Duration, was calculated by subtracting Order
Date from Ship Date.

**Key Results:** - Average Shipping Duration: Approximately 4 days -
Median: 4 days - Minimum: 0 days - Maximum: 7 days - Same-day Shipment
Records: 519 - Negative Shipping Durations: 0

The middle 50% of records had shipping durations ranging from 3 to 5
days.

These findings provide a foundation for evaluating order-processing
efficiency across different shipping modes.

## 3.3 Profit Margin Calculation

Profit Margin was calculated using the following formula:

**Profit Margin (%) = (Profit / Sales) × 100**

**Statistical Results:**

  Statistic                 Result
  ----------------------- --------
  Average Profit Margin     12.03%
  Median Profit Margin         27%
  Minimum Profit Margin      -275%
  Maximum Profit Margin        50%

**Profit Margin Distribution:**

  Status       Records   Percentage
  ---------- --------- ------------
  Positive       8,058       80.63%
  Negative       1,871       18.72%
  Zero              65        0.65%

Further investigation identified four transactions with a minimum profit
margin of -275%. All four transactions had an 80% discount, although
their actual monetary losses differed.

The average transaction-level profit margin should not be confused with
the company's overall profit margin, which requires dividing total
Profit by total Sales.

## 3.4 Sales Per Unit

A new numerical feature, Sales Per Unit, was created using the following
formula:

**Sales Per Unit = Sales / Quantity**

The Quantity column was checked to avoid division-by-zero errors. Its
previously observed minimum value was 1.

This feature represents the average recorded selling price per unit
within each transaction and supports further product pricing analysis.

## 3.5 Profitability Status

A new categorical feature, Profitability Status, was created using the
Profit column.

Transactions were classified into three categories:

-   **Profit:** Profit greater than zero.
-   **Loss:** Profit less than zero.
-   **Break-even:** Profit equal to zero.

This classification enables straightforward comparisons of profitable,
loss-making and break-even transactions across product categories,
regions and customer segments.

## 3.6 Discount Band Classification

A new categorical feature, Discount Bands, was created using the
following project-defined boundaries:

  Discount Band   Range
  --------------- -----------------------------
  No Discount     Exactly 0%
  Low             Greater than 0% up to 20%
  Medium          Greater than 20% up to 50%
  High            Greater than 50% up to 100%

**Classification Results:**

  Discount Band       Records   Percentage
  --------------- ----------- ------------
  No Discount           4,798       48.01%
  Low                   3,803       38.05%
  Medium                  537        5.37%
  High                    856        8.57%
  **Total**         **9,994**     **100%**

All records were successfully classified. Most transactions (86.06%)
belonged to the No Discount or Low Discount categories.

## Final Transformation Summary

The data transformation phase introduced the following nine analytical
features:

1.  Year
2.  Month
3.  Quarter
4.  Month Name
5.  Day of Week
6.  Shipping Duration
7.  Profit Margin
8.  Sales Per Unit
9.  Profitability Status
10. Discount Bands

These features enhance the dataset's suitability for time-series
analysis, shipping performance evaluation, product pricing analysis,
profitability assessment and discount-related business investigations.

The original dataset was preserved, and no rows were intentionally
removed during this phase.

**Final Working Dataset:** 9,994 rows and 31 columns, assuming all ten
features were added without removing or replacing existing columns.

## Conclusion

The data transformation and feature engineering phase successfully
converted existing transactional information into additional analytical
features.

The resulting working dataset provides a stronger foundation for
Exploratory Data Analysis (EDA), statistical visualization and business
intelligence.

The next phase will focus on identifying distributions, relationships,
trends and patterns within the transformed data.

------------------------------------------------------------------------

# Part 4 --- 4. Descriptive Statistics & Exploratory Data Analysis

## 4.1 Introduction

This section presents the descriptive statistics and exploratory data
analysis of the Superstore Sales dataset. The purpose is to understand
numerical distributions, categorical frequencies, and relationships
between important business variables.

The analysis covers 9,994 transaction records and focuses on Sales,
Quantity, Discount, Profit, Region, Category, Segment, and Ship Mode.

No transaction records were removed during the preceding data-cleaning
process.

------------------------------------------------------------------------

## 4.2 Numerical Summary

Descriptive statistics were calculated for four key numerical variables.

  Statistic                  Sales   Quantity   Discount      Profit
  -------------------- ----------- ---------- ---------- -----------
  Count                      9,994      9,994      9,994       9,994
  Mean                      229.86       3.79     0.1562       28.66
  Standard Deviation        623.25       2.23     0.2065      234.26
  Minimum                    0.444          1          0   -6,599.98
  25th Percentile            17.28          2          0        1.73
  Median                     54.49          3       0.20        8.67
  75th Percentile           209.94          5       0.20       29.36
  Maximum                22,638.48         14       0.80    8,399.98

### Interpretation

-   The average transaction Sales value is 229.86, substantially higher
    than the median of 54.49. This indicates that relatively large
    transactions influence the average.
-   The average Quantity is approximately 3.79 units, while the median
    is 3 units.
-   The average Discount is approximately 15.62%, and the median
    Discount is 20%.
-   Profit exhibits considerable variation, ranging from a loss of
    6,599.98 to a positive profit of 8,399.98.
-   The standard deviations of Sales and Profit indicate substantial
    variability in transaction-level financial performance.

## 4.3 Distribution Analysis

The distributions of Sales and Profit were examined using skewness,
mean, median, and extreme transaction values.

  Variable       Mean   Median             Skewness Distribution
  ---------- -------- -------- -------------------- ---------------------
  Sales        229.86    54.49   Approximately 13.0 Highly right-skewed
  Profit        28.66     8.67    Approximately 7.6 Highly right-skewed

Both variables have positive skewness, indicating long right tails.

For Sales, the large difference between the mean and median suggests
that a relatively small number of high-value transactions substantially
influence the average.

Profit also has a right-skewed distribution, although the dataset
contains both profitable and loss-making transactions.

### Extreme-Value Observations

The following observations were identified during the investigation of
extreme transaction values:

-   The transaction with the highest Profit also recorded high Sales.
-   The minimum-Sales transaction involved a single unit and a high
    discount.
-   The transaction with the largest monetary loss involved a 70%
    discount and a quantity of five units.

These observations demonstrate why extreme values should be investigated
rather than automatically removed. They represent potentially meaningful
business events.

## 4.4 Categorical Exploration

Categorical frequency analysis was conducted to examine the distribution
of transaction records across Region, Category, Segment, and Ship Mode.

### Regional Distribution

  Region        Frequency   Percentage
  ----------- ----------- ------------
  West              3,203       32.04%
  East              2,848       28.50%
  Central           2,323       23.24%
  South             1,620       16.21%
  **Total**     **9,994**     **100%**

West has the highest representation, while South has the lowest.

### Product Category Distribution

  Category            Frequency   Percentage
  ----------------- ----------- ------------
  Office Supplies         6,026       60.30%
  Furniture               2,121       21.22%
  Technology              1,847       18.48%
  **Total**           **9,994**     **100%**

Office Supplies accounts for approximately three-fifths of all
transaction rows, making it the most frequently recorded product
category.

### Customer Segment Distribution

  Segment         Frequency   Percentage
  ------------- ----------- ------------
  Consumer            5,191       51.94%
  Corporate           3,020       30.22%
  Home Office         1,783       17.84%
  **Total**       **9,994**     **100%**

Consumer is the most frequently represented customer segment, accounting
for more than half of the dataset.

### Shipping Mode Distribution

  Ship Mode          Frequency   Percentage
  ---------------- ----------- ------------
  Standard Class         5,968       59.72%
  Second Class           1,945       19.46%
  First Class            1,538       15.39%
  Same Day                 543        5.43%
  **Total**          **9,994**     **100%**

Standard Class is the most frequently recorded shipping method, whereas
Same Day has the lowest frequency.

**Interpretation note:** These percentages represent transaction-row
frequencies. A higher frequency does not necessarily indicate higher
revenue, greater profitability, or a larger number of unique orders.

*Percentages are rounded to two decimal places; totals may differ
slightly from 100% due to rounding.*

## 4.5 Correlation Analysis

Pearson correlation analysis was performed to examine linear
associations among Sales, Quantity, Discount, and Profit.

### Correlation Matrix

  Variable      Sales   Quantity   Discount   Profit
  ---------- -------- ---------- ---------- --------
  Sales         1.000      0.201     -0.028    0.479
  Quantity      0.201      1.000      0.009    0.066
  Discount     -0.028      0.009      1.000   -0.219
  Profit        0.479      0.066     -0.219    1.000

### Interpretation of Relationships

  Variable Pair             Correlation Interpretation
  ----------------------- ------------- ---------------------------------
  Sales and Profit               +0.479 Moderate positive association
  Sales and Quantity             +0.201 Weak positive association
  Sales and Discount             -0.028 Negligible negative association
  Quantity and Profit            +0.066 Negligible positive association
  Quantity and Discount          +0.009 Negligible association
  Discount and Profit            -0.219 Weak negative association

Sales and Profit demonstrate the strongest linear association among the
examined variable pairs.

Discount and Profit show a weak negative association, indicating that
higher discounts tend to be associated with lower transaction profits
within the dataset.

However, these findings are observational. **Correlation does not
establish causation**, and no causal conclusions are drawn from the
correlation matrix.

Furthermore, a negligible Pearson correlation does not necessarily
indicate the absence of every possible relationship; it indicates little
or no observed linear association.

------------------------------------------------------------------------

## 4.6 EDA Summary --- Key Patterns and Evidence

The following seven findings summarize the major patterns identified
during exploratory analysis.

### Finding 1: Sales Are Highly Right-Skewed

**Pattern:** Most transaction Sales values are relatively small compared
with the highest recorded values.

**Evidence:** Mean Sales is 229.86, median Sales is 54.49, and skewness
is approximately +13.0.

### Finding 2: Profit Shows Significant Variation

**Pattern:** Transaction-level profitability varies considerably, and
the Profit distribution is right-skewed.

**Evidence:** Profit ranges from -6,599.98 to +8,399.98, with skewness
of approximately +7.6.

### Finding 3: West Has the Highest Regional Representation

**Pattern:** West contributes the largest share of transaction records,
while South contributes the smallest.

**Evidence:** West accounts for 3,203 records (32.04%), compared with
South's 1,620 records (16.21%).

### Finding 4: Office Supplies Dominates Transaction Frequency

**Pattern:** Office Supplies is the most frequently recorded product
category.

**Evidence:** It represents 6,026 records, approximately 60.30% of the
dataset.

### Finding 5: Consumer Is the Largest Customer Segment by Frequency

**Pattern:** Consumer transactions account for more than half of all
transaction records.

**Evidence:** The Consumer segment contains 5,191 records (51.94%).

### Finding 6: Standard Class Is the Most Frequently Used Shipping Mode

**Pattern:** Standard Class has a considerably higher recorded frequency
than other shipping methods.

**Evidence:** Standard Class accounts for 5,968 records (59.72%),
whereas Same Day accounts for 543 records (5.43%).

### Finding 7: Sales--Profit and Discount--Profit Show Different Associations

**Pattern:** Sales and Profit have a moderate positive linear
association, while Discount and Profit have a weak negative association.

**Evidence:** Their respective Pearson correlation coefficients are
+0.479 and -0.219.

These findings identify statistical associations rather than causal
relationships.

------------------------------------------------------------------------

## 4.7 Overall Conclusion

The exploratory analysis reveals substantial variation in
transaction-level Sales and Profit, with both variables displaying
highly right-skewed distributions.

Office Supplies, Consumer, West, and Standard Class are the most
frequently represented groups within their respective categorical
dimensions.

Correlation analysis identifies a moderate positive association between
Sales and Profit and a weak negative association between Discount and
Profit.

These results provide a statistical foundation for subsequent visual
analysis and deeper investigation of sales performance, profitability,
discounts, product categories, and customer segments.

The findings should be interpreted as descriptive observations rather
than evidence of causal relationships.

------------------------------------------------------------------------

# Part 5 --- 5. Revenue & Profitability Analysis

## 5.1 Overall Business KPIs

The overall business performance was evaluated using key performance
indicators (KPIs).

  KPI                               Result
  ----------------------- ----------------
  Total Sales               \$2,297,200.86
  Total Profit                \$286,397.02
  Total Quantity Sold               37,873
  Unique Orders                      5,009
  Overall Profit Margin             12.47%

The overall profit margin was calculated by dividing total profit by
total sales and multiplying by 100.

**Key Insight:** The business generated approximately \$2.30 million in
sales and \$286,397 in net profit, with an overall profit margin of
12.47%.

## 5.2 Transaction Analysis

Transaction-level analysis was performed to understand sales
distribution and order values.

  Metric                                           Result
  -------------------------------------- ----------------
  Average Sales per Transaction                  \$229.86
  Average Order Value                            \$458.61
  Highest Individual Transaction Sales        \$22,638.48
  Lowest Individual Transaction Sales             \$0.444
  Highest-Sales Order ID                   CA-2014-145317
  Lowest-Sales Order ID                    CA-2017-124114

Average Order Value was calculated by first grouping sales by Order ID
and then calculating the average of the order totals.

**Key Insight:** Average Order Value (\$458.61) is higher than average
sales per transaction (\$229.86), because an order can contain multiple
transactions or product records.

## 5.3 Profit and Loss Analysis

Transactions were classified into three categories using the existing
Profitability Status feature.

  -----------------------------------------------------------------------------------------------
  Status         Transaction                Sales          Sales        Profit/Loss   Transaction
                       Count                        Contribution                       Percentage
  ------------ ------------- -------------------- -------------- ------------------ -------------
  Profit               8,058       \$1,800,806.86         78.40%       \$442,528.31        80.63%

  Loss                 1,871         \$468,707.20         20.40%      -\$156,131.29        18.72%

  Break-even              65          \$27,686.85          1.21%             \$0.00          0.65

  **Total**        **9,994**   **\$2,297,200.86**       **100%**   **\$286,397.02**      **100%**
  -----------------------------------------------------------------------------------------------

**Key Insights:** - Approximately 80.63% of transactions were
profitable. - Around 18.72% of transactions resulted in losses. -
Break-even transactions accounted for approximately 0.65% of all
transactions. - Profitable transactions generated \$442,528.31 in total
profit, while loss-making transactions resulted in \$156,131.29 in
losses. - After accounting for losses, the business achieved a net
profit of \$286,397.02.

## 5.4 Sales vs Profit

The 15 transactions with the highest sales were examined to understand
the relationship between sales and profitability.

**Key Observations:**

1.  High-sales transactions with medium discounts (20%--50%) can also
    result in losses.
2.  Some high-sales transactions generate substantial profits,
    demonstrating that high sales can also be accompanied by strong
    profitability.
3.  High sales do not always guarantee profitability, as some high-sales
    transactions have negative profit margins.

**Key Insight:** Sales volume alone does not determine business
profitability. Discount levels and other transaction factors should also
be considered when evaluating financial performance.

## Part 5 Conclusion

The revenue and profitability analysis shows that the business generated
substantial sales and achieved a positive overall profit margin.
However, a considerable number of transactions resulted in losses.
Transaction-level analysis also demonstrated that high sales do not
necessarily guarantee high profits. Therefore, monitoring discounts,
transaction profitability, and overall profit margins is important for
improving business performance.

------------------------------------------------------------------------

# Part 6 --- 6. Product & Category Analysis

## 1. Introduction

The objective of this analysis is to evaluate product and category
performance using Sales, Profit, Quantity, and Discount metrics.

This analysis identifies: - Top 10 products by revenue. - Top 10
products by quantity sold. - Top 10 profitable products. - Top 10
loss-making products. - Category-level sales, profit, quantity, profit
margin, and revenue share. - Sub-category performance and
revenue-versus-volume leaders.

Pandas `groupby()`, `sum()`, `mean()`, and `sort_values()` were used to
perform the analysis.

## 2. Top 10 Products by Revenue

Products were grouped by Product Name, and their total Sales were
calculated. The results were sorted in descending order to identify the
ten highest-revenue products.

  -----------------------------------------------------------------------
                       Rank Product Name                      Total Sales
  ------------------------- ------------------- -------------------------
                          1 Canon imageCLASS                    61,599.82
                            2200 Advanced       
                            Copier              

                          2 Fellowes PB500                      27,453.38
                            Electric Punch      
                            Plastic Comb        
                            Binding Machine     
                            with Manual Bind    

                          3 Cisco TelePresence                  22,638.48
                            System EX90         
                            Videoconferencing   
                            Unit                

                          4 HON 5400 Series                     21,870.58
                            Task Chairs for Big 
                            and Tall            

                          5 GBC DocuBind TL300                  19,823.48
                            Electric Binding    
                            System              

                          6 GBC Ibimaster 500                   19,024.50
                            Manual ProClick     
                            Binding System      

                          7 Hewlett Packard                     18,839.69
                            LaserJet 3310       
                            Copier              

                          8 HP Designjet T520                   18,374.90
                            Inkjet Large Format 
                            Printer - 24" Color 

                          9 GBC DocuBind P400                   17,965.07
                            Electric Binding    
                            System              

                         10 High Speed                          17,030.31
                            Automatic Electric  
                            Letter Opener       
  -----------------------------------------------------------------------

**Key Observation:** Canon imageCLASS 2200 Advanced Copier generated the
highest total sales, approximately 61,599.82, making it the leading
product by revenue.

## 3. Top 10 Products by Quantity Sold

Total Quantity was aggregated for each product to identify the products
with the highest sales volume.

    Rank Product Name                                                   Total Quantity
  ------ ------------------------------------------------------------ ----------------
       1 Staples                                                                   215
       2 Staple envelope                                                           170
       3 Easy-staple paper                                                         150
       4 Staples in misc. colors                                                    86
       5 KI Adjustable-Height Table                                                 74
       6 Storex Dura Pro Binders                                                    71
       7 Avery Non-Stick Binders                                                    71
       8 GBC Premium Transparent Covers with Diagonal Lined Pattern                 67
       9 Situations Contoured Folding Chairs, 4/Set                                 64
      10 Staple-based wall hangings                                                 62

**Key Observation:** Staples ranked first with 215 units sold, followed
by Staple envelope with 170 units. These products lead in sales volume
but are not necessarily the highest-revenue products.

## 4. Product Profitability Analysis

Total Profit was calculated for each product to identify the most
profitable and loss-making products.

### 4.1 Top 10 Profitable Products

  -----------------------------------------------------------------------
                       Rank Product Name                     Total Profit
  ------------------------- ------------------- -------------------------
                          1 Canon imageCLASS                    25,199.93
                            2200 Advanced       
                            Copier              

                          2 Fellowes PB500                       7,753.04
                            Electric Punch      
                            Plastic Comb        
                            Binding Machine     
                            with Manual Bind    

                          3 Hewlett Packard                      6,983.88
                            LaserJet 3310       
                            Copier              

                          4 Canon PC1060                         4,570.93
                            Personal Laser      
                            Copier              

                          5 HP Designjet T520                    4,094.98
                            Inkjet Large Format 
                            Printer - 24" Color 

                          6 Ativa V4110MDD                       3,772.95
                            Micro-Cut Shredder  

                          7 3D Systems Cube                      3,717.97
                            Printer, 2nd        
                            Generation, Magenta 

                          8 Plantronics Savi                     3,696.28
                            W720 Multi-Device   
                            Wireless Headset    
                            System              

                          9 Ibico EPK-21                         3,345.28
                            Electric Binding    
                            System              

                         10 Zebra ZM400 Thermal                  3,343.54
                            Label Printer       
  -----------------------------------------------------------------------

**Key Observation:** Canon imageCLASS 2200 Advanced Copier was also the
most profitable product, generating approximately 25,199.93 in total
profit.

### 4.2 Top 10 Loss-Making Products

Products were sorted in ascending order of total Profit to identify the
products with the greatest overall losses.

  -----------------------------------------------------------------------
                       Rank Product Name                     Total Profit
  ------------------------- ------------------- -------------------------
                          1 Cubify CubeX 3D                     -8,879.97
                            Printer Double Head 
                            Print               

                          2 Lexmark MX611dhe                    -4,589.97
                            Monochrome Laser    
                            Printer             

                          3 Cubify CubeX 3D                     -3,839.99
                            Printer Triple Head 
                            Print               

                          4 Chromcraft                          -2,876.12
                            Bull-Nose Wood Oval 
                            Conference Tables & 
                            Bases               

                          5 Bush Advantage                      -1,934.40
                            Collection          
                            Racetrack           
                            Conference Table    

                          6 GBC DocuBind P400                   -1,878.17
                            Electric Binding    
                            System              

                          7 Cisco TelePresence                  -1,811.08
                            System EX90         
                            Videoconferencing   
                            Unit                

                          8 Martin Yale                         -1,299.18
                            Chadless Opener     
                            Electric Letter     
                            Opener              

                          9 Balt Solid Wood                     -1,201.06
                            Round Tables        

                         10 BoxOffice By Design                 -1,148.44
                            Rectangular and     
                            Half-Moon Meeting   
                            Room Tables         
  -----------------------------------------------------------------------

**Key Observation:** Cubify CubeX 3D Printer Double Head Print recorded
the largest total loss of approximately 8,879.97.

Some products appear in both the high-revenue and loss-making rankings.
For example, Cisco TelePresence System EX90 and GBC DocuBind P400
generated substantial sales but had negative total profits. This
demonstrates that high revenue does not always guarantee profitability.

## 5. Category-Level Analysis

The dataset contains three main categories: Furniture, Office Supplies,
and Technology.

The following metrics were calculated for each category: - Total Sales -
Total Profit - Total Quantity - Category Profit Margin - Category
Revenue Share

### 5.1 Category Performance Comparison

  Category            Total Sales   Total Profit   Quantity
  ----------------- ------------- -------------- ----------
  Furniture            741,999.80      18,451.27      8,028
  Office Supplies      719,047.03     122,490.80     22,906
  Technology           836,154.03     145,454.95      6,939

### 5.2 Category Profit Margin and Revenue Share

  Category            Profit Margin   Revenue Share
  ----------------- --------------- ---------------
  Furniture                   2.49%          32.30%
  Office Supplies            17.04%          31.30%
  Technology                 17.40%          36.40%

**Key Observations:**

1.  **Technology** generated the highest revenue, approximately
    836,154.03, and contributed around 36.40% of overall revenue.
2.  **Office Supplies** recorded the highest sales volume, with 22,906
    units.
3.  **Technology** achieved the highest category profit, approximately
    145,454.95.
4.  **Furniture** generated approximately 742,000 in sales but had a
    relatively low profit margin of 2.49%.
5.  Office Supplies and Technology had considerably higher profit
    margins than Furniture.

**Business Insight:** Furniture contributes a substantial share of
revenue but has a comparatively low profit margin. Its pricing,
discounting, and cost structure may deserve further investigation.

## 6. Sub-Category Analysis

A detailed analysis was performed for all 17 sub-categories using total
Sales, total Profit, total Quantity, and average Discount.

Average Discount was calculated using the mean discount for each
sub-category and converted into percentage form.

### 6.1 Sub-Category Performance Table

  --------------------------------------------------------------------------
  Sub-Category      Total Sales   Total Profit       Quantity        Average
                                                                    Discount
  -------------- -------------- -------------- -------------- --------------
  Accessories        167,380.32      41,936.64          2,976          7.85%

  Appliances         107,532.16      18,138.01          1,729         16.65%

  Art                 27,118.79       6,527.79          3,000          7.49%

  Binders            203,412.73      30,221.76          5,974         37.23%

  Bookcases          114,880.00      -3,472.56            868         21.11%

  Chairs             328,449.10      26,590.17          2,356         17.02%

  Copiers            149,528.03      55,617.82            234         16.18%

  Envelopes           16,476.40       6,964.18            906          8.03%

  Fasteners            3,024.28         949.52            914          8.20%

  Furnishings         91,705.16      13,059.14          3,563         13.83%

  Labels              12,486.31       5,546.25          1,400          6.87%

  Machines           189,238.63       3,384.76            440         30.61%

  Paper               78,479.21      34,053.57          5,178          7.49%

  Phones             330,007.05      44,515.73          3,289         15.46%

  Storage            223,843.61      21,278.83          3,158          7.47%

  Supplies            46,673.54      -1,189.10            647          7.68%

  Tables             206,965.53     -17,725.48          1,241         26.13%
  --------------------------------------------------------------------------

### 6.2 Sub-Category Insights

1.  **Phones** generated the highest sub-category revenue, approximately
    330,007.05.
2.  **Copiers** generated the highest total profit, approximately
    55,617.82, despite selling only 234 units.
3.  **Binders** recorded the highest sales volume with 5,974 units.
4.  **Tables** recorded the largest sub-category loss, approximately
    17,725.48.
5.  Bookcases and Supplies also recorded negative total profits.
6.  **Machines** generated approximately 189,238.63 in sales but only
    3,384.76 in profit, indicating comparatively low profitability.
7.  Binders had the highest average discount among the listed
    sub-categories, approximately 37.23%.

These results highlight considerable differences in revenue, sales
volume, discount levels, and profitability across sub-categories.

## 7. Revenue vs Volume Analysis

The leading sub-categories were compared using three separate metrics:
total Quantity, total Sales, and total Profit.

### 7.1 Performance Leaders

  Metric                 Leading Sub-Category         Result
  ---------------------- ---------------------- ------------
  Highest Units Sold     Binders                       5,974
  Highest Revenue        Phones                   330,007.05
  Highest Total Profit   Copiers                   55,617.82

### 7.2 Business Insights

-   **Binders** lead in units sold, indicating the highest sales volume.
-   **Phones** lead in revenue generation, making them the largest
    contributor to sub-category sales.
-   **Copiers** lead in total profit, despite having a much lower
    quantity sold than Binders or Phones.

The difference between these leaders demonstrates that selling more
units does not necessarily generate the highest revenue or profit.

A sub-category can generate higher profitability even with a lower sales
volume, depending on its selling price, costs, and discount structure.

## 8. Overall Business Insights

The analysis produced the following important findings:

1.  Canon imageCLASS 2200 Advanced Copier was the leading product in
    both total sales and total profit.
2.  Staples recorded the highest product-level quantity sold, with 215
    units.
3.  Cubify CubeX 3D Printer Double Head Print recorded the largest
    product-level loss.
4.  Technology generated the highest category revenue and profit.
5.  Office Supplies recorded the highest category-level quantity sold.
6.  Furniture had the lowest category profit margin, approximately
    2.49%.
7.  Phones generated the highest sub-category revenue, while Copiers
    generated the highest sub-category profit.
8.  Binders had the highest sub-category sales volume.
9.  Tables recorded the largest sub-category loss.
10. High revenue or high sales volume does not necessarily indicate high
    profitability.

## 9. Conclusion

The Product & Category Analysis provides a comprehensive understanding
of the dataset's product performance.

The analysis shows that product-level and category-level performance can
differ significantly depending on whether performance is measured
through revenue, quantity, or profit.

Technology was the strongest category in terms of revenue and total
profit, while Office Supplies led in quantity sold. At the sub-category
level, Phones generated the highest revenue, Copiers generated the
highest profit, and Binders recorded the highest quantity sold.

The results also identify loss-making products and sub-categories that
may require further investigation. These findings can support better
decisions regarding product selection, pricing, discount strategies,
inventory management, and profitability improvement.

------------------------------------------------------------------------

# Part 7 --- 7. Customer, Segment, Regional & Shipping Analysis

## 1. Introduction

This part focuses on understanding sales and profitability across
different customers, customer segments, geographical regions, states,
cities, shipping methods, and discount levels.

The objective is to identify valuable customers, evaluate segment and
regional performance, examine shipping patterns, and understand how
different discount levels relate to profitability.

------------------------------------------------------------------------

## 2. Customer Analysis (7.1)

The dataset contains **793 unique customers**.

### Top 10 Customers by Sales

  Customer ID     Total Sales
  ------------- -------------
  SM-20320          25,043.05
  TC-20980          19,052.22
  RB-19360          15,117.34
  TA-21385          14,595.62
  AB-10105          14,473.57
  KL-16645          14,175.23
  SC-20095          14,142.33
  HL-15040          12,873.30
  SE-20110          12,209.44
  CC-12370          12,129.07

**Finding:** SM-20320 generated the highest total sales.

### Top 10 Customers by Profit

  Customer ID     Total Profit
  ------------- --------------
  TC-20980            8,981.32
  RB-19360            6,976.10
  SC-20095            5,757.41
  HL-15040            5,622.43
  AB-10105            5,444.81
  TA-21385            4,703.79
  CM-12385            3,899.89
  KD-16495            3,038.63
  AR-10540            2,884.62
  DR-12940            2,869.08

**Finding:** TC-20980 generated the highest total profit.

### Top Customers by Number of Orders

  Customer ID     Unique Orders
  ------------- ---------------
  EP-13915                   17
  SH-19975                   13
  NS-18640                   13
  PG-18820                   13
  ZC-21910                   13
  EA-14035                   13
  JE-15745                   13
  CK-12205                   13
  AH-10690                   12
  RB-19465                   12

**Finding:** EP-13915 placed the highest number of unique orders, with
17 orders.

### Customer Analysis Insights

-   SM-20320 was the highest revenue-generating customer.
-   TC-20980 was the most profitable customer.
-   EP-13915 placed the highest number of unique orders.
-   The customer generating the highest sales is not necessarily the
    customer generating the highest profit.

------------------------------------------------------------------------

## 3. Customer Segment Analysis (7.2)

Customer performance was evaluated across Consumer, Corporate, and Home
Office segments.

  Segment          Total Sales   Total Profit   Quantity   Profit Margin
  ------------- -------------- -------------- ---------- ---------------
  Consumer        1,161,401.35     134,119.21     19,521          11.55%
  Corporate         706,146.40      91,979.13     11,608          13.03%
  Home Office       429,653.10      60,298.68      6,744          14.03%

### Segment Analysis Insights

-   Consumer generated the highest sales, profit, and quantity.
-   Home Office achieved the highest profit margin at 14.03%.
-   Corporate achieved a 13.03% profit margin.
-   Although Consumer generated the largest overall profit, Home Office
    showed the highest profitability relative to its sales.

------------------------------------------------------------------------

## 4. Regional Analysis (7.3)

Regional performance was analyzed using total sales, profit, quantity,
and profit margin.

  Region      Total Sales   Total Profit   Quantity   Profit Margin
  --------- ------------- -------------- ---------- ---------------
  Central      501,239.89      39,706.36      8,780           7.92%
  East         678,781.24      91,522.78     10,618          13.48%
  South        391,721.91      46,749.43      6,209          11.93%
  West         725,457.82     108,418.45     12,266          14.94%

### Regional Analysis Insights

-   West generated the highest sales, profit, and quantity.
-   West also achieved the highest profit margin at 14.94%.
-   Central had the lowest profit margin at 7.92%.
-   South recorded the lowest sales, profit, and quantity.
-   Central's relatively low profit margin indicates an opportunity for
    further investigation into its product mix, discounts, and pricing
    patterns.

------------------------------------------------------------------------

## 5. State and City Analysis (7.4)

### Top 10 States by Sales

  State            Total Sales
  -------------- -------------
  California        457,687.63
  New York          310,876.27
  Texas             170,188.05
  Washington        138,641.27
  Pennsylvania      116,511.91
  Florida            89,473.71
  Illinois           80,166.10
  Ohio               78,258.14
  Michigan           76,269.61
  Virginia           70,636.72

**Finding:** California generated the highest state-level sales.

### Bottom 10 States by Profit

  State              Total Profit
  ---------------- --------------
  Texas                -25,729.36
  Ohio                 -16,971.38
  Pennsylvania         -15,559.96
  Illinois             -12,607.89
  North Carolina        -7,490.91
  Colorado              -6,527.86
  Tennessee             -5,341.69
  Arizona               -3,427.92
  Florida               -3,399.30
  Oregon                -1,190.47

**Finding:** Texas recorded the largest state-level loss.

### Top 10 Cities by Sales

  City              Total Sales
  --------------- -------------
  New York City      256,368.16
  Los Angeles        175,851.34
  Seattle            119,540.74
  San Francisco      112,669.09
  Philadelphia       109,077.01
  Houston             64,504.76
  Chicago             48,539.54
  San Diego           47,521.03
  Jacksonville        44,713.18
  Springfield         43,054.34

**Finding:** New York City generated the highest city-level sales.

### Bottom 10 Cities by Profit

  City             Total Profit
  -------------- --------------
  Philadelphia       -13,837.77
  Houston            -10,153.55
  San Antonio         -7,299.05
  Lancaster           -7,239.07
  Chicago             -6,654.57
  Burlington          -3,622.88
  Dallas              -2,846.53
  Phoenix             -2,790.88
  Aurora              -2,691.74
  Jacksonville        -2,323.84

**Finding:** Philadelphia recorded the largest city-level loss.

### Geographical Analysis Insights

-   California and New York were the strongest states in terms of sales.
-   Texas recorded the largest state-level loss.
-   New York City was the leading city by sales.
-   Philadelphia recorded the largest city-level loss.
-   Texas and Philadelphia could be investigated further to understand
    their product mix, discount patterns, and pricing performance.

------------------------------------------------------------------------

## 6. Shipping Analysis (7.5)

Shipping performance was evaluated through shipping mode frequency,
average shipping duration, total sales, and total profit.

### Shipping Mode Frequency

  Ship Mode          Number of Records
  ---------------- -------------------
  Standard Class                 5,968
  Second Class                   1,945
  First Class                    1,538
  Same Day                         543

**Finding:** Standard Class was the most frequently used shipping
method, while Same Day was the least frequently used.

### Average Shipping Duration

The overall average shipping duration was:

**3 days, 22 hours, 59 minutes (approximately 4 days).**

### Sales and Profit by Shipping Mode

  Ship Mode           Total Sales   Total Profit
  ---------------- -------------- --------------
  Standard Class     1,358,215.70     164,088.79
  Second Class         459,193.60      57,446.64
  First Class          351,428.40      48,969.84
  Same Day             128,363.10      15,891.76

### Shipping Analysis Insights

-   Standard Class accounted for the highest number of records, sales,
    and profit.
-   Same Day had the lowest frequency, sales, and profit.
-   The overall average shipping duration was approximately four days.
-   Higher total sales and profit for Standard Class should be
    interpreted alongside its higher transaction frequency.

------------------------------------------------------------------------

## 7. Discount Impact Analysis (7.6)

Discount bands were compared using total sales, total profit, profit
margin, and the number of loss-making transactions.

### Discount Band Performance

  Discount Band      Total Sales   Total Profit   Profit Margin
  --------------- -------------- -------------- ---------------
  High                 64,228.74     -76,559.05        -119.20%
  Low                 846,522.20     100,785.47          11.91%
  Medium              298,541.40     -58,817.00         -19.70%
  No Discount       1,087,908.00     320,987.60          29.51%

### Loss Records by Discount Band

  Discount Band     Loss Records
  --------------- --------------
  High                       856
  Low                        523
  Medium                     492
  No Discount                  0
  **Total**            **1,871**

### Discount Analysis Insights

-   No Discount generated the highest total profit and the highest
    profit margin of 29.51%.
-   Low Discount also generated positive profit, with an 11.91% margin.
-   Medium Discount generated a total loss of 58,817.00 and a negative
    margin of -19.70%.
-   High Discount generated a total loss of 76,559.05 and the lowest
    margin of -119.20%.
-   All 856 transactions in the High Discount band were loss-making.
-   No Discount transactions had zero loss-making records.
-   The results show a strong association between higher discount bands
    and weaker profitability in this dataset. However, this analysis
    alone does not establish that discounts caused the losses.

------------------------------------------------------------------------

## 8. Overall Findings and Business Recommendations

### Key Findings

1.  Customer performance varies: the highest-sales customer is different
    from the highest-profit customer.
2.  Consumer is the largest segment by sales and profit, while Home
    Office has the highest profit margin.
3.  West is the strongest region in overall sales, profit, quantity, and
    margin.
4.  California leads state-level sales, while Texas records the largest
    state-level loss.
5.  New York City leads city-level sales, while Philadelphia records the
    largest city-level loss.
6.  Standard Class is the most frequently used shipping method and
    contributes the highest total sales and profit.
7.  No Discount transactions produce the highest profit margin, while
    High Discount transactions are entirely loss-making in this dataset.

### Business Recommendations

-   **Customer Strategy:** Identify and retain high-value customers
    while studying the purchasing patterns of customers with strong
    order frequency.
-   **Segment Strategy:** Maintain the Consumer segment's strong sales
    contribution while exploring ways to improve its profit margin.
-   **Regional Strategy:** Investigate the reasons behind Central's
    lower profit margin and study successful practices in the West.
-   **Geographical Strategy:** Review product mix, pricing, and discount
    patterns in loss-making states and cities, especially Texas and
    Philadelphia.
-   **Shipping Strategy:** Continue evaluating shipping methods using
    both transaction volume and profitability rather than total values
    alone.
-   **Discount Strategy:** Review high-discount transactions carefully,
    as all 856 records in the High Discount band resulted in losses.
    Evaluate discount policies and their impact on individual product
    profitability.

------------------------------------------------------------------------

## 9. Conclusion

Part 7 provided a detailed view of customer behavior, segment
performance, geographical sales distribution, shipping patterns, and
discount-related profitability.

The analysis identified important differences between revenue generation
and profitability. It also highlighted geographical areas and discount
bands that may require further investigation.

Overall, these findings can support better customer management, regional
planning, shipping evaluation, and discount-policy decisions. Further
analysis of product-level performance and transaction characteristics
can help identify the underlying factors behind these patterns.

------------------------------------------------------------------------

# Part 8 --- 8. Time-Based Analysis

## 8.1 Daily Sales and Profit Analysis

Daily analysis was performed by grouping transactions according to
`Order Date` and calculating total Sales and Profit for each date.

The analysis identified the following dates:

  Metric   Best Day          Worst Day
  -------- ----------------- -------------------
  Sales    March 18, 2014    July 19, 2015
  Profit   October 2, 2016   November 25, 2016

**Key Observations:** - The highest daily Sales occurred on March 18,
2014. - The lowest daily Sales occurred on July 19, 2015. - The highest
daily Profit occurred on October 2, 2016. - The lowest daily Profit
occurred on November 25, 2016. - The dates with the highest and lowest
Sales were different from those with the highest and lowest Profit.

This indicates that the highest revenue on a particular day does not
necessarily correspond to the highest profit.

## 8.2 Monthly Sales, Profit and Quantity Analysis

Monthly performance was analyzed by grouping transactions using Year and
Month. This produced 48 monthly records covering January 2014 through
December 2017.

The analysis included: - Total monthly Sales. - Total monthly Profit. -
Total monthly Quantity.

**Key Observations:** - Monthly performance varied across the four
years. - November 2017 recorded the highest monthly Sales. - February
2014 recorded the lowest monthly Sales. - December 2016 recorded the
highest monthly Profit. - January 2015 recorded the lowest monthly
Profit.

Analyzing both Sales and Profit provides a broader understanding of
monthly business performance.

## 8.3 Yearly Sales, Profit and Margin Analysis

The dataset covers four complete calendar years, from January 3, 2014,
to December 30, 2017.

Yearly Sales and Profit were calculated by aggregating transactions by
Year. Profit Margin was calculated using:

**Profit Margin = (Total Profit / Total Sales) × 100**

  Metric   Best Year   Worst Year
  -------- ----------- ------------
  Sales    2017        2015
  Profit   2017        2014

**Key Observations:** - 2017 recorded the highest total Sales and
Profit. - 2015 recorded the lowest total Sales. - 2014 recorded the
lowest total Profit. - Yearly Profit Margin was calculated using
aggregate yearly Sales and Profit rather than averaging individual
transaction margins.

The results indicate differences in yearly revenue and profitability
performance.

## 8.4 Quarterly Sales and Profit Analysis

Quarterly performance was analyzed by grouping data according to Year
and Quarter.

The analysis covered 16 quarterly periods across four years.

**Key Observations:** - Quarterly Sales and Profit were compared across
Q1, Q2, Q3 and Q4. - Q4 recorded the highest Sales in every year from
2014 to 2017. - Q1 recorded the lowest Sales in every year during the
same period. - This repeated pattern indicates stronger sales
performance toward the end of each year.

## 8.5 Month-over-Month (MoM) Growth Analysis

Month-over-Month growth measures the percentage change in Sales compared
with the previous month.

**Formula:**

MoM Growth (%) = ((Current Month Sales - Previous Month Sales) /
Previous Month Sales) × 100

The analysis used the previous month's Sales to calculate the percentage
change.

**Key Results:**

  Metric               Period               Growth
  -------------------- -------------- ------------
  Highest MoM Growth   March 2014       1,132.131%
  Lowest MoM Growth    January 2016       -75.250%

**Key Observations:** - March 2014 recorded the highest positive monthly
growth. - January 2016 recorded the largest monthly decline. - Positive
growth indicates an increase in Sales compared with the previous
month. - Negative growth indicates a decrease in Sales.

The first month was assigned an unavailable value because no previous
month existed. A zero previous-month Sales denominator was also handled
as unavailable to avoid division by zero.

## 8.6 Year-over-Year (YoY) Growth Analysis

Year-over-Year growth measures the percentage change in Sales compared
with the previous year.

**Formula:**

YoY Growth (%) = ((Current Year Sales - Previous Year Sales) / Previous
Year Sales) × 100

**Key Results:**

  Metric               Year       Growth
  -------------------- ------ ----------
  Highest YoY Growth   2016     29.4715%
  Lowest YoY Growth    2015      -2.832%

**Key Observations:** - 2016 recorded the highest annual Sales growth. -
2015 recorded the lowest annual growth, representing a decline compared
with 2014. - The first year, 2014, was assigned an unavailable value
because no previous year was available.

## 8.7 Best and Worst Periods

The best and worst periods were identified using maximum and minimum
Sales, Profit and growth values.

### Monthly Performance

  Metric   Best Period     Worst Period
  -------- --------------- ---------------
  Sales    November 2017   February 2014
  Profit   December 2016   January 2015

### Yearly Performance

  Metric     Best Year   Worst Year
  -------- ----------- ------------
  Sales           2017         2015
  Profit          2017         2014

### Growth Performance

  Metric   Highest Growth            Highest Decline
  -------- ------------------------- -------------------------
  MoM      March 2014 (1,132.131%)   January 2016 (-75.250%)
  YoY      2016 (29.4715%)           2015 (-2.832%)

**Key Observations:** - November 2017 was the strongest month in terms
of Sales. - December 2016 recorded the highest monthly Profit. - 2017
was the strongest year for both Sales and Profit. - Growth analysis
revealed significant changes between consecutive periods. - The highest
or lowest growth period does not necessarily represent the highest or
lowest Sales period because growth measures percentage change rather
than absolute Sales.

## 8.8 Seasonality Analysis

Seasonality analysis was performed to identify repeated monthly and
quarterly Sales patterns across the four years.

### Monthly Sales Patterns

The average Sales for each calendar month were calculated using the four
available years.

  Month         Average Sales
  ----------- ---------------
  January           23,731.21
  February          14,937.81
  March             51,251.37
  April             34,440.53
  May               38,757.20
  June              38,179.67
  July              36,809.52
  August            39,761.02
  September         76,912.49
  October           50,080.75
  November          88,115.27
  December          81,323.38

**Observations:** - November recorded the highest average monthly
Sales. - December recorded the second-highest average monthly Sales. -
February recorded the lowest average monthly Sales. - September also
showed comparatively strong average Sales. - Monthly performance was not
identical across all four years, so these findings indicate recurring
tendencies rather than guaranteed seasonal outcomes.

### Quarterly Sales Patterns

The quarterly comparison revealed a consistent pattern:

-   Q4 recorded the highest quarterly Sales in all four years.
-   Q1 recorded the lowest quarterly Sales in all four years.
-   Q3 generally performed better than Q1 and Q2.
-   Sales performance showed a recurring increase toward the final
    quarter of each year.

**Seasonality Interpretation:**

The repeated Q4 performance provides evidence of a consistent quarterly
Sales pattern in the available dataset. November and December also
recorded the highest average monthly Sales, while February recorded the
lowest average.

These findings suggest stronger Sales activity toward the end of the
year. However, the analysis covers only four years, so the observed
patterns should be treated as historical tendencies rather than
guaranteed future behavior.

## Overall Part 8 Conclusion

The time-based analysis examined daily, monthly, yearly and quarterly
business performance, along with monthly and annual growth rates.

The main findings include:

1.  March 18, 2014, recorded the highest daily Sales.
2.  November 2017 recorded the highest monthly Sales.
3.  December 2016 recorded the highest monthly Profit.
4.  2017 was the strongest year in terms of total Sales and Profit.
5.  Q4 consistently recorded the highest quarterly Sales across all four
    years.
6.  March 2014 recorded the highest MoM growth, while 2016 recorded the
    highest YoY growth.
7.  November had the highest average monthly Sales, whereas February had
    the lowest.

Overall, the analysis highlights variations in business performance over
time and identifies recurring patterns that can support historical
performance evaluation and business planning.

------------------------------------------------------------------------

# Part 9 --- 9. Data Visualization

## 9.1 Category-wise Sales Analysis

A bar chart was created to compare total sales across the three product
categories: Furniture, Office Supplies, and Technology.

**Key Findings:** - Technology generated the highest sales,
approximately **\$836,154.03**. - Furniture generated approximately
**\$741,999.80**. - Office Supplies generated the lowest sales,
approximately **\$719,047.03**.

**Business Insight:**

Technology is the leading category in terms of revenue, while Office
Supplies has the lowest total sales among the three categories. The
comparison helps identify the revenue contribution of each product
category.

## 9.2 Top 10 Products by Sales

A horizontal bar chart was created to visualize the top 10 products
based on total sales.

**Key Findings:** - Canon imageCLASS 2200 Advanced Copier ranked first,
generating approximately **\$61,599.82** in sales. - Fellowes PB500
Electric Punch Plastic Comb Binding Machine ranked second, with
approximately **\$27,453.38**. - Cisco TelePresence System EX90
Videoconferencing Unit ranked third, with approximately **\$22,638.48**.

**Business Insight:**

The Canon imageCLASS 2200 Advanced Copier generated substantially higher
sales than the other top-performing products. Identifying these
high-revenue products can help businesses understand which products
contribute significantly to overall sales.

## 9.3 Monthly Sales Trend

A line chart was created to analyze monthly sales from January 2014 to
December 2017.

The dataset was grouped by Year and Month, producing 48 monthly records.
The MultiIndex was reset, and a datetime column named `Year_Month` was
created to represent each month chronologically.

**Key Findings:** - Monthly sales showed noticeable fluctuations
throughout the four-year period. - November 2017 recorded the highest
monthly sales, approximately **\$118,447.83**. - February 2014 recorded
the lowest monthly sales, approximately **\$4,519.89**. - Sales
generally showed stronger performance toward the end of the year.

**Business Insight:**

The monthly trend highlights variations in sales performance over time.
Higher sales toward the end of the year suggest a recurring historical
pattern, although this observation alone does not guarantee similar
future performance.

## 9.4 Category Revenue Share

A pie chart was created to visualize the percentage contribution of each
category to total revenue.

**Key Findings:** - Technology contributed approximately **36.4%** of
total sales. - Furniture contributed approximately **32.3%**. - Office
Supplies contributed approximately **31.3%**.

**Business Insight:**

Technology contributed the largest share of total revenue, followed by
Furniture and Office Supplies. The revenue-share visualization provides
a clear comparison of the relative contribution of each category.

## 9.5 Discount vs Profit Analysis

A scatter plot was created to examine the relationship between Discount
and Profit.

Each point represents an individual transaction, with Discount on the
X-axis and Profit on the Y-axis.

**Key Findings:** - Transactions with higher discounts (40%--80%) were
predominantly associated with negative profits. - Transactions with
lower discounts (0%--10%) were mostly profitable. - The correlation
coefficient between Discount and Profit was approximately **-0.2195**,
indicating a weak negative linear relationship.

**Business Insight:**

The scatter plot suggests that higher discounts are associated with
lower profitability in many transactions. However, this relationship is
not strong enough to establish that discounts directly cause losses.
Businesses should evaluate discount policies alongside product costs,
pricing, and transaction-level profitability.

## Overall Visualization Summary

The visualizations provided a graphical understanding of category
performance, top-selling products, monthly sales trends, revenue
distribution, and the relationship between discounts and profitability.

The analysis highlighted Technology as the leading revenue-generating
category, Canon imageCLASS 2200 Advanced Copier as the highest-revenue
product, and November 2017 as the strongest month in terms of sales.

The discount-profit scatter plot also highlighted a weak negative
relationship between discounts and profitability, emphasizing the
importance of monitoring discount strategies.

**Conclusion:**

Data visualization made the findings of the exploratory and analytical
stages easier to understand. Different chart types were selected
according to the nature of each analysis, allowing sales patterns,
comparisons, distributions, and relationships to be communicated
effectively.

------------------------------------------------------------------------

# Part 10 --- 10. Seaborn Visualizations

## 10.1 Histogram --- Sales Distribution

A histogram was created using Seaborn to examine the frequency
distribution of Sales.

**Visualization:** - X-axis: Sales - Y-axis: Frequency - Displayed Sales
range: 0--1,000

**Statistical Results:**

  Metric                      Value
  --------------------- -----------
  Minimum Sales               0.444
  First Quartile (Q1)         17.28
  Median (Q2)                 54.49
  Third Quartile (Q3)        209.94
  Mean Sales                 229.86
  Maximum Sales           22,638.48
  Skewness                       13

**Key Findings:** - The highest frequency of transactions was observed
approximately between 0 and 120 in the displayed histogram. -
Transaction frequency gradually decreased as Sales values increased. - A
small number of transactions had extremely high Sales values. - The
distribution was strongly right-skewed. - Some extreme values exceeded
6,000 and extended up to 22,638.48. - The middle 50% of Sales values
were between 17.28 and 209.94.

**Business Insight:**

Most transactions were concentrated within relatively low Sales values,
while a small number of transactions generated substantially higher
sales. The difference between the mean (229.86) and median (54.49),
along with skewness of 13, confirms a strongly right-skewed
distribution.

Note: The histogram was displayed with an X-axis limit of 1,000 to make
the lower Sales range easier to examine. This display limit did not
remove any records from the original dataset.

## 10.2 KDE Plot --- Profit Density

A Kernel Density Estimation (KDE) plot was created to examine the
distribution and density of Profit values.

**Statistical Results:**

  Metric                                        Value
  -------------------------------------- ------------
  Minimum Profit                           -6,599.978
  Maximum Profit                            8,399.976
  Positive Profit Transactions                  8,058
  Negative Profit Transactions                  1,871
  Break-even Transactions                          65
  Approximate Density near Zero Profit          0.008

**Key Findings:** - The KDE curve showed its highest density
approximately around zero Profit. - Profit values extended from
approximately -6,600 to +8,400. - Negative values represented
loss-making transactions. - Positive values represented profitable
transactions. - Zero represented break-even transactions.

**Business Insight:**

The density distribution indicates that many transactions were
concentrated around relatively low Profit values. Although profitable
transactions were more frequent, the dataset also contained a
considerable number of loss-making transactions.

Note: KDE density is not the same as transaction frequency. The
approximate density value of 0.008 is a density estimate near zero
Profit.

## 10.3 Box Plot --- Profit Distribution by Category

A box plot was created to compare Profit distributions across Furniture,
Office Supplies, and Technology.

**Category-wise Median Profit:**

  Category            Median Profit
  ----------------- ---------------
  Furniture                  7.7748
  Office Supplies            6.8824
  Technology                25.0182

**Key Findings:** - Technology had the highest median Profit of
25.0182. - Furniture had the second-highest median Profit of 7.7748. -
Office Supplies had the lowest median Profit of 6.8824. - Prominent
outliers were observed in the Technology category. - Profit values were
distributed both above and below zero.

**Overall Profit Outlier Information:**

The previously calculated IQR analysis identified 1,881 Profit outlier
records across the complete dataset.

**Business Insight:**

Technology showed a higher central Profit value compared with the other
categories. The presence of outliers indicates substantial variation in
transaction-level profitability. These extreme observations may include
both unusually high profits and significant losses.

## 10.4 Count Plot --- Ship Mode and Customer Segment

A count plot was created to compare transaction frequencies across
different Shipping Modes, with Customer Segment represented through
separate colors.

**Segment-wise Shipping Frequency:**

  Ship Mode           Consumer   Corporate   Home Office       Total
  ---------------- ----------- ----------- ------------- -----------
  Standard Class         3,085       1,812         1,071       5,968
  Second Class           1,020         609           316       1,945
  First Class              769         485           284       1,538
  Same Day                 317         114           112         543
  **Total**          **5,191**   **3,020**     **1,783**   **9,994**

**Key Findings:** - Standard Class recorded the highest transaction
frequency with 5,968 records. - Same Day recorded the lowest transaction
frequency with 543 records. - Consumer was the largest customer segment
across all four shipping modes. - Corporate was the second-largest
segment. - Home Office recorded the lowest frequency overall. - Standard
Class was the most frequently used shipping mode for all three customer
segments.

**Business Insight:**

Standard Class accounted for approximately 59.71% of all transactions,
making it the most frequently selected shipping mode. Same Day
represented approximately 5.43%. Consumer customers contributed the
largest number of records across all shipping modes.

## 10.5 Bar Plot --- Total Sales and Profit by Category

Two separate bar plots were created to compare aggregated Sales and
Profit across product categories.

The `sum` estimator was used to calculate total values instead of the
default mean.

### Total Sales by Category

  Category            Total Sales
  ----------------- -------------
  Technology           836,154.03
  Furniture            741,999.80
  Office Supplies      719,047.03

**Key Findings:** - Technology generated the highest total Sales. -
Furniture ranked second. - Office Supplies generated the lowest total
Sales.

### Total Profit by Category

  Category            Total Profit
  ----------------- --------------
  Technology            145,454.95
  Office Supplies       122,490.80
  Furniture              18,451.27

**Key Findings:** - Technology generated the highest total Profit. -
Office Supplies ranked second. - Furniture generated substantially lower
Profit than the other two categories.

**Business Insight:**

Technology was the strongest category in terms of both total Sales and
total Profit. Although Furniture generated higher Sales than Office
Supplies, its total Profit was significantly lower. This highlights the
importance of evaluating profitability alongside revenue.

## 10.6 Heatmap --- Correlation Analysis

A correlation heatmap was created using four numerical variables: Sales,
Profit, Quantity, and Discount.

**Correlation Results:**

  Variable Relationship     Correlation Interpretation
  ----------------------- ------------- -------------------------------
  Sales -- Profit               +0.4791 Moderate positive
  Sales -- Quantity             +0.2008 Weak positive
  Sales -- Discount             -0.0282 Almost no linear relationship
  Profit -- Quantity            +0.0663 Very weak positive
  Profit -- Discount            -0.2195 Weak negative
  Quantity -- Discount          +0.0086 Almost no linear relationship

**Key Findings:** - Sales and Profit showed the strongest positive
correlation among the selected pairs. - Sales and Quantity showed a weak
positive relationship. - Profit and Discount showed a weak negative
relationship. - Sales and Discount had almost no linear correlation. -
Quantity and Discount also showed almost no linear correlation.

**Business Insight:**

The heatmap provides a compact overview of relationships among the
selected numerical variables. Sales and Profit showed a moderate
positive association, while Discount and Profit showed a weak negative
association.

Correlation measures association and does not establish causation.

## 10.7 Pair Plot --- Multiple Numerical Relationships

A pair plot was created using Sales, Profit, Quantity, and Discount.

The visualization displayed: - Histograms along the diagonal for
individual variable distributions. - Scatter plots outside the diagonal
for pairwise numerical relationships.

**Key Findings:** - Sales and Profit showed a positive relationship. -
Sales and Quantity showed a weak positive pattern. - Profit and Discount
showed a weak negative pattern. - Sales and Discount did not show a
strong linear pattern. - Extreme observations were visible in several
numerical relationships. - Sales and Profit distributions were strongly
influenced by a relatively small number of extreme values.

**Business Insight:**

The pair plot provided an overall view of the distributions and
relationships among the four numerical variables. It helped identify
potential patterns and unusual observations without requiring separate
plots for every variable pair.

## 10.8 Joint Plot --- Sales vs Profit

A joint plot was created to examine the relationship between Sales and
Profit, along with their marginal distributions.

**Variables:** - X-axis: Sales - Y-axis: Profit - Center: Scatter plot -
Top marginal plot: Sales distribution - Right marginal plot: Profit
distribution

**Key Findings:** - Sales and Profit showed a positive relationship. -
Transactions with higher Sales often showed higher Profit values. - Some
high-Sales transactions resulted in negative Profit. - Several extreme
observations were visible. - The marginal distributions showed that most
observations were concentrated within relatively low Sales and Profit
ranges.

**Business Insight:**

The joint plot demonstrated that higher Sales were generally associated
with higher Profit, but this relationship was not consistent for every
transaction. Some high-revenue transactions still generated losses,
showing that revenue alone does not guarantee profitability.

## Overall Summary

Part 10 applied multiple Seaborn visualization techniques to examine the
distribution, frequency, relationships, and category-level performance
of the Superstore dataset.

The major findings were:

1.  Sales followed a strongly right-skewed distribution, with a skewness
    value of 13.
2.  The middle 50% of Sales values ranged from 17.28 to 209.94.
3.  Profit density was concentrated around zero, with 8,058 profitable
    and 1,871 loss-making transactions.
4.  Technology showed the highest median Profit (25.0182) among the
    three categories.
5.  Standard Class was the most frequently used shipping mode, with
    5,968 records.
6.  Consumer customers represented the largest segment, with 5,191
    records.
7.  Technology generated the highest total Sales (836,154.03) and total
    Profit (145,454.95).
8.  Sales and Profit had a moderate positive correlation of
    approximately 0.4791.
9.  Discount and Profit had a weak negative correlation of approximately
    -0.2195.
10. Pair plots and joint plots provided additional views of numerical
    relationships and extreme observations.

**Conclusion:**

Seaborn visualizations helped communicate the dataset's statistical
characteristics and business patterns through different graphical
techniques. Histograms and KDE plots explained distributions, box plots
highlighted medians and outliers, count plots compared frequencies, bar
plots compared aggregated business performance, and correlation-based
visualizations explored numerical relationships.

------------------------------------------------------------------------
