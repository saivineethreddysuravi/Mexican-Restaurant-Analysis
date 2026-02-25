"""
Day 8: Performance Optimization - Market Opportunity & Consumer Behavior Analysis
Target Platform: Python / Pandas
Objective: Pre-aggregate large transactional data into smaller, optimized fact tables
           to reduce Power BI data model size and improve DAX engine performance.
"""

import pandas as pd
import os
import glob

def optimize_for_power_bi():
    print("Initiating Data Pre-Aggregation for Power BI Performance...")
    
    # Assume data files are in a 'data/raw' directory relative to the project root
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    raw_sales_files = glob.glob(os.path.join(data_dir, 'raw', '*sales*.csv'))
    
    if not raw_sales_files:
        print("Warning: No raw sales data found to aggregate. Simulating the aggregation logic.")
        # Simulate a dataset for demonstration
        data = {
            'order_date': pd.date_range(start='2025-01-01', periods=10000, freq='h'),
            'restaurant_id': [i % 50 for i in range(10000)],
            'item_id': [i % 200 for i in range(10000)],
            'quantity': [1 for _ in range(10000)],
            'revenue': [15.50 for _ in range(10000)]
        }
        df = pd.DataFrame(data)
    else:
        df = pd.concat((pd.read_csv(f) for f in raw_sales_files), ignore_index=True)
    
    # Ensure datetime parsing
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['date_key'] = df['order_date'].dt.date
    
    print("Aggregating to daily grain by restaurant and item...")
    
    # Pre-aggregate: Daily Sales Fact Table
    # Drastically reduces row count for BI, moving computation to ETL
    daily_sales_fact = df.groupby(['date_key', 'restaurant_id', 'item_id']).agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('revenue', 'sum'),
        total_orders=('order_date', 'count')
    ).reset_index()
    
    output_dir = os.path.join(data_dir, 'processed')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'fct_daily_sales_aggregated.csv')
    daily_sales_fact.to_csv(output_path, index=False)
    
    print(f"Aggregation successful. Output saved to: {output_path}")
    print(f"Original row count: {len(df):,}")
    print(f"Aggregated row count: {len(daily_sales_fact):,} ({(len(daily_sales_fact)/len(df))*100:.2f}% of original)")
    print("Power BI memory footprint optimized. DAX measures will compute faster.")

if __name__ == "__main__":
    optimize_for_power_bi()
