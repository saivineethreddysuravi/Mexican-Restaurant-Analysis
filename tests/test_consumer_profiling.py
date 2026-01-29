import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# Add parent directory to path to import scripts
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from consumer_profiling import analyze_consumer_demographics

class TestConsumerProfiling(unittest.TestCase):

    @patch('consumer_profiling.pd.read_csv')
    @patch('consumer_profiling.plt.savefig')
    @patch('consumer_profiling.os.makedirs')
    def test_analyze_demographics_flow(self, mock_makedirs, mock_savefig, mock_read_csv):
        """
        Test the main analysis flow with mocked data.
        """
        # Mock Data
        mock_df = pd.DataFrame({
            'Age': [20, 30, 40, 25],
            'Budget': ['Low', 'Medium', 'High', 'Medium'],
            'Occupation': ['Student', 'Engineer', 'Doctor', 'Student'],
            'Marital_Status': ['Single', 'Married', 'Married', 'Single']
        })
        mock_read_csv.return_value = mock_df
        
        # Run function
        result_df = analyze_consumer_demographics(data_path="dummy.csv", output_dir="test_output")
        
        # Assertions
        self.assertIsNotNone(result_df)
        self.assertEqual(len(result_df), 4)
        
        # Check if file reading was called
        mock_read_csv.assert_called_once_with("dummy.csv")
        
        # Check if output directory creation was attempted
        mock_makedirs.assert_called()

    @patch('consumer_profiling.pd.read_csv')
    def test_file_not_found(self, mock_read_csv):
        """
        Test graceful handling of missing file.
        """
        mock_read_csv.side_effect = FileNotFoundError
        
        result = analyze_consumer_demographics(data_path="non_existent.csv")
        
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
