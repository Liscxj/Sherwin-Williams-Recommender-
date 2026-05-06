import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def filter_paints(
    df_main,
    bases,
    interior=None,
    exterior=None,
    paint_type=None,
    price_tier=None,
    base_options=None,
    sheen=None
):
    df = df_main.copy()

    if interior is not None:
        df = df[df["Interior"] == interior]

    if exterior is not None:
        df = df[df["Exterior"] == exterior]

    if paint_type is not None:
        df = df[df["Type"] == paint_type]

    if price_tier is not None:
        df = df[df["Price_Tier"] == price_tier]

    if base_options is not None:
        valid_ids = bases[bases["Base"].isin(base_options)]["Product_ID"]
        df = df[df["Product_ID"].isin(valid_ids)]

    if sheen is not None:
        df = df[df["Sheen"].apply(lambda x: sheen in x if isinstance(x, list) else False)]

    return df


def assign_kmeans_clusters(df, n_clusters=4):
    df = df.copy()

    features = df[[
        "Appearance",
        "Easy_Clean",
        "Durability",
        "Mold_&_Mildew_Resistance",
        "Coverage",
        "Application",
        "Interior",
        "Exterior",
        "VOC_Value",
        "Recoat_Dry_Time",
        "Coverage_Min",
        "Coverage_Max"
    ]].copy()

    features["Interior"] = features["Interior"].astype(int)
    features["Exterior"] = features["Exterior"].astype(int)

    for col in ["VOC_Value", "Recoat_Dry_Time", "Coverage_Min", "Coverage_Max"]:
        features[col] = pd.to_numeric(features[col], errors="coerce")

    categorical = df[["Type", "Price_Tier", "Cleanup"]].fillna("Unknown")
    features = features.join(categorical)

    features = pd.get_dummies(
        features,
        columns=["Type", "Price_Tier", "Cleanup"],
        drop_first=False
    )

    features = features.fillna(features.mean(numeric_only=True))

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = kmeans.fit_predict(scaled_features)

    return df


def add_cluster_labels(df):
    df = df.copy()

    cluster_labels = {
        0: "Specialty Coating",
        1: "Premium Performance",
        2: "Standard Coating",
        3: "Exterior Coating"
    }

    df["Cluster_Label"] = df["Cluster"].map(cluster_labels)

    return df


def print_cluster_summary(df):
    print("\n--- CLUSTER SUMMARY ---")

    summary = df.groupby("Cluster")[[
        "QSum",
        "Interior",
        "Exterior",
        "VOC_Value",
        "Recoat_Dry_Time",
        "Coverage_Min",
        "Coverage_Max"
    ]].mean()

    print(summary)

    print("\nCluster Counts:")
    print(df["Cluster"].value_counts().sort_index())

    print("-----------------------\n")


def get_cluster_recommendations(df, selected_product_name, top_n=5):
    matches = df[df["Product_Name"] == selected_product_name]

    if matches.empty:
        return pd.DataFrame()

    selected_row = matches.iloc[0]
    selected_cluster = selected_row["Cluster"]
    selected_id = selected_row["Product_ID"]

    cluster_matches = df[
        (df["Cluster"] == selected_cluster) &
        (df["Product_ID"] != selected_id)
    ].copy()

    if cluster_matches.empty:
        return pd.DataFrame()

    cluster_matches = (
        cluster_matches
        .sort_values(by="QSum", ascending=False)
        .head(top_n)
    )

    return cluster_matches