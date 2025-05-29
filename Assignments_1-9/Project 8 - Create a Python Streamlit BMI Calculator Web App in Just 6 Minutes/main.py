import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.title("🧮 BMI Calculator")

height: int = st.slider("📏 Enter your height (in cm):", min_value=120, max_value=250, value=170)

weight: int = st.slider("🏋️ Enter your weight (in kg):", min_value=30, max_value=200, value=70)

# BMI calculation
bmi: int = weight / ((height / 100) ** 2)

st.metric(label="📊 Your BMI", value=f"{bmi:.1f}")

# BMI Result Interpretation
st.subheader("🧠 BMI Result:")
if bmi < 18.5:
    st.warning("🔸 Underweight (BMI < 18.5)")
elif 18.5 <= bmi < 25:
    st.success("✅ Normal weight (BMI 18.5–24.9)")
elif 25 <= bmi < 30:
    st.warning("⚠️ Overweight (BMI 25–29.9)")
else:
    st.error("❌ Obese (BMI ≥ 30)")

# BMI Categories for reference
with st.expander("📚 Learn about BMI categories"):
    st.markdown("""
    - 🔸 **Underweight**: BMI less than 18.5  
    - ✅ **Normal weight**: BMI between 18.5 and 24.9  
    - ⚠️ **Overweight**: BMI between 25 and 29.9  
    - ❌ **Obese**: BMI 30 or greater
    """)
