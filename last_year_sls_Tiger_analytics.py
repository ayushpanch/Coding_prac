# Remove rows where Customer_LSTYR_Sales is NaN for analysis purposes
cleaned_data = data.dropna(subset=['Customer_LSTYR_Sales'])

# Group by Customer_Number to aggregate sales and quantities
customer_summary = cleaned_data.groupby('Customer_Number').agg({
    'Customer_LSTYR_Sales': 'sum',
    'Quantity_Shipped': 'sum'
}).reset_index()

# Define thresholds
# Loyal high-value customers: top 10% in terms of sales
loyal_threshold = customer_summary['Customer_LSTYR_Sales'].quantile(0.90)

# Low-value high-volume customers: bottom 50% in terms of sales but top 25% in quantity shipped
low_value_threshold = customer_summary['Customer_LSTYR_Sales'].quantile(0.50)
high_volume_threshold = customer_summary['Quantity_Shipped'].quantile(0.75)

# Filter loyal high-value customers
loyal_high_value_customers = customer_summary[customer_summary['Customer_LSTYR_Sales'] >= loyal_threshold]

# Filter low-value high-volume customers
low_value_high_volume_customers = customer_summary[
    (customer_summary['Customer_LSTYR_Sales'] <= low_value_threshold) &
    (customer_summary['Quantity_Shipped'] >= high_volume_threshold)
]

# Show the results
loyal_high_value_customers.head(), low_value_high_volume_customers.head()
