import re

import pandas as pd


def build_from_excel(path: str, sheet_name: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name)
    df.columns = [re.sub(r'\W+', '_', col).lower() for col in df.columns]
    return df
