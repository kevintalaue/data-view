"""this python script will build the application hosted by streamlit"""

import pandas as pd
import streamlit as st

import plotly.graph_objects as go

from plotly.subplots import make_subplots

SPNS = [
    27,
    84,
    100,
    101,
    102,
    103,
    105,
    108,
    110,
    111,
    157,
    168,
    171,
    173,
    190,
    245,
    411,
    512,
    623,
    624,
    1127,
    1761,
    2659,
    3031,
    3216,
    3220,
    3226,
    3230,
    3236,
    3242,
    3246,
    3251,
    3482,
    3609,
    3610,
    3700,
    3701,
    3702,
    4334,
    4360,
    4363,
    4765,
    5077,
    5078,
    5079,
    5313,
    5506,
    5507,
]

# Upload file
uploaded_file = st.file_uploader(
    "Upload your data file (csv)",
    type=["csv"],
)


if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df[df["spn"].isin(SPNS)]
    df1 = pd.pivot_table(data=df, index="sampled_on", columns="spn", values="spn_value")

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
