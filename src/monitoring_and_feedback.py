import pandas as pd

def log_feedback(feedback_file, feedback_data):
    """Logs feedback for retraining."""
    feedback_df = pd.DataFrame(feedback_data)
    feedback_df.to_csv(feedback_file, index=False)

# Fraud Detection Rules

def rule_based_filter(transaction):
    if transaction['amount'] > 5000 or transaction['time_gap'] < 1:
        return "Flagged as Suspicious"
    return "Normal"

# Example Feedback Data Simulation
feedback_data = [
    {"amount_log_scaled": 1.2, "time_gap_scaled": 0.5, "actual": 0, "predicted": 1}
]
log_feedback("feedback.csv", feedback_data)

# ------------------------- Main Execution ------------------------- #

# Main workflow can be structured into a separate orchestrator script
print("Modules segregated into individual Python files.")
