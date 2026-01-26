import unittest
import sys
import os

# Add parent directory to path to import scripts
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from consumer_profiling import analyze_consumer_demographics
except ImportError:
    # If running from root
    from mexican_restaurant_analysis.consumer_profiling import analyze_consumer_demographics

class TestConsumerAnalysis(unittest.TestCase):
    def test_function_exists(self):
        self.assertTrue(callable(analyze_consumer_demographics))

if __name__ == '__main__':
    unittest.main()
