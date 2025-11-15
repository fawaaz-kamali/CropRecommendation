import streamlit as st
import pandas as pd

st.title("Field-Wise Crop Yield & Sustainability Recommender")

st.write("""
Upload a CSV with columns like:

**Field, Crop, Yield, Water_Use, Fertilizer_Use**
""")

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.write(df.head())

    required_cols = ["Field", "Crop", "Yield", "Water_Use", "Fertilizer_Use"]
    if not all(col in df.columns for col in required_cols):
        st.error(f"CSV must contain: {', '.join(required_cols)}")
    else:
        # --- Compute Sustainability Score ---
        df["Sustainability_Score"] = (
            df["Yield"] /
            (df["Water_Use"] + df["Fertilizer_Use"] + 1)
        )

        st.subheader("📊 Field-Wise Sustainability & Yield Table")
        st.write(df[["Field", "Crop", "Yield", "Water_Use", "Fertilizer_Use", "Sustainability_Score"]])

        # --- Best Crop Per Field ---
        st.subheader("🌟 Recommended Crop for Each Field")

        # Find best crop per field based on sustainability
        recommendations = (
            df.loc[df.groupby("Field")["Sustainability_Score"].idxmax()]
            [["Field", "Crop", "Yield", "Sustainability_Score"]]
            .sort_values("Field")
        )

        st.write(recommendations)

        # --- Simple chart ---
        st.subheader("📈 Sustainability Score by Field & Crop")
        chart_data = df.set_index("Crop")["Sustainability_Score"]
        st.bar_chart(chart_data)

        # --- Global Summary ---
        best_overall = df.loc[df["Sustainability_Score"].idxmax()]

        st.subheader("🏆 Overall Best Crop")
        st.success(
            f"**{best_overall['Crop']}** (Field {best_overall['Field']}) "
            f"with sustainability score **{best_overall['Sustainability_Score']:.2f}**"
        )


