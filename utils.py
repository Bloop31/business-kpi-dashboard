import pandas as pd
def load_csv(file_path):
    df=pd.read_csv(file_path)
    required_columns=[
        "order_id",
        "date",
        "customer_id",
        "product",
        "region",
        "quantity",
        "price"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Missing column: {col}")
        
    return df
