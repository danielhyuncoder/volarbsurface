from scipy.stats import norm
import numpy as np
import math

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price

def implied_volatility(S, K, T, r, market_price, option_type='call', tol=1e-6, max_iterations=100):

    sigma_low = 1e-6
    sigma_high = 5.0

    for i in range(max_iterations):
        sigma_mid = (sigma_low + sigma_high) / 2
        price = black_scholes_price(S, K, T, r, sigma_mid, option_type)
        diff = price - market_price

        if abs(diff) < tol:
            return sigma_mid

        if diff > 0:
            sigma_high = sigma_mid
        else:
            sigma_low = sigma_mid

    return sigma_mid

def calculate_matrix(x_labels: np.array, y_labels: np.array, y_axis: str, realized_volatility: float, K:float, T:float, r:float, option_price: float, option_type:str):
    matrix=[]
    for j in y_labels:
        row=[]
        for i in x_labels:
            if "Risk" in y_axis:
               row.append(np.round(implied_volatility(i, K, T, j, option_price, option_type=option_type) - realized_volatility, 2))

            else:
               row.append(np.round(implied_volatility(i,K,i,r,option_price, option_type=option_type)-realized_volatility, 2))
        matrix.append(row)
    return np.array(matrix)
