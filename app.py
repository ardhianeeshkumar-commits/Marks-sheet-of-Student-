import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Dashboard",page_icon="📊",layout="wide")
df = pd.read_csv("Students_Dataset.csv")


st.title("Student Details & Marks Dashboard")
st.write("Analyze student performance using the CSV dataset.")

st.sidebar.header("🔎 Filters")

gender = st.sidebar.multiselect("Select Gender",options=df["Gender"].unique(),default=df["Gender"].unique())

age = st.sidebar.multiselect("Select Age",options=sorted(df["Age"].unique()),default=sorted(df["Age"].unique()))

filtered_df = df[(df["Gender"].isin(gender)) &(df["Age"].isin(age))]

st.subheader("📋 Student Dataset")

st.dataframe(filtered_df,use_container_width=True)

st.subheader("📈 Overall Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students",len(filtered_df))

col2.metric("Average Total Marks",round(filtered_df["Total"].mean(), 2))

col3.metric("Highest Total",filtered_df["Total"].max())

col4.metric("Lowest Total",filtered_df["Total"].min())

st.subheader("📚 Average Marks by Subject")

subjects = ["Maths","Physics","Chemistry","English","Computer"]

average_marks = filtered_df[subjects].mean()

fig, a = plt.subplots(figsize=(10, 5))

a.bar(average_marks.index,average_marks.values)

a.set_xlabel("Subjects")
a.set_ylabel("Average Marks")
a.set_title("Average Marks by Subject")
st.pyplot(fig)
st.subheader("🔬 Maths vs Physics")

fig, b = plt.subplots(figsize=(8, 5))

b.scatter(filtered_df["Maths"],filtered_df["Physics"])
b.set_xlabel("Maths Marks")
b.set_ylabel("Physics Marks")
b.set_title("Maths vs Physics Marks")
b.grid(True)
st.pyplot(fig)
st.subheader("📊 Total Marks Distribution")

fig, c = plt.subplots(figsize=(8, 5))

c.hist(filtered_df["Total"],bins=5,edgecolor="black")
c.set_xlabel("Total Marks")
c.set_ylabel("Number of Students")
c.set_title("Distribution of Total Marks")
st.pyplot(fig)
st.subheader("👨‍🎓 Gender Distribution")
gender_count = filtered_df["Gender"].value_counts()

fig, d = plt.subplots(figsize=(6, 6))

d.pie(gender_count.values,labels=gender_count.index,autopct="%1.1f%%",startangle=90)
d.set_title("Gender Distribution")
st.pyplot(fig)

st.subheader("🏆 Top 5 Students")

top5 = filtered_df.sort_values(by="Total",ascending=False).head(5)

st.dataframe(
    top5[
        [
            "Student ID",
            "Name",
            "Gender",
            "Age",
            "Maths",
            "Physics",
            "Chemistry",
            "English",
            "Computer",
            "Total"
        ]
    ],
    use_container_width=True)

fig, e = plt.subplots(figsize=(8, 5))

e.bar(top5["Name"],top5["Total"])
e.set_xlabel("Student")
e.set_ylabel("Total Marks")
e.set_title("Top 5 Students")
st.pyplot(fig)
st.subheader("🔍 Search Student")
student_name = st.selectbox("Select a Student",df["Name"].tolist())
student = df[df["Name"] == student_name].iloc[0]
col1, col2, col3 = st.columns(3)
col1.write(f"**Student ID:** {student['Student ID']}")
col1.write(f"**Name:**{student["Name"]}")
col2.write(f"**Gender:**{student["Gender"]}")
col2.write(f"**Age:**{student["Age"]}")
col3.write(f"**Total Marks:**{student["Total"]}")
student_subject_marks = student[subjects]

fig,f = plt.subplots(figsize=(9, 5))
f.bar(subjects,student_subject_marks.values)
f.set_xlabel("Subjects")
f.set_ylabel("Marks")
f.set_title(f"Marks of {student_name}")
st.pyplot(fig)
st.markdown("---")
st.write("📌 Student Performance Dashboard using Streamlit and Matplotlib")
