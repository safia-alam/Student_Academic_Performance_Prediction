import os
import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "best_model.pkl")

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("🎓 Student Academic Performance — Prediction App")
st.write("Input student details to predict the **average exam score**.")

# Sidebar info
with st.sidebar:
    st.header("About")
    st.markdown(
        "This app uses a trained scikit-learn pipeline (OneHot + Regressor) "
        "to predict a student's **average score** based on demographic and academic inputs."
    )
    st.caption("Model file: `models/best_model.pkl`")

# Input form
with st.form("input_form"):
    gender = st.selectbox("Gender", ["female", "male"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_education = st.selectbox(
        "Parental level of education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree",
        ],
    )
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test preparation course", ["none", "completed"])

    math_score = st.number_input("Math score", min_value=0, max_value=100, value=70, step=1)
    reading_score = st.number_input("Reading score", min_value=0, max_value=100, value=70, step=1)
    writing_score = st.number_input("Writing score", min_value=0, max_value=100, value=70, step=1)

    submitted = st.form_submit_button("Predict")


def _build_default_pipeline():
    """Builds a fallback dummy model in case no real model exists"""
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.pipeline import Pipeline
    from sklearn.ensemble import RandomForestRegressor

    cat_features = [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course",
    ]
    num_features = ["math score", "reading score", "writing score"]

    pre = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
            ("num", "passthrough", num_features),
        ]
    )
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    pipe = Pipeline([("pre", pre), ("model", model)])

    # Train dummy model
    n = 100
    X = pd.DataFrame(
        {
            "gender": ["female", "male"] * (n // 2),
            "race/ethnicity": (["group A", "group B", "group C", "group D", "group E"] * ((n // 5) + 1))[:n],
            "parental level of education": (
                ["some high school", "high school", "some college", "associate's degree",
                 "bachelor's degree", "master's degree"] * ((n // 6) + 1)
            )[:n],
            "lunch": (["standard", "free/reduced"] * (n // 2))[:n],
            "test preparation course": (["none", "completed"] * (n // 2))[:n],
            "math score": list(range(50, 50 + n)),
            "reading score": list(range(50, 50 + n)),
            "writing score": list(range(50, 50 + n)),
        }
    )

    y = X[["math score", "reading score", "writing score"]].mean(axis=1)
    pipe.fit(X, y)
    return pipe


@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            st.sidebar.success(f"✅ Loaded trained model from `{MODEL_PATH}`")
            return model, True
        except Exception as e:
            st.sidebar.error(f"⚠️ Could not load model: {e}")
            return _build_default_pipeline(), False
    else:
        st.sidebar.warning("⚠️ No trained model found. Using fallback model.")
        return _build_default_pipeline(), False


# Load model
model, is_real_model = load_model()

# Run prediction
if submitted:
    row = pd.DataFrame(
        {
            "gender": [gender],
            "race/ethnicity": [race_ethnicity],
            "parental level of education": [parental_education],
            "lunch": [lunch],
            "test preparation course": [test_prep],
            "math score": [math_score],
            "reading score": [reading_score],
            "writing score": [writing_score],
        }
    )
    pred = model.predict(row)[0]
    st.success(f"Predicted **Average Score**: {pred:.2f} / 100")

    # Only show training tip if using fallback
    if not is_real_model:
        st.caption("💡 Tip: Train and save a real model in the notebook for best accuracy.")
