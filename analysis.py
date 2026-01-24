import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plotting style
sns.set(style="whitegrid")

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

def analyze_demographics(consumers):
    """Analyzes consumer demographics."""
    print("\n--- Demographic Analysis ---")
    
    # Age distribution
    print(f"Average Consumer Age: {consumers['Age'].mean():.2f}")
    
    plt.figure(figsize=(10, 6))
    sns.histplot(consumers['Age'], bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Consumer Age')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig('output/age_distribution_analysis.png')
    print("Saved age distribution plot to output/age_distribution_analysis.png")

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

def analyze_ratings(ratings):
    """Analyzes rating distributions."""
    print("\n--- Rating Distribution Analysis ---")
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Overall_Rating', data=ratings, palette='viridis')
    plt.title('Distribution of Overall Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig('output/rating_distribution.png')
    print("Saved rating distribution plot to output/rating_distribution.png")

import market_opportunity

def main():
    # Ensure output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')
        
    consumers, ratings, restaurants = load_data()
    
    if consumers is not None and ratings is not None:
        analyze_demographics(consumers)
        analyze_ratings(ratings)
        
        if restaurants is not None:
            analyze_top_restaurants(ratings, restaurants)
            
        # Run Market Gap Analysis
        market_opportunity.analyze_market_gaps()
        
        print("\nAnalysis complete. Plots saved to 'output/' directory.")

if __name__ == "__main__":
    main()
