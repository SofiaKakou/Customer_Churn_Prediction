# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# page config
st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide"
)

st.markdown("""
<style>
            
/* ------Metric Cards------ */        
[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(0, 102, 255, 0.18),
        rgba(140, 82, 255, 0.18)
    );

    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px;
    border-radius: 18px;
    box-shadow:
        0 8px 24px rgba(0,0,0,0.18);
    backdrop-filter: blur(12px);
} 
                 
/* ------Main Title------ */                     
.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0px;
}     
                  
/* -----Subtitle------- */             
.subtitle{
    font-size: 18px;
    color:  #666;
    margin-bottom: 25px;                                                     
}
            
/* ------Tabs------ */ 
button[data-baseweb="tab"]{
    font-size: 16px;
    font-weight: 600;
}

/* ------Side Bar------ */
section[data-testid="stSidebar"]{
    padding-top: 20px;
}

/* ------Sidebar Navigation Buttons------ */
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 14px;
    padding: 12px 14px;
    margin-bottom: 8px;

    font-weight: 600;

    border: 1px solid rgba(120,120,120,0.25);

    background: rgba(120,120,120,0.08);

    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] button:hover {
    transform: translateX(4px);

    background: linear-gradient(
        135deg,
        rgba(0,102,255,0.20),
        rgba(140,82,255,0.18)
    );
}
            
/* ------Images------ */
img {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)



# ---------------------------------------------------------

# paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

OUTPUTS_DIR = PROJECT_DIR / "outputs"
MODEL_METRICS_DIR = OUTPUTS_DIR / "model-metrics"
SHAP_DIR = OUTPUTS_DIR / "shap"
FINAL_DATA_DIR = PROJECT_DIR / "data" / "final"

# helper functions
@st.cache_data
def load_csv(path):
    return pd.read_csv(path)

def safe_load_csv(path):
    if path.exists():
        return load_csv(path)
    else:
        st.warning(f"Missing File: {path.name}")
        return None

def safe_show_image(path, caption=None, width=700):
    if path.exists():
        st.image(str(path), caption=caption, width=width)
    else:
        st.warning(f"Missing Image: {path.name}")
        
# ---------------------------------------------------------

# dashboard title
st.markdown('<div class="main-title">Customer Churn Prediction Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning insights across Telecom and Banking customer churn</div>', unsafe_allow_html=True)

# side bar
st.sidebar.header("Dashboard Navigation")

if "page" not in st.session_state:
    st.session_state.page = "Overview"

if st.sidebar.button("Overview", use_container_width=True):
    st.session_state.page = "Overview"

if st.sidebar.button("Telecom", use_container_width=True):
    st.session_state.page = "Telecom"

if st.sidebar.button("Bank", use_container_width=True):
    st.session_state.page = "Bank"

if st.sidebar.button("Comparison", use_container_width=True):
    st.session_state.page = "Comparison"

dataset_option = st.session_state.page

st.sidebar.divider()

st.sidebar.markdown("### Project Repository")

st.sidebar.link_button(
    "🔗 View GitHub Repo",
    "https://github.com/SofiaKakou/Customer_Churn_Prediction"
)

st.sidebar.markdown("""
<div style='font-size:14px; opacity:0.8; margin-top:10px;'>
Made by <b>Sofia Kakou</b><br>
Computer Science Thesis Project
</div>
""", unsafe_allow_html=True)

# overview page
if dataset_option == "Overview":
    st.header("Project Overview")

    st.markdown("""
    This dashboard compares customer churn prediction across multiple industries using machine learning and SHAP analysis
    """)

    st.divider()

    # KPI placeholders
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Datasets", "2")
    with col2:
        st.metric("Models Tested", "3")
    with col3:
        st.metric("Best Telecom Model", "XGBoost")
    with col4:
        st.metric("Best Bank Model", "Random Forest")
    
    st.subheader("Project Pipeline")

    cols = st.columns(3, border=True)

    with cols[0]:
        st.markdown("""
        ### 1. Data Preparation
        - Data exploration
        - Cleaning
        - Feature engineering
        """)

    with cols[1]:
        st.markdown("""
        ### 2. Modelling
        - Logistic Regression
        - Random Forest
        - XGBoost
        """)

    with cols[2]:
        st.markdown("""
        ### 3. Interpretation
        - Feature importance
        - SHAP analysis
        - Dashboard insights
        """)

    st.subheader("Industry Summary")

    st.subheader("Project Highlights")

    col1, col2, col3 = st.columns(3, border=False)

    with col1:
        st.metric("Total Models Evaluated", "6")

    with col2:
        st.metric("Industries Analysed", "2")

    with col3:
        st.metric("Explainability Method", "SHAP")

    cols = st.columns(2, border=True)

    with cols[0]:
        st.markdown("""
        ### Telecom
        **Best model:** XGBoost  
        **Main focus:** Usage and service-related churn behaviour
        """)

    with cols[1]:
        st.markdown("""
        ### Bank
        **Best model:** Random Forest  
        **Main focus:** Demographic and account-behaviour churn patterns
        """)

    st.subheader("Dashboard Sections")

    st.markdown("""
    - Telecom Churn Insights
    - Bank Churn Insights
    - Multi-Industry Comparison
    - SHAP Interpretation
    """)

    st.subheader("Project Repository")

    st.link_button(
        "View Github Project",
        "https://github.com/SofiaKakou/Customer_Churn_Prediction"
    )

    # footer
    st.divider()
    st.caption("Customer Churn Prediction Thesis Project | Machine Learning & SHAP & Streamlit")

# ---------------------------------------------------------

# telecom page
elif dataset_option == "Telecom":
    st.header("Telecom Churn Insights")

    st.markdown("""
   Telecom Churn appears to be mainly influenced by customer usage behaviour, 
    service-related interactions and subscription features. These insights can 
    help identify customers who may need retention support.
    """)

    telecom_results = safe_load_csv(MODEL_METRICS_DIR / "model_results.csv")
    telecom_rf = safe_load_csv(MODEL_METRICS_DIR / "rf_importance.csv")
    telecom_xgb = safe_load_csv(MODEL_METRICS_DIR / "xgb_importance.csv")
    telecom_sample = safe_load_csv(FINAL_DATA_DIR / "dashboard_sample.csv")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Sample Data",
        "Model Results",
        "Feature Importance",
        "SHAP"
    ])

    with tab1:
        st.subheader("Sample Data")

        if telecom_sample is not None:
            col1, col2, col3 = st.columns(3)

            col1.metric("Rows Shown", telecom_sample.shape[0])
            col2.metric("Features", telecom_sample.shape[1])
            col3.metric("Dataset", "Telecom")

            st.markdown("### Preview")
            st.dataframe(telecom_sample.head(10), use_container_width=True)

            with st.expander("View Full Sample Dataset"):
                st.dataframe(telecom_sample, use_container_width=True)

        st.divider()

    with tab2:
        st.subheader("Model Results")

        if telecom_results is not None:
            st.dataframe(telecom_results, use_container_width=True)

        if telecom_results is not None:
            best_telecom = telecom_results.sort_values("F1-Score", ascending=False).iloc[0]

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Best Model", best_telecom["Model"])
            col2.metric(
                "Accuracy",
                f"{best_telecom['Accuracy']:.2%}",
                help="Overall percentage of correct predictions."
            )

            col3.metric(
                "F1-Score",
                f"{best_telecom['F1-Score']:.2%}",
                help="Balance between precision and recall."
            )

            col4.metric(
                "ROC-AUC",
                f"{best_telecom['ROC-AUC']:.2%}",
                help="How well the model separates churn and non-churn customers."
            )
        st.success("""
        XGBoost was selected as the best telecom model because it achieved 
        the strongest overall performance, especially in F1-Score and recall.
        """)

        st.markdown("### Model Metric Comparison")

        metric = st.segmented_control(
            "Select metric to visualize",
            ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
            default="F1-Score",
            key="telecom_model_metric"
)

        fig = px.bar(
            telecom_results.sort_values(metric, ascending=True),
            x=metric,
            y="Model",
            orientation="h",
            text=metric,
            title=f"Telecom Model Comparison by {metric}"
        )

        fig.update_layout(
            height=400,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Feature Importance")

        st.dataframe(telecom_xgb.head(10))

        if telecom_rf is not None:
            st.markdown("### XGBoost Feature Importance")
            top_n = st.slider(
                "Select number of features to display",
                3,
                8,
                13,
                key="telecom_top_features"
)
            top_telecom = telecom_xgb.head(top_n).sort_values(
                "Importance",
                ascending=True
            )
            fig = px.bar(
                top_telecom,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Top 10 Telecom Churn Drivers",
                text="Importance"
            )

            fig.update_layout(
                height=500,
                showlegend=False
            )

            st.info("""
            Higher importance values indicate features that contribute more strongly
            to churn prediction within the XGBoost model.
            """)
            st.plotly_chart(fig, use_container_width=True)

        top_features = telecom_xgb.head(3)["Feature"].tolist()

        col1, col2, col3 = st.columns(3)
        col1.metric("Top Driver", top_features[0])
        col2.metric("Second Driver", top_features[1])
        col3.metric("Third Driver", top_features[2])

    with tab4:
        st.subheader("SHAP Visualisations")

        st.markdown("""
        SHAP plots explain how features influence the model's churn predictions.
        The plots are kept inside expanders to keep the dashboard clean.
        """)

        with st.expander("View SHAP Summary Plot"):
            safe_show_image(
                SHAP_DIR / "shap_summary.png",
                "Telecom SHAP Summary Plot"
            )

        with st.expander("View SHAP Bar Plot"):
            safe_show_image(
                SHAP_DIR / "shap_bar.png",
                "Telecom SHAP Bar Plot"
            )

        with st.expander("Business Recommendations"):
            st.markdown("""
            - Monitor customers with unusual usage patterns.
            - Identify customers with frequent service interactions.
            - Offer targeted retention campaigns to high-risk customers.
            """)

    # footer
    st.caption("Customer Churn Prediction Thesis Project | Machine Learning & SHAP & Streamlit")

# ---------------------------------------------------------

# bank page
elif dataset_option == "Bank":
    st.header("Bank Churn Insights")

    st.markdown("""
   Bank Churn appears to be strongly influenced by customer demographics
    and account behaviour, especially age, active membership, balance and product usage.
     These insights can support targeted customer retention strategies.
    """)

    bank_results = safe_load_csv(MODEL_METRICS_DIR / "bank_model_results.csv")
    bank_rf = safe_load_csv(MODEL_METRICS_DIR / "bank_rf_importance.csv")
    bank_xgb = safe_load_csv(MODEL_METRICS_DIR / "bank_xgb_importance.csv")
    bank_sample = safe_load_csv(FINAL_DATA_DIR / "bank_dashboard_sample.csv")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Sample Data",
        "Model Results",
        "Feature Importance",
        "SHAP"
    ])

    with tab1:
        st.subheader("Sample Data")

        if bank_sample is not None:
            col1, col2, col3 = st.columns(3)

            col1.metric("Rows Shown", bank_sample.shape[0])
            col2.metric("Features", bank_sample.shape[1])
            col3.metric("Dataset", "Bank")

            st.markdown("### Preview")
            st.dataframe(bank_sample.head(10), use_container_width=True)

            with st.expander("View Full Sample Dataset"):
                st.dataframe(bank_sample, use_container_width=True)

        st.divider()
    
    with tab2:
        st.subheader("Model Results")

        if bank_results is not None:
            st.dataframe(bank_results, use_container_width=True)

        if bank_results is not None:
            best_bank = bank_results.sort_values("F1-Score", ascending=False).iloc[0]

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Best Model", best_bank["Model"])
            col2.metric(
                "Accuracy",
                f"{best_bank['Accuracy']:.2%}",
                help="Overall percentage of correct predictions."
            )

            col3.metric(
                "F1-Score",
                f"{best_bank['F1-Score']:.2%}",
                help="Balance between precision and recall."
            )

            col4.metric(
                "ROC-AUC",
                f"{best_bank['ROC-AUC']:.2%}",
                help="How well the model separates churn and non-churn customers."
            )

        st.success("""
        Random Forest was selected as the best bank model because it achieved
        the best balance across accuracy, precision, F1-Score and ROC-AUC.
        """)

        st.markdown("### Model Metric Comparison")

        metric = st.segmented_control(
            "Select metric to visualize",
            ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
            default="F1-Score",
            key="bank_model_metric"
        )

        fig = px.bar(
            bank_results.sort_values(metric, ascending=True),
            x=metric,
            y="Model",
            orientation="h",
            text=metric,
            title=f"Bank Model Comparison by {metric}"
        )

        fig.update_layout(
            height=400,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Feature Importance")
        
        st.dataframe(bank_rf.head(10))

        if bank_rf is not None:
            st.markdown("### Random Forest Feature Importance")
            top_n = st.slider(
                "Select number of features to display",
                3,
                7,
                11,
                key="bank_top_features"
)
            top_bank = bank_rf.head(top_n).sort_values(
                "Importance",
                ascending=True
            )
            fig = px.bar(
                top_bank,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Top 10 Bank Churn Drivers",
                text="Importance"
            )
            fig.update_layout(
                height=500,
                showlegend=False
            )

        st.info("""
        Higher importance values indicate features that contribute more strongly
        to churn prediction within the Random Forest model.
        """)
        st.plotly_chart(fig, use_container_width=True)
    
        top_features = bank_rf.head(3)["Feature"].tolist()

        col1, col2, col3 = st.columns(3)

        col1.metric("Top Driver", top_features[0])
        col2.metric("Second Driver", top_features[1])
        col3.metric("Third Driver", top_features[2])
        
    with tab4:
        st.subheader("SHAP Visualisations")

        st.markdown("""
        SHAP plots explain how features influence the model's churn predictions.
        The plots are kept inside expanders to keep the dashboard clean.
        """)

        with st.expander("View SHAP Summary Plot"):
            safe_show_image(
                SHAP_DIR / "bank_shap_summary.png",
                "Bank SHAP Summary Plot",
                width=750
            )

        with st.expander("View SHAP Bar Plot"):
            safe_show_image(
                SHAP_DIR / "bank_shap_bar.png",
                "Bank SHAP Bar Plot",
                width=750
            )
    
        with st.expander("Business Recommendations"):
            st.markdown("""
            - Re-engage inactive customers.
            - Monitor older customers with higher balances.
            - Review product usage patterns to identify churn risk.
            """)
            
    # footer
    st.caption("Customer Churn Prediction Thesis Project | Machine Learning & SHAP & Streamlit")


# ---------------------------------------------------------

# comparison page
elif dataset_option == "Comparison":
    st.header("Multi-Industry Comparison")

    st.divider()

    telecom_results = safe_load_csv(MODEL_METRICS_DIR / "model_results.csv")
    bank_results = safe_load_csv(MODEL_METRICS_DIR / "bank_model_results.csv")

    if telecom_results is not None and bank_results is not None:
        telecom_results = telecom_results.copy()
        bank_results = bank_results.copy()

        telecom_results["Industry"] = "Telecom"
        bank_results["Industry"] = "Bank"
        
        comparison_df = pd.concat(
            [telecom_results, bank_results],
            ignore_index=True
        )

        st.subheader("Model Performance Comparison")
        st.dataframe(comparison_df, use_container_width=True)

        st.subheader("Metric Comparison")

        metric = st.segmented_control(
            "Select metric to visualize",
            ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
            default="F1-Score",
        )

    fig = px.bar(
        comparison_df,
        x="Model",
        y=metric,
        color="Industry",
        barmode="group",
        text=metric,
        title=f"Model Performance Comparison by {metric}",
        color_discrete_map={
            "Telecom": "#3B82F6",
            "Bank": "#8B5CF6"
        }
    )

    fig.update_layout(
        height=450,
        yaxis_range=[0, 1]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Key Comparison Insights")

    st.markdown("""
    - The best performing model differs by industry
    - XGBoost performed best for the telecom dataset
    - Random Forest performed best for the bank dataset
    - Telecom churn appears more influenced by usage and service related behaviour
    - Bank churn appears more influenced by demographics and account behaviour
    """)

    # footer
    st.divider()
    st.caption("Customer Churn Prediction Thesis Project | Machine Learning & SHAP & Streamlit")

    # ---------------------------------------------------------