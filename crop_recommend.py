import streamlit as st
import pandas as pd
import random

st.title("Field-Wise Crop Yield & Sustainability Recommender")

# --- File Uploads ---
uploaded_crop_file = st.file_uploader("Upload Crop Profile", type=["csv"])
uploaded_current_conditions_file = st.file_uploader("Upload Current Conditions", type=["csv"])
uploaded_historical_data_file = st.file_uploader("Upload Historical Data", type=["csv"])


# --- Placeholder model ---
def my_model(df_crop, df_current, df_history):
    sustainability_score = 0.82
    yield_prediction = 3.75
    return sustainability_score, yield_prediction


# --- Main ---
if uploaded_crop_file and uploaded_current_conditions_file and uploaded_historical_data_file:

    df_crop = pd.read_csv(uploaded_crop_file)
    df_current = pd.read_csv(uploaded_current_conditions_file)
    df_history = pd.read_csv(uploaded_historical_data_file)

    st.subheader("📄 Crop Profile Preview")
    st.write(df_crop.head())

    st.subheader("📄 Current Conditions Preview")
    st.write(df_current.head())

    st.subheader("📄 Historical Data Preview")
    st.write(df_history.head())

    # Detect crop column
    possible_crop_cols = ["crop", "Crop", "crop_name", "crop_type", "Crop Name"]
    crop_col = None
    for col in df_crop.columns:
        if col.strip() in possible_crop_cols:
            crop_col = col
            break

    if not crop_col:
        st.error(
            "❌ Could not find a crop name column.\n\n"
            "Your Crop Profile CSV must contain one of these column names:\n"
            "`crop`, `Crop`, `crop_name`, `crop_type`, `Crop Name`"
        )
        st.stop()

    # Check field_id column
    if "field_id" not in df_current.columns:
        st.error("❌ Current Conditions CSV must contain a column named `field_id`.")
        st.stop()

    # --- Run placeholder model ---
    sustainability_score, yield_prediction = my_model(df_crop, df_current, df_history)

    st.subheader("📊 Model Output")
    st.metric("Sustainability Score", f"{sustainability_score:.2f}")
    st.metric("Yield Prediction (t/ha)", f"{yield_prediction:.2f}")

    # --------------------------------------------------------------------
    # TOP 3 CROPS FOR EACH FIELD (using current_conditions_data)
    # --------------------------------------------------------------------
    st.subheader("🌾 Top 3 Recommended Crops per Field")

    recommendations_list = []

    for _, row in df_current.iterrows():
        field_id = row["field_id"]

        # Copy crop list and assign placeholder score
        temp = df_crop.copy()
        temp["field_id"] = field_id
        temp["Score"] = [random.uniform(0, 1) for _ in range(len(temp))]
        temp["Rank"] = temp["Score"].rank(ascending=False).astype(int)

        # Select top 3
        top3 = temp.nsmallest(3, "Rank")

        recommendations_list.append(
            top3[["field_id", "Rank", crop_col, "Score"]]
        )

    # Combine results into a single dataframe
    rec_df = pd.concat(recommendations_list, ignore_index=True)

    st.dataframe(rec_df)
