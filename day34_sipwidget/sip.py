import ipywidgets as widgets
import locale
import pandas as pd
from IPython.display import display

# Set the locale for Indian numbering system
locale.setlocale(locale.LC_NUMERIC, 'en_IN')

def format_currency(amount):
    """
    Format the amount in Indian numbering system.

    Args:
        amount (float): The amount to format.

    Returns:
        str: The formatted amount.
    """
    if amount >= 1e7 or amount <= -1e7 :
        return f'₹{amount / 1e7:.1f} Cr'
    elif amount >= 1e5 or amount <= -1e5:
        return f'₹{amount / 1e5:.1f} L'
    elif amount >= 1e3 or amount <= -1e3:
        return f'₹{amount / 1e3:.1f} K'
    else:
        return f'₹{amount:.1f}'

def sip_calculator(monthly_investment, expected_return_rate, time_period, current_age):
    """
    Calculates the estimated returns and total value for a Systematic Investment Plan (SIP).

    Args:
        monthly_investment (float): Monthly investment amount.
        expected_return_rate (float): Expected annual return rate as a decimal (e.g., 0.12 for 12%).
        time_period (int): Investment time period in years.
        current_age (int): Current age of the investor.

    Returns:
        pandas.DataFrame: DataFrame containing the investment details for each year.
    """
    n = time_period * 12  # Number of payments
    i = expected_return_rate / 12  # Periodic rate of interest
    
    data = []
    total_investment = 0
    
    for year in range(1, time_period + 1):
        total_investment += monthly_investment * 12
        total_value = monthly_investment * ((1 + i) ** (year * 12) - 1) / i * (1 + i)
        estimated_returns = total_value - total_investment
        data.append([current_age + year - 1, year, format_currency(monthly_investment),format_currency(total_investment), format_currency(estimated_returns), format_currency(total_value)])
    
    df = pd.DataFrame(data, columns=['Age', 'Year', 'Monthly Investment','Total Investment Year', 'Estimated Returns', 'Total Value']).set_index('Year')
    return df

# Create interactive widgets with styled descriptions
monthly_investment_slider = widgets.IntSlider(value=1000, min=1000, max=100000, step=1000, description='Monthly investment (₹):', continuous_update=False, style={'description_width': 'initial'})
expected_return_rate_slider = widgets.FloatSlider(value=0.10, min=0.01, max=0.2, step=0.01, description='Expected return rate:', continuous_update=False, style={'description_width': 'initial'})
time_period_slider = widgets.IntSlider(value=10, min=1, max=30, step=1, description='Time period (years):', continuous_update=False, style={'description_width': 'initial'})
current_age_slider = widgets.IntSlider(value=25, min=18, max=100, step=1, description='Current age:', continuous_update=False, style={'description_width': 'initial'})

# Create an output widget for displaying results
output_widget = widgets.Output()

def display_results(change):
    df = sip_calculator(monthly_investment_slider.value, expected_return_rate_slider.value, time_period_slider.value, current_age_slider.value)
    with output_widget:
        output_widget.clear_output()
        display(df)

# Call display_results initially to show initial values
display_results(None)

# Observe changes and display results
monthly_investment_slider.observe(display_results, names='value')
expected_return_rate_slider.observe(display_results, names='value')
time_period_slider.observe(display_results, names='value')
current_age_slider.observe(display_results, names='value')

# Display the widgets
widgets.VBox([
    monthly_investment_slider,
    expected_return_rate_slider,
    time_period_slider,
    current_age_slider,
    output_widget
])
