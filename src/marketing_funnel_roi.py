import pandas as pd
import numpy as np

def calculate_marketing_funnel(df):
    """
    Analyzes the marketing funnel from Impression to Repeat Customer.
    Calculates Conversion Rates and Identifies Leakage Points.
    """
    funnel_data = {
        'Stage': ['Impressions', 'Visits', 'First-Time Order', 'Loyalty Signup', 'Repeat Visit (3+)'],
        'Count': [
            df['impressions'].sum(),
            df['visits'].sum(),
            df['first_time_orders'].sum(),
            df['loyalty_signups'].sum(),
            df['repeat_visits'].sum()
        ]
    }
    funnel = pd.DataFrame(funnel_data)
    
    # Simple conversion rate calculation
    counts = funnel['Count'].values
    conv_rates = [100.0]
    for i in range(1, len(counts)):
        rate = (counts[i] / counts[i-1]) * 100 if counts[i-1] > 0 else 0
        conv_rates.append(round(rate, 2))
    funnel['Conversion Rate (%)'] = conv_rates
    
    return funnel

def calculate_cac_vs_ltv(df, marketing_spend, clv_value):
    """
    Calculates Customer Acquisition Cost (CAC) and LTV/CAC Ratio.
    Goal: Senior-level ROI tracking.
    """
    total_new_customers = df['first_time_orders'].sum()
    if total_new_customers == 0:
        return {'CAC': 0, 'LTV/CAC Ratio': 0, 'Status': 'N/A'}
        
    cac = marketing_spend / total_new_customers
    ltv_cac_ratio = clv_value / cac
    
    return {
        'CAC': round(cac, 2),
        'LTV/CAC Ratio': round(ltv_cac_ratio, 2),
        'Status': 'Healthy' if ltv_cac_ratio > 3 else 'Needs Optimization'
    }

if __name__ == "__main__":
    # Mock data representing regional marketing performance
    data = {
        'region': ['Southwest', 'Northeast', 'Midwest', 'West', 'South'],
        'impressions': [100000, 80000, 50000, 120000, 90000],
        'visits': [5000, 4500, 2000, 6000, 4000],
        'first_time_orders': [2000, 1800, 800, 2500, 1500],
        'loyalty_signups': [400, 350, 100, 600, 200],
        'repeat_visits': [150, 120, 30, 200, 60]
    }
    df = pd.DataFrame(data)
    
    # Calculate Funnel
    funnel_results = calculate_marketing_funnel(df)
    print("--- Marketing Funnel Analysis (Total) ---")
    print(funnel_results)
    
    # Senior Impact Metric: ROI of optimizing the 'Loyalty Signup' drop-off
    roi_metrics = calculate_cac_vs_ltv(df, marketing_spend=50000, clv_value=150)
    print("\n--- ROI Metrics ---")
    for k, v in roi_metrics.items():
        print(f"{k}: {v}")

    # Regional Performance Analysis
    print("\n--- Regional CAC Analysis ---")
    df['CAC'] = 50000 / 5 / df['first_time_orders'] # Assuming equal spend per region
    print(df[['region', 'first_time_orders', 'CAC']].sort_values(by='CAC'))
