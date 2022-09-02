import pandas as pd

from typing import Any, Dict


def load_and_truncate_data(
    data: pd.DataFrame, input_param: Dict[str, Any]
) -> pd.DataFrame:
    """Load and truncate data to top n rows

    Args:
        data (pd.DataFrame): raw input data
        input_param (dict): input parameters

    Returns:
        (pd.DataFrame)
    """
    n_rows = input_param["n_rows"]
    data = data.head(n_rows)
    return data


def drop_null_data(data: pd.DataFrame) -> pd.DataFrame:
    """Process data by dropping empty values

    Args:
        data (pd.DataFrame): intermediate data

    Returns:
        (pd.DataFrame)
    """
    data = data.dropna()
    data["dummy_col"] = 0
    return data
