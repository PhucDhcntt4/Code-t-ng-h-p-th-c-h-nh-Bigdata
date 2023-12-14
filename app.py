from vega_datasets import data
import streamlit as st
import altair as alt


def load_data():

    return data.cars()

def visualize_data(df, x_axis, y_axis):

    chart = alt.Chart(df).mark_circle().encode(
        x=x_axis,
        y=y_axis,
        tooltip=[x_axis, y_axis]
    ).interactive()



def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("This is your data explorer")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)

if __name__ == "__main__":
    main()
