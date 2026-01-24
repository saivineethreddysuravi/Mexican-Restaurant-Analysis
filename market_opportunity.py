import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_market_gaps(data_dir="Dataset", output_dir="output"):
    """
    Compares consumer preferences vs. available restaurant cuisines 
    to identify market gaps (high demand, low supply).
    """
    print("\n--- Market Opportunity & Gap Analysis ---")
    
    try:
        # Load necessary data
        user_prefs = pd.read_csv(os.path.join(data_dir, "consumer_preferences.csv"))
        rest_cuisines = pd.read_csv(os.path.join(data_dir, "restaurant_cuisines.csv"))
        
        # 1. Analyze Demand (Consumer Preferences)
        demand_counts = user_prefs['Preferred_Cuisine'].value_counts().reset_index()
        demand_counts.columns = ['Cuisine', 'Demand_Count']
        
        # 2. Analyze Supply (Restaurant Cuisines)
        supply_counts = rest_cuisines['Cuisine'].value_counts().reset_index()
        supply_counts.columns = ['Cuisine', 'Supply_Count']
        
        # 3. Merge Demand and Supply
        market_analysis = pd.merge(demand_counts, supply_counts, on='Cuisine', how='outer').fillna(0)
        
        # Calculate 'Opportunity Score': Demand / (Supply + 1) to avoid division by zero
        # Higher score = High Demand, Low Supply
        market_analysis['Opportunity_Score'] = market_analysis['Demand_Count'] / (market_analysis['Supply_Count'] + 1)
        
        # Sort by Opportunity Score
        top_opportunities = market_analysis.sort_values(by='Opportunity_Score', ascending=False).head(10)
        
        print("\nTop 5 Underserved Cuisines (High Demand / Low Supply):")
        print(top_opportunities[['Cuisine', 'Demand_Count', 'Supply_Count', 'Opportunity_Score']].head(5))
        
        # Visualization
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Opportunity_Score', y='Cuisine', data=top_opportunities, palette='magma')
        plt.title('Top Market Opportunities (Gap Analysis)')
        plt.xlabel('Opportunity Score (Demand / Supply ratio)')
        plt.ylabel('Cuisine')
        plt.tight_layout()
        
        output_path = os.path.join(output_dir, 'market_opportunity_gap.png')
        plt.savefig(output_path)
        print(f"Saved market gap chart to {output_path}")
        
        return top_opportunities
        
    except FileNotFoundError as e:
        print(f"Error loading files for market analysis: {e}")
        return None

if __name__ == "__main__":
    analyze_market_gaps()
