import streamlit as st

def main():
    st.set_page_config(
        page_title="Home",
    )
    st.sidebar.header("EDA")
    # Add title to the app
    st.title('Best hacking league, AI')
    st.header('Exploratory Data Analysis')

    st.image('pierwszy.jpeg', caption='Correlation Matrix')
    st.image('drugi.jpeg', caption='User behaviour')
    st.image('trzeci.jpeg', caption='Cost data')
    st.image('czwarty.jpeg', caption='Missing values')

if __name__ == '__main__':
    main()
