import streamlit as st

st.set_page_config(page_title="CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 CGPA Calculator")

st.markdown(
    """
    Enter your subjects, grades, and credit hours below to calculate your **CGPA**.
    """
)

# Function to convert grade to grade point
def grade_to_point(grade):
    grade_dict = {
        "O": 10,
        "A+": 9,
        "A": 8,
        "B+": 7,
        "B": 6,
        "C": 5,
        "F": 0
    }
    return grade_dict.get(grade.upper(), 0)

# Get number of subjects
num_subjects = st.number_input("Enter number of subjects:", min_value=1, max_value=20, step=1)

grades = []
credits = []

st.write("---")
st.subheader("Enter Subject Details:")

for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)
    with col1:
        grade = st.selectbox(
            f"Grade for Subject {i+1}",
            ["O", "A+", "A", "B+", "B", "C", "F"],
            key=f"grade_{i}"
        )
    with col2:
        credit = st.number_input(
            f"Credit Hour for Subject {i+1}",
            min_value=1.0,
            max_value=10.0,
            step=0.5,
            key=f"credit_{i}"
        )

    grades.append(grade)
    credits.append(credit)

if st.button("Calculate CGPA"):
    total_points = sum(grade_to_point(g) * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    if total_credits == 0:
        st.error("Total credits cannot be zero.")
    else:
        cgpa = total_points / total_credits
        st.success(f"✅ Your CGPA is: **{cgpa:.2f}**")
        st.info(f"📘 Total Credit Hours: **{total_credits:.1f}**")

st.write("---")
st.caption("Made with ❤️ using Streamlit")
