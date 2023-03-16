import pandas as pd


def clean_data(data):
    df = pd.DataFrame(data)
    df["price"] = df["price"].astype(int)
    df["year"] = df["year"].astype(int)
    df["mileage"] = df["mileage"].astype(int)
    return df
