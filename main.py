import kagglehub
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def get_file(url, output_file):
    try:
        # Download latest version
        path = kagglehub.dataset_download(url)
        print("Path to datasets files: ",path)
        

        if os.path.exists(path):
            files = os.listdir(path)
            print("Files in dataset directory:", files)

            # Assume the dataset contains a CSV file (replace with the actual file name if known)
            csv_file = None
            for file in files:
                if file.endswith(".xlsx"):
                    csv_file = os.path.join(path, file)
                    break

            if csv_file:
                print("CSV file found:", csv_file)

                # Change permissions for the CSV file
                try:
                    os.chmod(csv_file, 0o666)  # Read-write permissions for all
                    print("File permissions modified successfully!")
                except PermissionError:
                    print("Permission denied: You don't have the necessary permissions to change the permissions of this file.")

                # Process the CSV file
                try:
                    data = pd.read_excel(csv_file, nrows=200)
                    output_file = f"{output_file}"
                    data.to_csv(output_file, index=False)
                    print("Data saved to:", output_file)
                    #return output_file
                except Exception as e:
                    print("Error while processing the CSV file:", e)
            else:
                print("No CSV file found in the dataset directory.")
        else:
            print("Dataset directory not found:", path)
    except Exception as e:
        print("Exception: ",e)
        raise         
    with open(output_file,"r") as f:
        try:
            data = pd.read_csv(f)
            rows, cols = data.shape
            last_column = data.columns[-1]
            unique_classes = data[last_column].nunique()
            print(f"Rows: {rows}, Columns: {cols}")
            print(f"Unique classes: {unique_classes}")
            print(f"Last column: {last_column}")
            
            try:
                target_column = "TotalSalesValue"
                # Ensure the target column exists
                if target_column not in data.columns:
                    raise ValueError(f"Target column '{target_column}' not found in dataset.")

                # Separate features (X) and target (y)
                X = data.drop(columns=[target_column])
                y = data[target_column]

                # Handle non-numeric data if any
                X = pd.get_dummies(X, drop_first=True)

                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Fit linear regression model
                model = LinearRegression()
                model.fit(X_train, y_train)

                # Make predictions
                predictions = model.predict(X_test)
                mse = mean_squared_error(y_test, predictions)

                print(f"Linear Regression Mean Squared Error: {mse}")
            except Exception as e:
                print(f"Error in linear regression prediction: {e}")
                raise
            f.close()
        except Exception as e:
            print("Error analyzing the dataset:", e)
            raise    

url = "srinivasav22/sales-transactions-dataset"
output_file = "For_prediction.csv"
get_file(url,output_file)
