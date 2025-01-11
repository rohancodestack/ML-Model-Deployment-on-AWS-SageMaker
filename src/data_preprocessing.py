import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(data_path):
    """Handles data cleaning and feature engineering."""
    data = pd.read_csv(data_path)

    # Handle missing values
    data['amount'] = data['amount'].fillna(data['amount'].median())
    data['time_gap'] = data['time_gap'].fillna(data['time_gap'].mean())

    # Feature Engineering
    data['amount_log'] = data['amount'].apply(lambda x: np.log1p(x))  # Log transformation
    data['is_large'] = data['amount'] > 1000  # Binary feature

    # Standardization
    scaler = StandardScaler()
    data[['amount_log_scaled', 'time_gap_scaled']] = scaler.fit_transform(
        data[['amount_log', 'time_gap']]
    )

    # Separate features and target
    X = data[['amount_log_scaled', 'time_gap_scaled']]
    y = data['target']

    return train_test_split(X, y, test_size=0.2, random_state=42)