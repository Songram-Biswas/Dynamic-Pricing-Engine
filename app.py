
# import streamlit as st
# import pandas as pd
# from pricing_engine.pipeline.prediction_pipeline import CustomData, PredictPipeline

# st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")

# st.title("🚀 Dynamic Pricing Predictor")
# st.markdown("---")

# with st.sidebar:
#     st.header("Product Specifications")
#     weight = st.number_input("Weight (g)", min_value=0.0, value=500.0)
#     volume = st.number_input("Volume (cm3)", min_value=0.0, value=1500.0)
#     category = st.selectbox("Category", ["bed_bath_table", "health_beauty", "sports_leisure", "computers_accessories", "watches_gifts"])

# st.subheader("Order & Payment Details")
# col1, col2, col3 = st.columns(3)

# with col1:
#     review = st.slider("Review Score", 1.0, 5.0, 4.0)
#     month = st.selectbox("Month", list(range(1, 13)))
#     is_weekend = st.selectbox("Weekend?", [0, 1])

# with col2:
#     status = st.selectbox("Order Status", ["delivered", "shipped", "processing"])
#     delay = st.number_input("Delivery Delay (days)", value=0.0)
#     payment_val = st.number_input("Payment Value", min_value=0.0, value=100.0)

# with col3:
#     c_state = st.selectbox("Customer State", ["SP", "RJ", "MG", "RS", "PR"])
#     s_state = st.selectbox("Seller State", ["SP", "RJ", "MG", "PR"])
#     p_type = st.selectbox("Payment Type", ["credit_card", "boleto", "voucher", "debit_card"])

# if st.button("Predict Optimal Price"):
#     data = CustomData(
#         review_score=review,
#         product_weight_g=weight,
#         product_volume_cm3=volume,
#         purchase_month=month,
#         is_weekend=is_weekend,
#         delivery_delay=delay,
#         payment_value=payment_val,
#         product_category_name_english=category,
#         order_status=status,
#         customer_state=c_state,
#         seller_state=s_state,
#         payment_type=p_type
#     )
    
#     input_df = data.get_data_as_data_frame()
#     pipeline = PredictPipeline()
#     prediction = pipeline.predict(input_df)
    
#     st.markdown("---")
#     st.success(f"### 💰 Suggested Price: ${round(prediction[0], 2)}")

# import streamlit as st
# import pandas as pd
# from pricing_engine.pipeline.prediction_pipeline import CustomData, PredictPipeline

# # ক্যাটাগরি লিস্ট ডাইনামিক করার জন্য ডাটা লোড করা
# @st.cache_data
# def get_categories():
#     df = pd.read_csv("notebook/product_category_name_translation.csv")
#     return sorted(df['product_category_name_english'].unique().tolist())

# all_categories = get_categories()

# st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")

# st.title("🚀 Dynamic Pricing Predictor")
# st.markdown("---")

# with st.sidebar:
#     st.header("Product Specifications")
#     weight = st.number_input("Weight (g)", min_value=0.0, value=500.0)
#     volume = st.number_input("Volume (cm3)", min_value=0.0, value=1500.0)
    
#     # এখানে এখন সব ক্যাটাগরি দেখাবে
#     category = st.selectbox("Product Category", all_categories)

# st.subheader("Order & Payment Details")
# col1, col2, col3 = st.columns(3)

# with col1:
#     review = st.slider("Review Score", 1.0, 5.0, 4.0)
#     month = st.selectbox("Month", list(range(1, 13)))
#     is_weekend = st.selectbox("Weekend?", [0, 1])

# with col2:
#     status = st.selectbox("Order Status", ["delivered", "shipped", "canceled", "processing"])
#     delay = st.number_input("Delivery Delay (days)", value=0.0)
#     payment_val = st.number_input("Payment Value", min_value=0.0, value=100.0)

