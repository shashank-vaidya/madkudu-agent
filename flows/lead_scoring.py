import pandas as pd

def preprocess_data(input_file):
    """
    Preprocess the raw dataset by:
    - Normalizing numerical features.
    - Calculating engagement scores.

    Args:
        input_file (str): Path to the raw input CSV file.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    # Load the raw dataset
    df = pd.read_csv(input_file)

    # Normalize numerical features
    df["Norm_Website_Visits"] = df["Website Visits"] / df["Website Visits"].max()
    df["Norm_Content_Downloads"] = df["Content Downloads"] / df["Content Downloads"].max()
    df["Norm_Time_Spent"] = df["Time Spent (mins)"] / df["Time Spent (mins)"].max()
    df["Norm_Actions_Platform"] = df["Actions on Platform"] / df["Actions on Platform"].max()
    df["Norm_Event_Attendance"] = df["Event Attendance"] / df["Event Attendance"].max()
    df["Norm_Product_Trials"] = df["Product Trials Initiated"].astype(int)  # Convert boolean to 0/1

    # Calculate engagement score
    weights = {
        "Norm_Website_Visits": 0.10,
        "Norm_Content_Downloads": 0.10,
        "Norm_Time_Spent": 0.10,
        "Norm_Actions_Platform": 0.10,
        "Norm_Event_Attendance": 0.20,
        "Norm_Product_Trials": 0.25,
    }
    df["Engagement_Score"] = (
        weights["Norm_Website_Visits"] * df["Norm_Website_Visits"] +
        weights["Norm_Content_Downloads"] * df["Norm_Content_Downloads"] +
        weights["Norm_Time_Spent"] * df["Norm_Time_Spent"] +
        weights["Norm_Actions_Platform"] * df["Norm_Actions_Platform"] +
        weights["Norm_Event_Attendance"] * df["Norm_Event_Attendance"] +
        weights["Norm_Product_Trials"] * df["Norm_Product_Trials"]
    )

    return df


def save_preprocessed_data(input_file, output_file):
    """
    Preprocess and save the dataset.

    Args:
        input_file (str): Path to the raw input CSV file.
        output_file (str): Path to save the preprocessed CSV file.
    """
    print("Preprocessing the dataset...")
    df = preprocess_data(input_file)
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")


if __name__ == "__main__":
    # Example usage
    input_file = "data/leads_dataset_with_id.csv"  # Raw input dataset
    output_file = "data/processed_leads.csv"       # Preprocessed dataset output
    save_preprocessed_data(input_file, output_file)
