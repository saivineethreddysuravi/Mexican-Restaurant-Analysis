import pytest
import pandas as pd
from scripts.market_opportunity import calculate_opportunity_index

def test_opportunity_index_calculation():
    """Test that the opportunity index correctly weights demand vs supply."""
    # Scenario: High Demand, Low Supply
    test_data = pd.DataFrame({
        'demand_score': [90],
        'competitor_density': [10]
    })
    
    index = calculate_opportunity_index(test_data)
    assert index.values[0] > 75 # Should be a high opportunity score

def test_sentiment_boundary_conditions():
    """Ensure that sentiment scores are clipped between -1 and 1."""
    # Logic implementation check
    from scripts.market_opportunity import normalize_sentiment
    
    assert normalize_sentiment(500) == 1.0
    assert normalize_sentiment(-500) == -1.0
    assert normalize_sentiment(0.5) == 0.5
