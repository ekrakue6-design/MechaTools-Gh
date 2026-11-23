import streamlit as st

st.title("⚡ Electrical Engineering")
st.caption("Basic DC circuit calculations for learning and practice.")

tab1, tab2, tab3 = st.tabs(["Resistors", "Electrical power", "Voltage divider"])

with tab1:
    st.subheader("Equivalent resistance")
    mode = st.radio("Connection type", ["Series", "Parallel"], horizontal=True)
    values_text = st.text_input("Resistor values in ohms, separated by commas", "100, 220, 330")
    if st.button("Calculate equivalent resistance"):
        try:
            values = [float(item.strip()) for item in values_text.split(",")]
            if not values or any(value <= 0 for value in values):
                raise ValueError
            result = sum(values) if mode == "Series" else 1 / sum(1 / value for value in values)
            st.metric("Equivalent resistance", f"{result:.4f} Ω")
            st.latex(r"R_s = R_1 + R_2 + \cdots")
            if mode == "Parallel":
                st.latex(r"\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots")
        except ValueError:
            st.error("Enter positive resistor values separated by commas, for example: 100, 220, 330.")

with tab2:
    st.subheader("Electrical power")
    voltage = st.number_input("Voltage (V)", min_value=0.0, value=12.0, key="p_v")
    current = st.number_input("Current (A)", min_value=0.0, value=2.0, key="p_i")
    if st.button("Calculate power"):
        power = voltage * current
        st.metric("Power", f"{power:.4f} W")
        st.latex(r"P = VI")

with tab3:
    st.subheader("Two-resistor voltage divider")
    supply = st.number_input("Supply voltage (V)", min_value=0.0, value=12.0, key="vd_v")
    r1 = st.number_input("R1 (Ω)", min_value=0.000001, value=1000.0)
    r2 = st.number_input("R2 (Ω)", min_value=0.000001, value=2000.0)
    if st.button("Calculate output voltage"):
        output = supply * r2 / (r1 + r2)
        st.metric("Output across R2", f"{output:.4f} V")
        st.latex(r"V_{out} = V_{in}\frac{R_2}{R_1+R_2}")
        st.caption("Assumes an unloaded divider (no load connected across R2).")
