import math
import streamlit as st

st.title("⚙️ Mechanics of Machines")
st.caption("Explore simple machine relationships. Ideal equations may not include friction or losses.")

tab1, tab2, tab3 = st.tabs(["Gear ratio", "Torque", "Angular speed"])

with tab1:
    st.subheader("Simple gear pair")
    driver = st.number_input("Driver gear teeth", min_value=1, value=20)
    driven = st.number_input("Driven gear teeth", min_value=1, value=60)
    driver_rpm = st.number_input("Driver speed (rpm)", min_value=0.0, value=900.0)
    if st.button("Calculate gear output"):
        ratio = driven / driver
        output_rpm = driver_rpm / ratio
        st.metric("Gear ratio (driven / driver)", f"{ratio:.3f}:1")
        st.metric("Ideal driven speed", f"{output_rpm:.2f} rpm")
        st.caption("For two external gears, the gears rotate in opposite directions.")

with tab2:
    st.subheader("Torque from force")
    force = st.number_input("Applied force (N)", min_value=0.0, value=50.0)
    radius = st.number_input("Perpendicular moment arm (m)", min_value=0.0, value=0.2)
    if st.button("Calculate torque"):
        torque = force * radius
        st.metric("Torque", f"{torque:.4f} N·m")
        st.latex(r"T = F r")

with tab3:
    st.subheader("Convert rotational speed")
    rpm = st.number_input("Rotational speed (rpm)", min_value=0.0, value=120.0)
    if st.button("Convert to angular speed"):
        omega = 2 * math.pi * rpm / 60
        st.metric("Angular speed", f"{omega:.4f} rad/s")
        st.latex(r"\omega = \frac{2\pi N}{60}")
