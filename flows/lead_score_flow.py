import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib
from flows.lead_scoring import preprocess_data
from crews.lead_response_crew import LeadResponseCrew

df = preprocess_data("data/leads_dataset_with_id.csv")

response_crew = LeadResponseCrew()
print(f"Tools in LeadResponseCrew: {response_crew.tools}")


class LeadScoreFlow:
    """
    Orchestrates the lead scoring process:
    - Preprocess data.
    - Predict lead categories.
    - Save the results.
    """

    def preprocess_data(self, input_file):
        """
        Preprocess the raw dataset:
        - Normalize features.
        - Calculate engagement scores.

        Args:
            input_file (str): Path to the raw input CSV file.

        Returns:
            pd.DataFrame: Preprocessed DataFrame.
        """
        # Load the raw dataset
        df = pd.read_csv(input_file)

        # Normalize features
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

    def predict_lead_category(self, df, model_file):
        """
        Predict lead categories using a pre-trained model.

        Args:
            df (pd.DataFrame): Preprocessed DataFrame.
            model_file (str): Path to the trained model file.

        Returns:
            pd.DataFrame: DataFrame with predictions.
        """
        # Encode categorical features
        categorical_features = ["Seniority Level", "Industry", "Funding Stage"]
        for feature in categorical_features:
            df[feature] = LabelEncoder().fit_transform(df[feature])

        # Select features for prediction
        selected_features = [
            "Norm_Website_Visits", "Norm_Content_Downloads", "Norm_Time_Spent",
            "Norm_Actions_Platform", "Norm_Event_Attendance", "Norm_Product_Trials",
            "Seniority Level", "Industry", "Funding Stage"
        ]
        X = df[selected_features]

        # Load the trained model
        model = joblib.load(model_file)

        # Predict lead categories
        df["Predicted Lead Category"] = model.predict(X)
        category_mapping = {0: "Difficult", 1: "Easy", 2: "Medium"}
        df["Predicted Lead Category"] = df["Predicted Lead Category"].map(category_mapping)

        return df

    def generate_email_drafts(self, csv_path: str):
        import pandas as pd

        try:
            # Load the CSV file containing the top leads
            leads = pd.read_csv(csv_path)
            print("Columns in DataFrame:", leads.columns)  # Debugging output
            print(leads.head())  # Debugging output

            # Loop through each lead in the DataFrame
            for _, lead in leads.iterrows():
                # Dynamically construct the email if not explicitly provided
                email = f"{lead['First Name'].lower()}.{lead['Last Name'].lower()}@{lead['Company Name'].lower()}.com"
                
                # Prepare the context for the email follow-up task
                context = {
                    "lead_id": lead["Lead ID"],  # Adjusted for the column name in the CSV
                    "lead_email": email,
                    "first_name": lead["First Name"],
                    "last_name": lead["Last Name"],
                    "company_name": lead["Company Name"],
                }
                print("Processing Lead:", context)  # Debugging output

                # Create the task object
                task = response_crew.send_followup_email_task()

                # Assign the email follow-up agent to the task
                task.agent = response_crew.email_followup_agent()

                # Execute the task synchronously using execute_sync
                email_content = task.execute_sync(context=context)

                # Here you can save or process the email content
                print("Generated Email Content:", email_content.raw)  # Debugging output
        except Exception as e:
            print(f"Error while generating email drafts: {e}")






    def kickoff(self):
        """
        Run the entire lead scoring flow:
        - Preprocess data.
        - Predict lead categories.
        - Save the results.
        """
        # Step 1: Preprocess data
        print("Preprocessing data...")
        input_file = "data/leads_dataset_with_id.csv"
        df = self.preprocess_data(input_file)

        # Step 2: Predict lead categories
        print("Predicting lead categories...")
        model_file = "models/trained_xgboost_model.pkl"
        df = self.predict_lead_category(df, model_file)

        # Step 3: Save predictions
        output_file = "data/predicted_leads.csv"
        df.to_csv(output_file, index=False)
        print(f"Predictions saved to {output_file}")

         # Step 4: Shortlist top 3 leads
        print("Shortlisting top 3 leads...")
        top_leads = df[df["Predicted Lead Category"] == "Easy"].nlargest(3, "Engagement_Score")
        top_leads_output = "data/top_3_leads.csv"
        top_leads.to_csv(top_leads_output, index=False)
        print(f"Top 3 leads saved to {top_leads_output}")

        # Step 5: Generate email drafts
        print("Generating email drafts...")
        self.generate_email_drafts("data/top_3_leads.csv")