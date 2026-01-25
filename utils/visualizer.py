import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:
    """
    Centralized visualization utility for consistent styling and export.
    """
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        sns.set(style="whitegrid")

    def save_plot(self, filename):
        """Helper to save the current plot."""
        path = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(path, dpi=300)
        plt.close()
        print(f"  [Visualizer] Saved plot to {path}")

    def plot_histogram(self, data, column, title, xlabel, filename, bins=20, color='skyblue'):
        """Plots a histogram for a numerical column."""
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], bins=bins, kde=True, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel('Count')
        self.save_plot(filename)

    def plot_countplot(self, data, column, title, xlabel, filename, palette='viridis'):
        """Plots a count plot for a categorical column."""
        plt.figure(figsize=(8, 6))
        sns.countplot(x=column, data=data, palette=palette)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel('Count')
        self.save_plot(filename)

    def plot_bar(self, data, x, y, title, xlabel, ylabel, filename, palette='magma'):
        """Plots a bar chart."""
        plt.figure(figsize=(12, 8))
        sns.barplot(x=x, y=y, data=data, palette=palette)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        self.save_plot(filename)
