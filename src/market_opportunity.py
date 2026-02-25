import pandas as pd
import numpy as np

def calculate_opportunity_index(df):
    """
    Calculates a Market Opportunity Index based on demand vs competitor density.
    Formula: Opportunity = Demand - Competitor Density (with some weighting)
    """
    df = df.copy()
    # Simplified logic for demonstration
    df['opportunity_index'] = df['demand_score'] - (df['competitor_density'] * 0.5)
    return df['opportunity_index']

def normalize_sentiment(score):
    """
    Clips sentiment scores to be between -1 and 1.
    """
    return max(-1.0, min(1.0, float(score)))
