import streamlit as st

st.set_page_config(page_title="Strength of Materials | MechaTools", page_icon="🧱", layout="wide")
st.title("🧱 Strength of Materials")
st.caption("Additional learning calculators for material behaviour. Check assumptions and units.")

tab1, tab2, tab3 = st.tabs(["Thermal expansion", "Poisson's ratio", "Shear stress"])

with tab1:
    st.subheader("Linear thermal expansion")
    alpha = st.number_input("Coefficient of linear expansion (1/°C)", min_value=0.0, value=0.000012, format="%.8f")
    length = st.number_input("Original length (m)", min_value=0.0, value=2.0)
    change_temp = st.number_input("Temperature change (°C)", value=50.0)
    if st.button("Calculate expansion", key="thermal"):
        delta_l = alpha * length * change_temp
        st.metric("Change in length", f"{delta_l:.6f} m")
        st.metric("Change in length", f"{delta_l * 1000:.4f} mm")
        st.latex(r"\Delta L = \alpha L_0 \Delta T")

with tab2:
    st.subheader("Poisson's ratio")
    lateral = st.number_input("Lateral strain", value=0.0002, format="%.6f")
    longitudinal = st.number_input("Longitudinal strain", value=-0.001, format="%.6f")
    if st.button("Calculate Poisson's ratio", key="poisson"):
        if longitudinal == 0:
            st.error("Longitudinal strain cannot be zero.")
        else:
            ratio = -lateral / longitudinal
            st.metric("Poisson's ratio", f"{ratio:.5f}")
            st.latex(r"\nu = -\frac{\epsilon_{lateral}}{\epsilon_{longitudinal}}")

with tab3:
    st.subheader("Average direct shear stress")
    force = st.number_input("Shear force (N)", min_value=0.0, value=5000.0)
    area = st.number_input("Shear area (mm²)", min_value=0.000001, value=250.0)
    if st.button("Calculate shear stress", key="shear"):
        stress = force / area
        st.metric("Average shear stress", f"{stress:.4f} MPa")
        st.latex(r"\tau_{avg} = \frac{V}{A}")
        st.caption("This is an average-stress calculation; actual stress distribution depends on geometry and loading.")
