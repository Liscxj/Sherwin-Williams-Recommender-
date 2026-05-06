from flask import Flask, render_template, request
import pandas as pd
from filters import (
    filter_paints,
    assign_kmeans_clusters,
    add_cluster_labels,
    print_cluster_summary
)

app = Flask(__name__)

# load csv files once when the app starts
df_main = pd.read_csv("data/Sherwin Williams PDSDB 2 - Products.csv")
bases = pd.read_csv("data/Sherwin Williams PDSDB  - Product Bases.csv")
qualities = pd.read_csv("data/Sherwin Williams PDSDB  - Product Qualities.csv")
sheens = pd.read_csv("data/Sherwin Williams PDSDB  - Product Sheen.csv")

# clean sheen names so dropdown values match
sheens["Sheen"] = sheens["Sheen"].replace({
    "LowSheen Eggshell": "Low Sheen Eggshell"
})

# group sheens into a list for each product
sheens_grouped = sheens.groupby("Product_ID")["Sheen"].apply(list).reset_index()

# merge qualities + sheens into main products dataframe
df_main = df_main.merge(qualities, on="Product_ID", how="left")
df_main = df_main.merge(sheens_grouped, on="Product_ID", how="left")

# fill missing sheen lists
df_main["Sheen"] = df_main["Sheen"].apply(lambda x: x if isinstance(x, list) else [])

# create QSum from the quality columns
df_main["QSum"] = (
    df_main["Appearance"] +
    df_main["Easy_Clean"] +
    df_main["Durability"] +
    df_main["Mold_&_Mildew_Resistance"] +
    df_main["Coverage"] +
    df_main["Application"]
)

# assign clusters and readable labels
df_main = assign_kmeans_clusters(df_main, n_clusters=4)
df_main = add_cluster_labels(df_main)

print_cluster_summary(df_main)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    use_area = request.form.get("use_area")
    paint_type = request.form.get("paint_type")
    price_tier = request.form.get("price_tier")
    color_plan = request.form.get("color_plan")
    sheen = request.form.get("sheen")

   
    interior = None
    exterior = None

    if use_area == "Interior":
        interior = True
    elif use_area == "Exterior":
        exterior = True
    elif use_area == "Interior/Exterior":
        interior = True
        exterior = True

    if paint_type == "":
        paint_type = None

    # map dollar signs to dataset price tiers
    if price_tier == "":
        price_tier = None
    elif price_tier == "$":
        price_tier = "Basic"
    elif price_tier == "$$":
        price_tier = "Mid Range"
    elif price_tier == "$$$":
        price_tier = "Premium"

    if sheen == "":
        sheen = None

    # maps user-friendly color choices to actual base options
    base_options = None

    if color_plan == "":
        base_options = None
    elif color_plan == "Light colors / whites":
        base_options = ["Extra White", "White"]
    elif color_plan == "Medium or dark colors":
        base_options = ["Deep"]
    elif color_plan == "Very dark / very bold colors":
        base_options = ["Ultradeep", "Ultra Deep"]
    elif color_plan == "Bright reds, greens, or yellows":
        base_options = ["Real Red", "Bright Yellow", "Deep", "Ultradeep", "Ultra Deep"]

    # apply filters
    results = filter_paints(
        df_main=df_main,
        bases=bases,
        interior=interior,
        exterior=exterior,
        paint_type=paint_type,
        price_tier=price_tier,
        base_options=base_options,
        sheen=sheen
    )

    # sort best matches first
    if not results.empty:
        results = results.sort_values(by="QSum", ascending=False).reset_index(drop=True)

    # fill missing descriptions
    if not results.empty and "Description" in results.columns:
        results["Description"] = results["Description"].fillna("No description available.")

    # convert QSum into 5-star rating
    if not results.empty and "QSum" in results.columns:
        results["star_rating"] = ((results["QSum"] / 18) * 5).round().astype(int)

    # mark the top result as best match
    if not results.empty:
        results["best_match"] = False
        results.loc[0, "best_match"] = True

    # convert sheen list into display string
    if not results.empty and "Sheen" in results.columns:
        results["Sheen_Display"] = results["Sheen"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) and len(x) > 0 else "Not listed"
        )

    results_list = results.to_dict(orient="records")

    return render_template(
        "results.html",
        results=results_list,
        count=len(results_list)
    )


if __name__ == "__main__":
    app.run(debug=True)