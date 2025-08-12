import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from calculations import calculate_matrix

st.set_page_config(page_title="Volatility Arbitrage Surface", page_icon="icon.png")

st.title("Volatility Arbitrage Surface")

st.sidebar.title("Model Parameters")
st.sidebar.text("Inputs to get IV (Implied Volatility) from Black Scholes Model")
strike = st.sidebar.number_input("Strike Price", value=0.00, min_value=0.0)
time = st.sidebar.number_input("Time to Maturity (Years)", value=0.00, min_value=0.0)
rate = st.sidebar.number_input("Risk free Rate", min_value=0.00, max_value=1.00)
op = st.sidebar.number_input("Option Price", min_value=0.00)
st.sidebar.title("Realized Volatility")
realized_vol = st.sidebar.number_input("Realized Volatility", value=0.00, min_value=0.0)
st.sidebar.title("Visual Spot Price Configuration")
min_spot = st.sidebar.number_input("Min Spot Price", value=0.00, min_value=0.0)
max_spot = st.sidebar.number_input("Max Spot Price", value=0.00, min_value=0.0)
st.sidebar.title("Visual Y Axis Configuration")
st.session_state.y_axis = st.sidebar.selectbox("Select Y-Axis", ["Risk free Rate","Time to Maturity (Years)"])
min_y = st.sidebar.number_input("Min "+st.session_state.y_axis, value=0.00, min_value=0.0)
max_y = st.sidebar.number_input("Max "+st.session_state.y_axis, value=0.00, min_value=0.0)

github_url = "https://github.com/danielhyuncoder"
github_icon_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

# Markdown with an image and link
st.sidebar.markdown(
    f"""
    <a href="{github_url}" target="_blank" style="text-decoration: none; display: flex; align-items: center;">
        <span style="font-weight: bold; margin-right: 8px; color: inherit;">Created by Daniel Hyun</span>
        <img src="{github_icon_url}" width="20" height="20" alt="GitHub Logo">
    </a>
    """,
    unsafe_allow_html=True
)

if strike > 0 and time > 0 and rate > 0 and op > 0 and max_spot > 0 and max_y>0 and min_spot>0:
    fig, ax = plt.subplots()
    range_x = max_spot - min_spot
    range_y = max_y - min_y
    unit_x = max(range_x, 0.00001) / 10
    unit_y = max(range_y, 0.00001) / 10
    x_labels = np.round(np.arange(min_spot, max_spot + unit_x, unit_x), 2)
    y_labels = np.round(np.arange(min_y, max_y + unit_y, unit_y), 2)

    sns.heatmap(
        calculate_matrix(
            x_labels, y_labels,
            st.session_state.y_axis,
            realized_vol, strike, time, rate, op, "call"
        ),
        annot=True, cmap='magma', ax=ax,
        xticklabels=x_labels, yticklabels=y_labels
    )
    ax.set_title("Volatility Arbitrage (RV - IV) for CALL options")
    ax.set_xlabel("Spot Price")
    ax.set_ylabel(st.session_state.y_axis)
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    sns.heatmap(
        calculate_matrix(
            x_labels, y_labels,
            st.session_state.y_axis,
            realized_vol, strike, time, rate, op, "put"
        ),
        annot=True, cmap='magma', ax=ax2,
        xticklabels=x_labels, yticklabels=y_labels
    )
    ax2.set_title("Volatility Arbitrage (RV - IV) for PUT options")
    ax2.set_xlabel("Spot Price")
    ax2.set_ylabel(st.session_state.y_axis)
    st.pyplot(fig2)
else:
    st.write("Please input all the fields in order to see the heatmap visualizations.")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    sys.argv = ["streamlit", "run", "main.py", "--server.port", str(port), "--server.address", "0.0.0.0"]
    sys.exit(stcli.main())
