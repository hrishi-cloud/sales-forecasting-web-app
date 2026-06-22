print("Sales Forecasting & Business Analytics Web Application")

sales_data = [12000, 15000, 17000, 16000, 18000]

total_sales = sum(sales_data)

average_sales = total_sales / len(sales_data)

print("Total Sales:", total_sales)
print("Average Monthly Sales:", average_sales)

forecast = average_sales * 1.05

print("Next Month Forecast:", round(forecast))
