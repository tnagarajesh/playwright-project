import csv, json, os, pandas as pd


def clean_environment_variables(environment_variable_name):
    """ Cleans the specified environment variable by removing any leading or trailing whitespace.
    :param variable_name: The name of the environment variable to clean.
    :return: The cleaned value of the environment variable, or None if it is not set.
    """
    
    #Parse safely from env var (JSON or CSV)
    raw_menu_items = os.environ.get(environment_variable_name, "[]")

    try:
        menu_item_role_link_list = json.loads(raw_menu_items)
        if not isinstance(menu_item_role_link_list, list):
            raise ValueError("menu_item_role_link_list is not a list")
    except json.JSONDecodeError:
        menu_item_role_link_list = [item.strip() for item in raw_menu_items.split(",") if item.strip()]

    return menu_item_role_link_list

def read_data(user_type, env_type):
        
        data = pd.read_csv(os.environ["user_data"])

        data = data[(data['user_type'] == user_type) & (data['env_type'] == env_type)]

        if data.empty:
            raise ValueError(f"No matching data for user_type='{user_type}', env_type='{env_type}'")
        
        username = data["username"].iloc[0]
        password = data["password"].iloc[0]
        url = data["url"].iloc[0]
        
        return username, password, url

def load_test_data(file_path, test_case_name, sheet_name="TestData"):
    """
    Load test data from a CSV or Excel file and filter by test_case_name.

    Args:
        file_path (str): Path to .csv or .xlsx file
        test_case_name (str): Name of the test case to filter
        sheet_name (str): Name of the sheet (Excel only)

    Returns:
        List of tuples: Each tuple contains (user_type, env_type, menu_item)
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [
                (row['user_type'], row['env_type'], row['menu_item'])
                for row in reader
                if row['test_case_name'] == test_case_name
            ]
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        filtered_df = df[df["test_case_name"] == test_case_name]
        return [
            (row["user_type"], row["env_type"], row["menu_item"])
            for _, row in filtered_df.iterrows()
        ]
    else:
        raise ValueError("Unsupported file format: use .csv or .xlsx")