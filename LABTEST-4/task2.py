import numpy as np
import pandas as pd


def generate_healthcare_dataset(num_rows: int = 50, seed: int | None = 42) -> pd.DataFrame:
    """
    Create a synthetic healthcare dataset with numeric attributes and random missing values.
    """
    rng = np.random.default_rng(seed)
    data = {
        "patient_id": np.arange(1, num_rows + 1),
        "age": rng.integers(18, 90, size=num_rows),
        "bmi": rng.normal(27, 4.5, size=num_rows),
        "systolic_bp": rng.normal(125, 15, size=num_rows),
        "diastolic_bp": rng.normal(80, 10, size=num_rows),
        "cholesterol": rng.normal(200, 35, size=num_rows),
        "glucose": rng.normal(105, 18, size=num_rows),
        "hospital_stay_days": rng.poisson(4, size=num_rows),
    }
    df = pd.DataFrame(data)

    # Introduce missing values in numeric columns (excluding patient_id)
    missing_mask = rng.random(df.shape) < 0.08
    numeric_columns = [col for col in df.columns if col != "patient_id"]
    for col in numeric_columns:
        df.loc[missing_mask[:, df.columns.get_loc(col)], col] = np.nan

    return df


def fill_missing_with_median(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    """
    Fill missing values in numeric columns using the column median.
    Returns the transformed DataFrame and the medians used.
    """
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    medians: dict[str, float] = {}
    filled_df = df.copy()

    for col in numeric_columns:
        median_value = filled_df[col].median(skipna=True)
        medians[col] = median_value
        filled_df[col] = filled_df[col].fillna(median_value)

    return filled_df, medians


def min_max_scale(df: pd.DataFrame, exclude: list[str] | None = None) -> pd.DataFrame:
    """
    Apply Min-Max scaling to numeric columns, optionally excluding some columns.
    Scaling formula: (value - min) / (max - min).
    Columns with constant values will remain zero after scaling.
    """
    exclude = exclude or []
    scaled_df = df.copy()
    numeric_columns = [col for col in df.select_dtypes(include=[np.number]).columns if col not in exclude]

    for col in numeric_columns:
        col_min = df[col].min()
        col_max = df[col].max()
        denominator = col_max - col_min
        if denominator == 0:
            scaled_df[col] = 0.0
        else:
            scaled_df[col] = (df[col] - col_min) / denominator

    return scaled_df


def main() -> None:
    # Step 1: Generate synthetic dataset
    raw_df = generate_healthcare_dataset()
    print("Original dataset (first 5 rows):")
    print(raw_df.head(), "\n")

    # Step 2: Handle missing values using median
    filled_df, medians = fill_missing_with_median(raw_df)
    print("Column medians used for imputation:")
    for column, median_value in medians.items():
        print(f"  {column}: {median_value:.2f}")
    print("\nDataset after median imputation (first 5 rows):")
    print(filled_df.head(), "\n")

    # Step 3: Min-Max scaling of numeric columns (excluding identifiers)
    scaled_df = min_max_scale(filled_df, exclude=["patient_id"])
    print("Min-Max scaled dataset (first 5 rows):")
    print(scaled_df.head())


if __name__ == "__main__":
    main()

