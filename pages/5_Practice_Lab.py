import streamlit as st

st.title("🧠 Practice Lab")
st.write("A short mixed-topic check. Choose an answer, then check it.")

questions = [
    {
        "topic": "Strength of Materials",
        "question": "A force of 2,000 N acts on an area of 100 mm². What is the normal stress?",
        "options": ["2 MPa", "20 MPa", "200 MPa", "20,000 MPa"],
        "answer": "20 MPa",
        "explanation": "Stress = F/A = 2,000/100 = 20 N/mm² = 20 MPa."
    },
    {
        "topic": "Electrical Engineering",
        "question": "Two 10 Ω resistors are connected in series. What is their equivalent resistance?",
        "options": ["5 Ω", "10 Ω", "20 Ω", "100 Ω"],
        "answer": "20 Ω",
        "explanation": "For series resistors, add the resistances: 10 + 10 = 20 Ω."
    },
    {
        "topic": "Mechanics of Machines",
        "question": "A 10 N force acts perpendicular to a 0.5 m lever arm. What torque is produced?",
        "options": ["2 N·m", "5 N·m", "10 N·m", "20 N·m"],
        "answer": "5 N·m",
        "explanation": "Torque = force × perpendicular distance = 10 × 0.5 = 5 N·m."
    },
    {
        "topic": "Robotics",
        "question": "If the left and right wheel speeds are equal in a differential-drive robot, what is its ideal angular speed?",
        "options": ["Zero", "One rad/s", "Twice the wheel speed", "Cannot be determined"],
        "answer": "Zero",
        "explanation": "Angular speed = (right wheel speed − left wheel speed) / track width. Equal speeds give zero."
    }
]

for index, item in enumerate(questions, start=1):
    with st.container(border=True):
        st.caption(f"Question {index} · {item['topic']}")
        st.write(item["question"])
        choice = st.radio("Select an answer", item["options"], key=f"practice_{index}", index=None)
        if st.button("Check answer", key=f"check_{index}"):
            if choice == item["answer"]:
                st.success("Correct!")
            elif choice is None:
                st.warning("Choose an answer first.")
            else:
                st.error("Not quite. Try reviewing the formula.")
            st.info(item["explanation"])
