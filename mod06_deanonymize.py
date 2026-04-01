import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    # merge the datasets on the quasi-identifiers
    merged = pd.merge(anon_df, aux_df, on=["age", "gender", "zip3"])

    # count how many matches each anonymized record has
    match_counts = merged.groupby("anon_id").size()

    # keep only anon_ids that appear once
    unique_ids = match_counts[match_counts == 1].index

    # filter merged data to keep only those
    unique_matches = merged[merged["anon_id"].isin(unique_ids)]

    # return just the columns we need
    result = unique_matches[["anon_id", "name"]]
    result = result.rename(columns={"name": "matched_name"})

    return result

    #raise NotImplementedError



def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    #raise NotImplementedError
    total = len(anon_df)
    matched = len(matches_df)

    rate = matched / total

    return rate
