import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="AgriYield",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    model = joblib.load("crop_yield_model.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    return model, feature_columns

model, feature_columns = load_model()

@st.cache_data
def load_dataset():
    DATASET_FILE = "CROP_DATASET.xlsx"

    if os.path.exists(DATASET_FILE):
        data = pd.read_excel(DATASET_FILE)
        data.columns = data.columns.str.strip()
        return data

    return None

df = load_dataset()

st.markdown(
    """
    <style>

    .stApp {
        background:
        linear-gradient(
            135deg,
            #fffbea 0%,
            #eef9e8 45%,
            #e1f5ec 100%
        );
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    [data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #14532d 0%,
            #166534 45%,
            #0f766e 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    h1 {
        color: #14532d !important;
        font-weight: 850 !important;
    }

    h2 {
        color: #166534 !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #0f766e !important;
        font-weight: 750 !important;
    }

    .stMarkdown p {
        color: #24352a;
        font-size: 16px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #f0fdf4 45%,
            #ecfeff 100%
        );

        border: 2px solid #86efac;
        border-radius: 18px;

        box-shadow:
        0 5px 15px rgba(22, 101, 52, 0.12);

        transition: 0.2s;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #14b8a6;

        box-shadow:
        0 7px 20px rgba(15, 118, 110, 0.18);
    }

    [data-testid="stMetric"] {
        background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #ecfdf5 45%,
            #fefce8 100%
        );

        padding: 17px;
        border-radius: 16px;
        border: 2px solid #86efac;

        box-shadow:
        0 4px 14px rgba(22, 101, 52, 0.12);

        min-height: 105px;
    }

    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #166534 !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 21px !important;
        white-space: normal !important;
        overflow: visible !important;
        color: #14532d !important;
    }

    .stButton > button {
        width: 100%;

        background:
        linear-gradient(
            90deg,
            #16a34a,
            #0f766e
        );

        color: white;
        border: none;
        border-radius: 12px;
        padding: 13px;
        font-size: 17px;
        font-weight: 700;

        box-shadow:
        0 4px 10px rgba(22, 101, 52, 0.18);
    }

    .stButton > button:hover {
        background:
        linear-gradient(
            90deg,
            #15803d,
            #0d9488
        );

        color: white;
    }

    [data-testid="stAlert"] {
        border-radius: 15px;
        border-width: 2px;
    }

    [data-baseweb="select"] > div {
        border-radius: 10px;
        border: 1px solid #86efac;
    }

    hr {
        border: none;
        border-top: 2px solid #bbf7d0;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🌿 AgriYield")

st.sidebar.caption(
    "Smart Crop Yield Prediction"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🌱 About / How It Works",
        "🌾 Model / Prediction",
        "💡 Insights"
    ]
)

st.sidebar.divider()

st.sidebar.write("🌱 Agriculture")
st.sidebar.write("📊 Data Science")
st.sidebar.write("🤖 Machine Learning")
st.sidebar.write("📈 Linear Regression")

if page == "🏠 Home":

    st.title("🌾 AgriYield")

    st.subheader(
        "Smart Crop Yield Prediction"
    )

    st.write(
        """
        A data-driven Machine Learning project that studies
        agricultural patterns and predicts crop yield using
        crop type, area, year, rainfall, pesticide usage
        and temperature.
        """
    )

    st.info(
        "Python  •  Pandas  •  Machine Learning  •  "
        "Linear Regression  •  Streamlit"
    )

    left, center, right = st.columns([1, 4, 1])

    with center:

        st.image(
            "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=90",
            width=1000
        )

    st.divider()

    st.header("📊 Project Overview")

    col1, col2, col3, col4 = st.columns(
        [1, 1, 1, 1.35]
    )

    with col1:

        st.metric(
            "🎯 Prediction Target",
            "hg/ha_yield"
        )

    with col2:

        st.metric(
            "📈 R² Score",
            "≈ 0.76"
        )

    with col3:

        st.metric(
            "📉 MAE",
            "≈ 29,491 hg/ha"
        )

    with col4:

        st.metric(
            "🤖 Model",
            "Linear Regression"
        )

    st.divider()

    st.header("🌿 About the Project")

    st.write(
        """
        AgriYield is a Machine Learning project developed to
        analyze agricultural data and predict crop yield.

        The project uses historical agricultural information
        to understand relationships between different factors
        and crop production.
        """
    )

    st.divider()

    st.header("✨ What Does AgriYield Do?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        with st.container(border=True):

            st.subheader("🌱 Data Analysis")

            st.write(
                "Examines agricultural data to identify "
                "useful patterns and relationships."
            )

    with col2:

        with st.container(border=True):

            st.subheader("📊 Data Visualization")

            st.write(
                "Uses charts to understand crop yield, "
                "rainfall, temperature and other factors."
            )

    with col3:

        with st.container(border=True):

            st.subheader("🤖 Machine Learning")

            st.write(
                "Uses Linear Regression to learn patterns "
                "from the agricultural dataset."
            )

    with col4:

        with st.container(border=True):

            st.subheader("🌾 Yield Prediction")

            st.write(
                "Generates an estimated crop yield from "
                "entered agricultural values."
            )

    st.divider()

    st.header("🌾 Factors Used in the Project")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("🌍 Crop Information")

            st.markdown(
                """
                - 🌍 **Area** – Geographical area
                - 🌱 **Item** – Type of crop
                - 📅 **Year** – Year of observation
                """
            )

    with col2:

        with st.container(border=True):

            st.subheader("☀️ Environmental Factors")

            st.markdown(
                """
                - 🌧️ **Rainfall** – Average rainfall
                - 🌡️ **Temperature** – Average temperature
                - 🧪 **Pesticides** – Pesticide usage
                """
            )

    st.success(
        "🌱 Agricultural Data → 🤖 Machine Learning → 🌾 Yield Estimate"
    )

elif page == "🌱 About / How It Works":

    st.title("🌱 About AgriYield")

    left, center, right = st.columns([1, 4, 1])

    with center:

        st.image(
            "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=1600&q=90",
            width=1000
        )

    st.write(
        """
        AgriYield demonstrates how agricultural data can be
        processed and passed through a Machine Learning model
        to generate a crop-yield estimate.
        """
    )

    st.divider()

    st.header("🔄 How It Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        with st.container(border=True):

            st.subheader("1️⃣ Enter")

            st.write(
                "Select the area and crop and enter "
                "the environmental values."
            )

    with col2:

        with st.container(border=True):

            st.subheader("2️⃣ Prepare")

            st.write(
                "Categorical variables such as Area "
                "and Item are converted into features."
            )

    with col3:

        with st.container(border=True):

            st.subheader("3️⃣ Predict")

            st.write(
                "The processed information is passed "
                "to the trained model."
            )

    with col4:

        with st.container(border=True):

            st.subheader("4️⃣ Result")

            st.write(
                "The application displays the estimated "
                "crop yield."
            )

    st.divider()

    st.header("🤖 Machine Learning Pipeline")

    st.info(
        """
        🌾 Agricultural Dataset
        →
        📊 Feature Selection
        →
        🔢 One-Hot Encoding
        →
        ✂️ Train/Test Split
        →
        🤖 Linear Regression
        →
        💾 Saved Model
        →
        🌐 Streamlit
        →
        🌾 Yield Prediction
        """
    )

    st.divider()

    st.header("🌿 Application Features")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📊 Data-Based")

            st.write(
                "Uses agricultural observations as the "
                "foundation for prediction."
            )

            st.subheader("🖱️ Interactive")

            st.write(
                "Users can change input values and "
                "generate predictions."
            )

            st.subheader("🌍 Agricultural Data")

            st.write(
                "Uses the areas and crops represented "
                "in the dataset."
            )

    with col2:

        with st.container(border=True):

            st.subheader("🌱 Agriculture Focused")

            st.write(
                "Inputs are directly related to "
                "agricultural production."
            )

            st.subheader("💡 Visual Insights")

            st.write(
                "Charts allow users to explore "
                "patterns in the dataset."
            )

            st.subheader("🎓 Educational")

            st.write(
                "Demonstrates the connection between "
                "Machine Learning and Streamlit."
            )

    st.divider()

    st.header("📊 Model Performance")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📈 R² Score",
            "≈ 0.76"
        )

        st.write(
            """
            The R² score represents how much variation
            in crop yield is explained by the model.
            """
        )

    with col2:

        st.metric(
            "📉 Mean Absolute Error",
            "≈ 29,491 hg/ha"
        )

        st.write(
            """
            MAE represents the average absolute difference
            between actual and predicted crop yield.
            """
        )

    st.warning(
        """
        ⚠️ This is a regression project, so R² and MAE
        are used for evaluation. R² ≈ 0.76 should not
        be called "76% accuracy".
        """
    )

    st.divider()

    st.header("🎯 Prediction Target")

    st.success(
        "hg/ha_yield — Crop yield measured in hectograms per hectare."
    )

elif page == "🌾 Model / Prediction":

    st.title("🌾 Crop Yield Prediction")

    left, center, right = st.columns([1, 4, 1])

    with center:

        st.image(
            "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=90",
            width=1000
        )

    st.write(
        """
        Select an area and crop from the dataset, enter the
        relevant growing conditions, and generate a crop-yield
        estimate using the trained Linear Regression model.
        """
    )

    st.info(
        "💡 Enter the values and click the button to generate a prediction."
    )

    if df is None:

        st.error(
            "CROP_DATASET.xlsx was not found."
        )

    else:

        area_options = sorted(
            df["Area"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        item_options = sorted(
            df["Item"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        st.header("🌱 Crop Information")

        col1, col2 = st.columns(2)

        with col1:

            area = st.selectbox(
                "🌍 Country / Area",
                area_options
            )

        with col2:

            item = st.selectbox(
                "🌱 Crop / Item",
                item_options
            )

        st.divider()

        st.header("☀️ Growing Conditions")

        col1, col2 = st.columns(2)

        with col1:

            year = st.number_input(
                "📅 Year",
                min_value=1900,
                max_value=2100,
                value=2020,
                step=1
            )

            rainfall = st.number_input(
                "🌧️ Average Rainfall (mm/year)",
                min_value=0.0,
                value=1000.0,
                step=10.0
            )

        with col2:

            temperature = st.number_input(
                "🌡️ Average Temperature (°C)",
                value=20.0,
                step=0.1
            )

            pesticides = st.number_input(
                "🧪 Pesticides (tonnes)",
                min_value=0.0,
                value=100.0,
                step=10.0
            )

        st.divider()

        if st.button(
            "🌾 Predict Crop Yield"
        ):

            input_data = pd.DataFrame(
                {
                    "Area": [area],
                    "Item": [item],
                    "Year": [year],
                    "average_rain_fall_mm_per_year": [
                        rainfall
                    ],
                    "pesticides_tonnes": [
                        pesticides
                    ],
                    "avg_temp": [
                        temperature
                    ]
                }
            )

            input_data = pd.get_dummies(
                input_data,
                columns=[
                    "Area",
                    "Item"
                ],
                dtype=int
            )

            input_data = input_data.reindex(
                columns=feature_columns,
                fill_value=0
            )

            prediction = model.predict(
                input_data
            )[0]

            st.divider()

            st.header("🎉 Prediction Result")

            st.success(
                f"🌾 Estimated Crop Yield: "
                f"{prediction:,.2f} hg/ha"
            )

            st.subheader("📋 Prediction Inputs")

            summary = pd.DataFrame(
                {
                    "Input": [
                        "Area",
                        "Crop",
                        "Year",
                        "Rainfall",
                        "Pesticides",
                        "Temperature"
                    ],
                    "Value": [
                        area,
                        item,
                        year,
                        f"{rainfall:,.1f} mm/year",
                        f"{pesticides:,.1f} tonnes",
                        f"{temperature:,.1f} °C"
                    ]
                }
            )

            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )

            st.info(
                "The estimate is generated from the trained "
                "Machine Learning model using the values entered above."
            )

elif page == "💡 Insights":

    st.title("💡 Agricultural Insights")

    left, center, right = st.columns([1, 4, 1])

    with center:

        st.image(
            "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=90",
            width=1000
        )

    st.write(
        """
        Explore the graphs created for the AgriYield project.
        These visualizations help understand crop yield,
        agricultural factors and model performance.
        """
    )

    st.divider()

    if df is None:

        st.error(
            "CROP_DATASET.xlsx was not found."
        )

    else:

        st.header("📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "🌾 Observations",
                f"{len(df):,}"
            )

        with col2:

            st.metric(
                "🌱 Crop Types",
                df["Item"].nunique()
            )

        with col3:

            st.metric(
                "🌍 Areas",
                df["Area"].nunique()
            )

        with col4:

            st.metric(
                "📅 Years",
                df["Year"].nunique()
            )

        st.divider()

        st.header(
            "📊 Distribution of Crop Yield"
        )

        graph1 = "distribution_of_crop_yield.png"

        if os.path.exists(graph1):

            st.image(
                graph1,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph1} was not found."
            )

        st.divider()

        st.header(
            "🌾 Crop Yield by Crop Type"
        )

        graph2 = "crop_yield_by_crop_type_boxplot.png"

        if os.path.exists(graph2):

            st.image(
                graph2,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph2} was not found."
            )

        st.divider()

        st.header(
            "📈 Average Crop Yield Over the Years"
        )

        graph3 = "average_crop_yield_over_years.png"

        if os.path.exists(graph3):

            st.image(
                graph3,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph3} was not found."
            )

        st.divider()

        st.header(
            "🌧️ Rainfall vs Crop Yield"
        )

        graph4 = "rainfall_vs_crop_yield.png"

        if os.path.exists(graph4):

            st.image(
                graph4,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph4} was not found."
            )

        st.divider()

        st.header(
            "🔎 Correlation Heatmap"
        )

        graph5 = "correlation_heatmap.png"

        if os.path.exists(graph5):

            st.image(
                graph5,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph5} was not found."
            )

        st.divider()

        st.header(
            "🎯 Actual vs Predicted Crop Yield"
        )

        graph6 = "actual_vs_predicted_crop_yield.png"

        if os.path.exists(graph6):

            st.image(
                graph6,
                use_container_width=True
            )

        else:

            st.warning(
                f"{graph6} was not found."
            )

        st.divider()

        st.header("📋 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        st.divider()

        st.header("🌱 Key Areas to Explore")

        col1, col2, col3 = st.columns(3)

        with col1:

            with st.container(border=True):

                st.subheader("🌾 Crop Patterns")

                st.write(
                    "Compare yield across different crops."
                )

        with col2:

            with st.container(border=True):

                st.subheader("📅 Time Patterns")

                st.write(
                    "Observe yield changes over the years."
                )

        with col3:

            with st.container(border=True):

                st.subheader("🌧️ Rainfall")

                st.write(
                    "Study rainfall and crop yield."
                )

        col1, col2 = st.columns(2)

        with col1:

            with st.container(border=True):

                st.subheader("🔎 Correlation")

                st.write(
                    "Examine relationships between numerical factors."
                )

        with col2:

            with st.container(border=True):

                st.subheader("🎯 Model Performance")

                st.write(
                    "Compare actual and predicted yield."
                )

        st.success(
            """
            🌱 Explore the visualizations above to understand
            crop patterns, environmental factors and model performance.
            """
        )

st.divider()

st.caption(
    "🌾 AgriYield | Smart Crop Yield Prediction using Machine Learning"
)
