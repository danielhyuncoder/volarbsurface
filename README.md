# 📈 Volatility Arbitrage Dashboard

This is an interactive Streamlit web application for visualizing **Volatility Arbitrage** opportunities using heatmaps of **Implied Volatility (IV)** minus **Realized Volatility (RV)** for both call and put options.

> 🔗 [**Launch the App**](https://volarbsurface.onrender.com)

---

## 🔍 What is Volatility Arbitrage?

Volatility arbitrage is a trading strategy that seeks to exploit differences between an asset's **implied volatility** (derived from option prices) and its **realized volatility** (historical actual movement). When these differ significantly, it may signal potential mispricings in the options market.

---

## 🚀 Features

- Built with **Streamlit** for fast and interactive deployment.
- Input key option parameters:
  - Option market price
  - Strike price
  - Time to maturity
  - Risk-free rate
  - Realized volatility
  - Min/Max spot price
- Choose a variable for the Y-axis:
  - Risk-free rate
  - Time to maturity
- Set the Y-axis range dynamically.
- Visualizes IV - RV across different spot and Y-axis values in two separate heatmaps:
  - 📊 Call Options
  - 📊 Put Options

---

## 🖼️ Example Outputs

The app generates two color-coded heatmaps where:
- **X-axis**: Varies the spot price
- **Y-axis**: Varies either risk-free rate or time to maturity (as selected)
- **Color**: Represents `IV - RV`, highlighting over/underpriced areas

---

## ⚙️ How It Works

1. User provides inputs through a sidebar form.
2. The app computes implied volatility using the Black-Scholes model.
3. It constructs a matrix of IV - RV values across varying spot prices and the selected Y-axis variable.
4. Two heatmaps are displayed: one for **Call options**, one for **Put options**.

---

## 📂 How to Run Locally

### Prerequisites

- Python 3.7+
- `pip` (Python package manager)

### Installation

```bash
git clone https://github.com/yourusername/volatility-arbitrage-dashboard.git
cd volatility-arbitrage-dashboard
pip install -r requirements.txt
streamlit run app.py

