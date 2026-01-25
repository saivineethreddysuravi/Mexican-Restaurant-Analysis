import pandas as pd
import os
import sys

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
try:
    from visualizer import Visualizer
except ImportError:
    # Fallback if running from root
    from mexican_restaurant_analysis.utils.visualizer import Visualizer

def load_data(data_dir="Dataset"):
    """Loads datasets from the specified directory."""
    print(f"Loading data from {data_dir}...")
    try:
        consumers = pd.read_csv(os.path.join(data_dir, "consumers.csv"))
        ratings = pd.read_csv(os.path.join(data_dir, "ratings.csv"))
        restaurants = pd.read_csv(os.path.join(data_dir, "restaurants.csv"))
        print("Data loaded successfully.")
        return consumers, ratings, restaurants
    except FileNotFoundError as e:
        print(f"Error loading files: {e}")
        return None, None, None

def analyze_demographics(consumers, viz):
    """Analyzes consumer demographics."""
    print("\n--- Demographic Analysis ---")
    
    # Age distribution
    print(f"Average Consumer Age: {consumers['Age'].mean():.2f}")
    
    viz.plot_histogram(
        data=consumers,
        column='Age',
        title='Distribution of Consumer Age',
        xlabel='Age',
        filename='age_distribution_analysis.png'
    )

    # Occupation counts
    occupation_counts = consumers['Occupation'].value_counts()
    print("\nTop Occupations:")
    print(occupation_counts.head())

def analyze_top_restaurants(ratings, restaurants):
    """Identifies top 5 highest rated restaurants."""
    print("\n--- Top Restaurant Analysis ---")
    
    # Merge ratings with restaurant details
    merged = pd.merge(ratings, restaurants, on='Restaurant_ID')
    
    # Calculate average rating per restaurant
    restaurant_ratings = merged.groupby('Name')['Overall_Rating'].mean().reset_index()
    
    # Sort and get top 5
    top_5 = restaurant_ratings.sort_values(by='Overall_Rating', ascending=False).head(5)
    
    print("Top 5 Highest Rated Restaurants:")
    print(top_5)
    
    return top_5

def analyze_ratings(ratings, viz):
    """Analyzes rating distributions."""
    print("\n--- Rating Distribution Analysis ---")
    
    viz.plot_countplot(
        data=ratings,
        column='Overall_Rating',
        title='Distribution of Overall Ratings',
        xlabel='Rating',
        filename='rating_distribution.png'
    )

import market_opportunity

def main():
    # Initialize Visualizer
    viz = Visualizer(output_dir='output')
        
    consumers, ratings, restaurants = load_data()
    
    if consumers is not None and ratings is not None:
        analyze_demographics(consumers, viz)
        analyze_ratings(ratings, viz)
        
        if restaurants is not None:
            analyze_top_restaurants(ratings, restaurants)
            
        # Run Market Gap Analysis
        market_opportunity.analyze_market_gaps()
        
        print("\nAnalysis complete. Plots saved to 'output/' directory.")

if __name__ == "__main__":
    main()
