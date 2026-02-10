import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def analyze_market_opportunity():
    print("Analyzing Market Opportunity & Consumer Behavior...")
    
    # Mock Data: Competitor Analysis
    competitors = ['Taco Bell', 'Chipotle', 'Local Taqueria A', 'Local Taqueria B', 'Moe's']
    ratings = [3.5, 4.2, 4.8, 4.6, 3.8]
    price_point = [1, 2, 2, 3, 2] # 1=$ , 3=$$$
    reviews_count = [1500, 2200, 350, 120, 800]
    
    df = pd.DataFrame({
        'Competitor': competitors,
        'Rating': ratings,
        'Price': price_point,
        'Reviews': reviews_count
    })
    
    print("Competitor Landscape:")
    print(df)
    
    # Identify Gap: High Rating, Mid Price
    # Visualization
    sns.set_theme(style="whitegrid")
    
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(data=df, x="Price", y="Rating", size="Reviews", sizes=(100, 1000), hue="Competitor", palette="viridis", alpha=0.7)
    
    plt.title("Market Opportunity Map: Price vs. Quality", fontsize=15)
    plt.xlabel("Price Point (1=$ to 3=$$$)", fontsize=12)
    plt.ylabel("Avg Customer Rating (Stars)", fontsize=12)
    plt.xticks([1, 2, 3], ['Budget ($)', 'Mid-Range ($$)', 'Premium ($$$)'])
    plt.ylim(3, 5)
    
    # Highlight Opportunity Zone
    plt.axhspan(4.5, 5.0, xmin=0.3, xmax=0.7, color='green', alpha=0.1, label='Opportunity Zone (High Quality, Mid Price)')
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    output_file = 'market_opportunity_map.png'
    plt.savefig(output_file)
    print(f"Analysis Chart generated: {output_file}")

if __name__ == "__main__":
    analyze_market_opportunity()
