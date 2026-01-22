import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_consumer_demographics(data_path="Dataset/consumers.csv", output_dir="output"):
    """
    Analyzes consumer demographics to understand the target audience.
    Focuses on Age, Budget, and Occupation correlations.
    """
    print("\n--- Consumer Demographics & Behavioral Profiling ---")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    try:
        df = pd.read_csv(data_path)
        print(f"Loaded {len(df)} consumer profiles.")
        
        # 1. Age Distribution Analysis
        avg_age = df['Age'].mean()
        print(f"Average Consumer Age: {avg_age:.1f} years")
        
        # 2. Budget Preferences
        budget_counts = df['Budget'].value_counts(normalize=True) * 100
        print("\nBudget Preferences:")
        print(budget_counts.to_string(float_format="%.1f%%"))
        
        # 3. Student vs Employed Budget Analysis
        # Filter for top occupations to avoid noise
        top_occupations = df['Occupation'].value_counts().head(3).index
        filtered_df = df[df['Occupation'].isin(top_occupations)]
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Occupation', hue='Budget', data=filtered_df, palette='viridis')
        plt.title('Budget Preferences by Occupation (Top 3)')
        plt.ylabel('Number of Consumers')
        
        output_path = os.path.join(output_dir, 'demographics_budget_by_occupation.png')
        plt.savefig(output_path)
        print(f"Saved demographics chart to {output_path}")
        
        # 4. Marital Status & Dining Habits (Hypothetical correlation)
        marital_counts = df['Marital_Status'].value_counts()
        print("\nMarital Status Breakdown:")
        print(marital_counts)

        return df
        
    except FileNotFoundError:
        print(f"Error: Could not find data file at {data_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    analyze_consumer_demographics()
