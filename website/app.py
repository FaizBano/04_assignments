import streamlit as st

# Page settings
st.set_page_config(page_title="Faiz Bano's Portfolio", page_icon="🧑‍💻", layout="wide")

# Profile Section
st.title("👋 Hi, I'm Faiz Bano , Frontend Developer")
st.image("ff.jpg", width=200)
st.write("I'm a frontend developer passionate about building web apps using Next.js, TypeScript, Python, and more!")

# Skills
st.header("🛠️ My Skills")
st.write("- HTML, CSS, JavaScript")
st.write("- TypeScript, React, Next.js")
st.write("- Python, Streamlit")
st.write("- Git, GitHub, VS Code")

# Projects
st.header("💼 My Projects")

st.subheader("🔐 Password Generator (Python)")
st.image("pic2.png", width=500)
st.write("A secure password generator app with strength checking and clipboard support.")

st.subheader("📚 Personal Library Management System (Python)")
st.image("pic3.png", width=500)
st.write("Personal Library Management System app manage all books like add new books, delee, updae etc it is a perfect app for any Library")

# Contact
st.header("📞 Contact Me")
st.write("📧 Email: faizbano02@gmail.com")
st.write("🔗 GitHub: [github.com/faizbano](https://github.com/faizbano)")
