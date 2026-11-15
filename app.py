import math
import streamlit as st

st.set_page_config(
    page_title="MechaTools | Engineering Workspace",
    page_icon="⚙️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f4f7fb; }
    [data-testid="stSidebar"] { background: #10283e; }
    [data-testid="stSidebar"] * { color: #edf5fb; }
    .hero {
        padding: 2rem 2.2rem;
        border-radius: 18px;
        color: white;
        background: linear-gradient(115deg, #10283e, #1d5275);
        margin-bottom: 1.5rem;
    }
    .hero h1 { color: white; font-size: 2.5rem; margin-bottom: .4rem; }
    .hero p { color: #d4e5f0; font-size: 1.05rem; }
    .small-muted { color: #708397; font-size: .9rem; }
    div[data-testid="stMetric"] {
        background: white; padding: 1rem; border-radius: 12px;
        border: 1px solid #e2eaf2;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("⚙️ MechaTools")
st.sidebar.caption("ENGINEERING WORKSPACE")
page = st.sidebar.radio(
    "NAVIGATION",
    ["Overview", "Stress & Strain", "Factor of Safety", "Ohm's Law", "Kinematics", "Formula Library", "Practice Corner"],
)
st.sidebar.divider()
st.sidebar.caption("Version 1.0 · Student edition")

if page == "Overview":
    st.markdown(
        """
        <div class="hero">
            <h1>Understand the idea. Make it work.</h1>
            <p>A practical workspace for exploring engineering concepts,
            testing calculations and building confidence — one problem at a time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("Your engineering toolbench")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calculators", "4", "Available")
    c2.metric("Formula topics", "3", "Materials · Circuits · Motion")
    c3.metric("Practice", "1", "Starter question")
    c4.metric("Version", "1.0", "Python edition")
    st.markdown("### Choose a tool")
    cards = st.columns(2)
    with cards[0]:
        st.info("**Stress & Strain**\n\nExplore how materials respond to an applied force.")
        st.info("**Ohm's Law**\n\nFind voltage, current or resistance.")
    with cards[1]:
        st.info("**Factor of Safety**\n\nCompare failure strength with working stress.")
        st.info("**Kinematics**\n\nCalculate motion under constant acceleration.")
    st.success("Tip: Start with the calculator you are studying in class. Check the units before trusting any result.")

elif page == "Stress & Strain":
    st.title("Stress & Strain")
    st.write("For a uniform rod under axial loading. Enter SI or the units shown beside each input.")
    col1, col2 = st.columns(2)
    with col1:
        force = st.number_input("Applied force (N)", min_value=0.0, value=12000.0, step=100.0)
        area = st.number_input("Cross-sectional area (mm²)", min_value=0.000001, value=300.0, step=10.0)
    with col2:
        length = st.number_input("Original length (mm) — optional", min_value=0.0, value=1000.0, step=10.0)
        extension = st.number_input("Extension (mm) — optional", min_value=0.0, value=0.5, step=0.1)
    if st.button("Calculate stress and strain", type="primary"):
        stress_mpa = force / area
        st.metric("Normal stress", f"{stress_mpa:,.4f} MPa")
        if length > 0 and extension > 0:
            strain = extension / length
            young_gpa = (stress_mpa / strain) / 1000
            a, b = st.columns(2)
            a.metric("Normal strain", f"{strain:.6g}")
            b.metric("Young's modulus", f"{young_gpa:,.4f} GPa")
        else:
            st.caption("Enter positive values for both length and extension to calculate strain and Young's modulus.")
        st.latex(r"\sigma = \frac{F}{A} \qquad \epsilon = \frac{\Delta L}{L_0} \qquad E = \frac{\sigma}{\epsilon}")
        st.caption("Because 1 N/mm² = 1 MPa. Young's modulus assumes linear-elastic material behaviour.")

elif page == "Factor of Safety":
    st.title("Factor of Safety")
    st.write("Use the same stress units for both values.")
    strength = st.number_input("Failure strength (MPa)", min_value=0.000001, value=250.0, step=5.0)
    working = st.number_input("Working stress (MPa)", min_value=0.000001, value=100.0, step=5.0)
    if st.button("Calculate factor of safety", type="primary"):
        fos = strength / working
        st.metric("Factor of safety", f"{fos:.4f}")
        st.latex(r"\mathrm{FoS} = \frac{\text{Failure strength}}{\text{Working stress}}")
        if fos > 1:
            st.success("The failure strength is greater than the stated working stress. This alone does not establish that a design is safe.")
        elif math.isclose(fos, 1.0):
            st.warning("The working stress equals the stated failure strength.")
        else:
            st.error("The working stress exceeds the stated failure strength. Review the design.")
        st.caption("A suitable design factor depends on standards, loading, uncertainty and application.")

elif page == "Ohm's Law":
    st.title("Ohm's Law Calculator")
    st.write("Enter exactly two known values. Leave the unknown quantity at zero.")
    voltage = st.number_input("Voltage (V)", min_value=0.0, value=12.0, step=1.0)
    current = st.number_input("Current (A)", min_value=0.0, value=0.0, step=0.1)
    resistance = st.number_input("Resistance (Ω)", min_value=0.0, value=6.0, step=1.0)
    if st.button("Solve Ohm's law", type="primary"):
        values = {"Voltage": voltage, "Current": current, "Resistance": resistance}
        unknowns = [key for key, value in values.items() if value == 0]
        if len(unknowns) != 1:
            st.error("Please enter exactly two positive values and leave one value at zero.")
        else:
            if unknowns[0] == "Voltage":
                result = current * resistance
                st.metric("Voltage", f"{result:,.4f} V")
            elif unknowns[0] == "Current":
                result = voltage / resistance if resistance else None
                if result is None:
                    st.error("Resistance must be greater than zero.")
                else:
                    st.metric("Current", f"{result:,.4f} A")
            else:
                result = voltage / current if current else None
                if result is None:
                    st.error("Current must be greater than zero.")
                else:
                    st.metric("Resistance", f"{result:,.4f} Ω")
    st.latex(r"V = IR")

elif page == "Kinematics":
    st.title("Kinematics — Constant Acceleration")
    st.write("Straight-line motion with constant acceleration.")
    c1, c2, c3 = st.columns(3)
    u = c1.number_input("Initial velocity, u (m/s)", value=5.0, step=1.0)
    acceleration = c2.number_input("Acceleration, a (m/s²)", value=2.0, step=0.5)
    time = c3.number_input("Time, t (s)", min_value=0.0, value=4.0, step=1.0)
    if st.button("Calculate motion", type="primary"):
        final_velocity = u + acceleration * time
        displacement = u * time + 0.5 * acceleration * time**2
        a, b = st.columns(2)
        a.metric("Final velocity", f"{final_velocity:,.4f} m/s")
        b.metric("Displacement", f"{displacement:,.4f} m")
        st.latex(r"v = u + at \qquad s = ut + \frac{1}{2}at^2")
    st.caption("These equations assume constant acceleration throughout the time interval.")

elif page == "Formula Library":
    st.title("Engineering Formula Library")
    st.write("A quick reference to core relationships. Check assumptions and units before applying them.")
    formulas = [
        ("Normal stress", r"\sigma = \frac{F}{A}", "Force divided by cross-sectional area.", "Pa; N and m²"),
        ("Normal strain", r"\epsilon = \frac{\Delta L}{L_0}", "Change in length divided by original length.", "Dimensionless"),
        ("Young's modulus", r"E = \frac{\sigma}{\epsilon}", "Stress divided by strain in the linear-elastic region.", "Pa"),
        ("Factor of safety", r"\mathrm{FoS} = \frac{S_f}{\sigma_w}", "Failure strength divided by working stress.", "Same stress units"),
        ("Ohm's law", r"V = IR", "Voltage equals current multiplied by resistance.", "V, A, Ω"),
        ("Final velocity", r"v = u + at", "Velocity after time t under constant acceleration.", "m/s, m/s², s"),
        ("Displacement", r"s = ut + \frac{1}{2}at^2", "Displacement under constant acceleration.", "m, m/s, s"),
        ("Velocity without time", r"v^2 = u^2 + 2as", "Relates velocity, acceleration and displacement.", "SI units"),
    ]
    for name, equation, description, units in formulas:
        with st.expander(name):
            st.latex(equation)
            st.write(description)
            st.caption(f"Units: {units}")

elif page == "Practice Corner":
    st.title("Practice Corner")
    st.write("Try this Strength of Materials question before revealing the explanation.")
    st.markdown(
        "**Question:** A steel rod is subjected to a tensile force of 12,000 N. "
        "Its cross-sectional area is 300 mm². What is the normal stress?"
    )
    answer = st.radio("Choose your answer:", ["4 N/mm²", "40 N/mm²", "400 N/mm²", "36,000 N/mm²"], index=None)
    if st.button("Check answer"):
        if answer == "40 N/mm²":
            st.success("Correct! Stress = Force ÷ Area = 12,000 ÷ 300 = 40 N/mm² = 40 MPa.")
        elif answer is None:
            st.warning("Choose an answer first.")
        else:
            st.error("Not quite. Divide the applied force by the cross-sectional area, keeping the units consistent.")
    with st.expander("Show the worked solution"):
        st.write("Step 1: Use σ = F/A.")
        st.write("Step 2: Substitute: σ = 12,000 N ÷ 300 mm².")
        st.write("Step 3: σ = 40 N/mm² = 40 MPa.")

st.divider()
st.caption("MechaTools · Educational project · Verify engineering calculations and design assumptions before real-world use.")
