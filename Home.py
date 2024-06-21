
import streamlit as st


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Chat App! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
         - Chat with Multiple PDFs
         - Chat with Websites
         """

    )


if __name__ == "__main__":
    run()