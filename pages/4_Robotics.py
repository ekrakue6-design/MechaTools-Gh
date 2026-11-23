import math
import streamlit as st

st.title("🤖 Robotics")
st.caption("Small tools for introductory mobile robotics and actuator calculations.")

tab1, tab2, tab3 = st.tabs(["Wheel motion", "Encoder distance", "Motor speed"])

with tab1:
    st.subheader("Differential-drive wheel speed")
    left = st.number_input("Left wheel linear speed (m/s)", value=0.5)
    right = st.number_input("Right wheel linear speed (m/s)", value=0.5)
    track = st.number_input("Distance between wheels (m)", min_value=0.000001, value=0.3)
    if st.button("Calculate robot motion"):
        linear = (right + left) / 2
        angular = (right - left) / track
        st.metric("Robot forward speed", f"{linear:.4f} m/s")
        st.metric("Robot angular speed", f"{angular:.4f} rad/s")
        st.latex(r"v = \frac{v_R+v_L}{2} \qquad \omega = \frac{v_R-v_L}{b}")
        st.caption("Positive angular speed follows the sign convention implied by right minus left.")

with tab2:
    st.subheader("Distance from wheel encoder counts")
    counts = st.number_input("Encoder counts measured", min_value=0, value=500)
    pulses = st.number_input("Counts per wheel revolution", min_value=1, value=1000)
    diameter = st.number_input("Wheel diameter (m)", min_value=0.000001, value=0.1)
    if st.button("Calculate travelled distance"):
        revolutions = counts / pulses
        distance = revolutions * math.pi * diameter
        st.metric("Wheel revolutions", f"{revolutions:.4f}")
        st.metric("Estimated distance", f"{distance:.4f} m")
        st.latex(r"d = \frac{C}{CPR}\pi D")
        st.caption("Assumes counts are interpreted consistently with the encoder's CPR specification and no wheel slip.")

with tab3:
    st.subheader("DC motor speed conversion")
    rpm = st.number_input("Motor speed (rpm)", min_value=0.0, value=3000.0)
    if st.button("Convert motor speed"):
        omega = 2 * math.pi * rpm / 60
        st.metric("Angular velocity", f"{omega:.3f} rad/s")
        st.latex(r"\omega = \frac{2\pi N}{60}")
