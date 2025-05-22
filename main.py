import streamlit as st
from prediction_helper import predict
st.set_page_config(page_title="Shyam Finance: Credit Risk Modelling", page_icon="📊")

# Custom CSS styling
st.markdown("""
    <style>
        .stApp {
            background-color: #e6f0ff;
        }
        .custom-row {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            margin: 15px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        .stNumberInput input, .stSelectbox select {
            background-color: #f8f9fa;
            border: 1px solid #ced4da;
            border-radius: 8px;
            padding: 10px;
        }
        h1 {
            color: #2c3e50;
            padding: 15px;
            font-size: 28px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
            text-align: center;
        }
        .stButton button {
            background-color: rgba(0, 123, 255, 0.2) !important;  /* Semi-transparent blue */
            color: #004fa1 !important;  /* Dark blue text */
            padding: 12px 24px;
            border-radius: 8px;
            border: 1px solid rgba(0, 123, 255, 0.5) !important;  /* Blue border */
            font-weight: bold;
            width: 100%;
            transition: all 0.5s;
        }
        .stButton button:hover {
            background-color: rgba(0, 123, 255, 0.3) !important;
            transform: scale(1.02);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            color: #003366 !important;
            border-color: rgba(0, 86, 179, 0.8) !important;
        }
        [data-testid="stMetricLabel"] {
            font-weight: bold;
            color: #4a4a4a;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='white-space: nowrap;'>Shyam Finance: Credit Risk Modeling</h1>",
    unsafe_allow_html=True
)


# Row 1
col1, col2, col3 = st.columns(3)
age = col1.number_input("Age", min_value=18, max_value=100, value=30,step=1)
income = col2.number_input("Income", min_value=0, value=40000)
loan_amount = col3.number_input("Loan Amount", min_value=1000, value=100000)

# Row 2
col4, col5, col6 = st.columns(3)
if income > 0:
    loan_to_income_ratio = loan_amount / income
    col4.write("Loan-to-Income Ratio")
    col4.write(f"{loan_to_income_ratio:.2f}")
else:
    col4.write("Loan-to-Income Ratio")
    col4.write("N/A (Income = 0)")
loan_tenure_months = col5.number_input("Loan Tenure (Months)", min_value=1, value=36,step= 1)
avg_dpd_per_delinquency = col6.number_input("Avg DPD", min_value=0, value=20)

# Row 3
col7, col8, col9 = st.columns(3)
credit_utilization_ratio = col7.number_input("Credit Utilization Ratio",min_value=0, max_value=100, step=1, value=30)
delinquency_ratio = col8.number_input("Delinquency Ratio", min_value=0, max_value=100, step=1, value=30)
num_open_accounts = col9.number_input("Open Loan Accounts", min_value=0,max_value=5, value=2, step= 1)

# Row 4
col10, col11, col12 = st.columns(3)
residence_type = col10.selectbox("Residence Type", ['Owned', 'Mortgage', 'Rented'])
loan_purpose = col11.selectbox("Loan Purpose", ['Education', 'Home', 'Auto', 'Personal'])
loan_type = col12.selectbox("Loan Type", ['Secured', 'Unsecured'])

if st.button("Calculate Risk"):
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)
    st.write(f"Deafult Probability:{probability:.2%}")
    st.write(f"Credit Score:{credit_score}")
    st.write(f"Rating:{rating}")