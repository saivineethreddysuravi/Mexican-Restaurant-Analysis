import pandas as pd
import logging

def audit_etl_integrity(df, expected_columns):
    # Data Quality Validation
    missing_cols = [c for c in expected_columns if c not in df.columns]
    if missing_cols:
        logging.error(f"ETL Failure: Missing columns {missing_cols}")
        return False
    # Row-count check
    if len(df) < 500:
        logging.warning("Anomaly Detected: Sample size unusually small.")
    return True
