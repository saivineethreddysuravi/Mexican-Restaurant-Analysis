import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_market_visualizations():
    print('Generating market opportunity visualizations...')
    
    # Simulating market data
    segments = ['Quick Service', 'Casual Dining', 'Fine Dining', 'Street Food']
    market_share = [35, 25, 15, 25]
    
    plt.figure(figsize=(12, 5))
    
    # 1. Market Share Distribution
    plt.subplot(1, 2, 1)
    plt.pie(market_share, labels=segments, autopct='%1.1f%%', colors=sns.color_palette('viridis'))
    plt.title('Mexican Food Market Segments (Projected)')
    
    # 2. Sentiment Analysis by Cuisines
    cuisines = ['Authentic', 'Tex-Mex', 'Fusion', 'Vegan']
    sentiment = [4.2, 3.8, 4.5, 4.0]
    
    plt.subplot(1, 2, 2)
    sns.barplot(x=cuisines, y=sentiment, palette='magma')
    plt.ylim(0, 5)
    plt.axhline(y=4.0, color='r', linestyle='--', label='Target Benchmark')
    plt.title('Consumer Sentiment Scores (Internal Beta)')
    plt.ylabel('Average Rating (1-5)')
    
    plt.tight_layout()
    if not os.path.exists('docs/visuals'):
        os.makedirs('docs/visuals')
        
    plt.savefig('docs/visuals/market_analysis_summary.png')
    print('Visualization saved: docs/visuals/market_analysis_summary.png')

if __name__ == '__main__':
    generate_market_visualizations()
