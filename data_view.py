"""this python script will build the application hosted by streamlit"""

import pandas as pd
import streamlit as st

import plotly.graph_objects as go

from plotly.subplots import make_subplots

from data_view.config import SPNS

# Title
st.title("Welcome to Data-View")

st.write(
    f"""
    Welcome to this open-source web app that lets you upload a CSV file containing time series telematics data for visualization and interaction.\n
    The supported file format requires the first row to contain column headers, with the datetime in the first column as the index.\n
    """
)

# Upload file
uploaded_file = st.file_uploader(
    "Upload your data file (csv)",
    type=["csv"],
)


if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df[df["spn"].isin(SPNS)]
    df1 = pd.pivot_table(
        data=df, index="sampled_on", columns="spn", values="spn_value", sort=True
    )

    start_date = df1.index.min()
    end_date = df1.index.max()

    st.write(
        f"""
             Data Start {start_date}\n
             Data End {end_date}
        """
    )

    cols_to_plot = df1.columns

    # Create subplots for the current page
    fig = make_subplots(
        rows=len(cols_to_plot),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.01,  # Reduced spacing
    )

    # Add traces and set y-axis labels
    for row, col in enumerate(cols_to_plot, start=1):
        fig.add_trace(
            go.Scatter(x=df1.index, y=df1[col], name=str(col), mode="markers"),
            row=row,
            col=1,
        )
        fig.update_yaxes(title_text=str(col), row=row, col=1)

    # Update layout for the current page
    fig.update_layout(
        title=f"Telematics Data",
        height=300 * len(cols_to_plot),  # Dynamic height for the page
        hovermode="x unified",
        showlegend=False,
    )

    st.plotly_chart(fig)
