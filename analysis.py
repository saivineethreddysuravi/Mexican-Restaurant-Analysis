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
    plt.savefig('assets/age_distribution_analysis.png')
    print("Saved age distribution plot to assets/age_distribution_analysis.png")

    # Occupation counts
    occupation_counts = consumers['Occupation'].value_counts()
    print("\nTop Occupations:")
    print(occupation_counts.head())

def analyze_ratings(ratings):
    """Analyzes restaurant ratings."""
    print("\n--- Ratings Analysis ---")
    
    # Calculate average ratings
    avg_ratings = ratings[['Overall_Rating', 'Food_Rating', 'Service_Rating']].mean()
    print("Average Ratings (0-2 Scale):")
    print(avg_ratings)
    
    # Correlation between Food and Service
    corr = ratings['Food_Rating'].corr(ratings['Service_Rating'])
    print(f"\nCorrelation between Food and Service Rating: {corr:.2f}")

def main():
    consumers, ratings, restaurants = load_data()
    
    if consumers is not None:
        analyze_demographics(consumers)
        analyze_ratings(ratings)
        
        print("\nAnalysis complete. This script demonstrates Python data manipulation skills parallel to the Power BI analysis.")

if __name__ == "__main__":
    main()