# with col3:
#     # একইভাবে স্টেটগুলোও ডাইনামিক করা যায়
#     c_state = st.selectbox("Customer State", ["SP", "RJ", "MG", "RS", "PR", "SC", "BA"])
#     s_state = st.selectbox("Seller State", ["SP", "RJ", "MG", "PR", "BA"])
#     p_type = st.selectbox("Payment Type", ["credit_card", "boleto", "voucher", "debit_card"])

# if st.button("Predict Optimal Price"):
#     data = CustomData(
#         review_score=review,
#         product_weight_g=weight,
#         product_volume_cm3=volume,
#         purchase_month=month,
#         is_weekend=is_weekend,
#         delivery_delay=delay,
#         payment_value=payment_val,
#         product_category_name_english=category, # এখানে এখন ইউজারের সিলেক্ট করা ক্যাটাগরি যাবে
#         order_status=status,
#         customer_state=c_state,
#         seller_state=s_state,
#         payment_type=p_type
#     )
    
#     input_df = data.get_data_as_data_frame()
#     pipeline = PredictPipeline()
#     prediction = pipeline.predict(input_df)
    
#     st.markdown("---")
#     st.success(f"### 💰 Suggested Price: ${round(prediction[0], 2)}")
import streamlit as st
import pandas as pd
import os
from src.pricing_engine.pipeline.prediction_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")

@st.cache_data
def load_all_names():
    # প্রথম ডাটাসেট থেকে নামগুলো নেওয়া হচ্ছে কারণ এখানে টেক্সট আছে
    df = pd.read_csv("notebook/final_pricing_dataset_with_reviews.csv")
    
    # এরর এড়াতে dropna() এবং astype(str) ব্যবহার করা হয়েছে
    categories = sorted(df['product_category_name_english'].dropna().unique().astype(str).tolist())
    states = sorted(df['customer_state'].dropna().unique().astype(str).tolist())
    payments = sorted(df['payment_type'].dropna().unique().astype(str).tolist())
    
    return categories, states, payments

# নামগুলো লোড করা
all_categories, all_states, all_payments = load_all_names()

st.title("🚀 Dynamic Pricing Predictor")
st.markdown("---")

with st.sidebar:
    st.header("Product Specifications")
    weight = st.number_input("Weight (g)", min_value=0.0, value=500.0)
    volume = st.number_input("Volume (cm3)", min_value=0.0, value=1500.0)
    # এখন এখানে সব ক্যাটাগরি দেখাবে
    category = st.selectbox("Category", all_categories)

st.subheader("Order & Payment Details")
col1, col2, col3 = st.columns(3)

with col1:
    review = st.slider("Review Score", 1.0, 5.0, 4.0)
    month = st.selectbox("Month", list(range(1, 13)))
    is_weekend = st.selectbox("Weekend?", [0, 1])

with col2:
    status = st.selectbox("Order Status", ["delivered", "shipped", "processing", "canceled"])
    delay = st.number_input("Delivery Delay (days)", value=0.0)
    payment_val = st.number_input("Payment Value", min_value=0.0, value=100.0)

with col3:
    c_state = st.selectbox("Customer State", all_states)
    s_state = st.selectbox("Seller State", all_states)
    p_type = st.selectbox("Payment Type", ["credit_card", "boleto", "voucher", "debit_card"])


if st.button("Predict Optimal Price"):
    # আপনার আগের CustomData ক্লাস যদি স্ট্রিং হ্যান্ডেল করতে পারে তবে এটি সরাসরি কাজ করবে
    data = CustomData(
        review_score=review,
        product_weight_g=weight,
        product_volume_cm3=volume,
        purchase_month=month,
        is_weekend=is_weekend,
        delivery_delay=delay,
        payment_value=payment_val,
        product_category_name_english=category,
        order_status=status,
        customer_state=c_state,
        seller_state=s_state,
        payment_type=p_type
    )
    
    input_df = data.get_data_as_data_frame()
    pipeline = PredictPipeline()
    prediction = pipeline.predict(input_df)
    
    st.markdown("---")
    st.success(f"### 💰 Suggested Price: ${round(prediction[0], 2)}")