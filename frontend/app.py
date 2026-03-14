import streamlit as st
import requests

API_URL = "http://127.0.0.1:5050/analyze-repository"


st.set_page_config(
    page_title="GitHub Portfolio Evaluation Agent",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 GitHub Portfolio Evaluation Agent")
st.write(
    "Analyze a developer's GitHub repository using AI to evaluate portfolio quality."
)

repo_url = st.text_input(
    "Enter GitHub Repository URL",
    placeholder="https://github.com/user/project"
)


if st.button("Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")
    else:

        with st.spinner("Analyzing repository..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"repo_url": repo_url}
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Analysis Completed!")

                    st.subheader("📊 Portfolio Score")

                    st.metric(
                        label="Score",
                        value=result["portfolio_score"]
                    )

                    st.subheader("🧠 Skills Detected")

                    skills = result.get("skills", [])

                    if skills:
                        for skill in skills:
                            st.write(f"• {skill}")
                    else:
                        st.write("No skills detected")

                    st.subheader("💡 AI Insights")

                    st.write(result["insights"])

                else:
                    st.error("Error from API")

            except Exception as e:
                st.error(f"Error: {str(e)}")