stocks = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2800,
    "HDFC": 1700,
    "WIPRO": 450,
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMAZON": 135,
    "MICROSOFT": 330,
    "META": 310,
    "NVIDIA": 900,
    "ADANI": 3200,
    "SBI": 820,
    "ITC": 430
}

portfolio = {}
grand_total = 0

print("==========================================")
print("      ADVANCED STOCK PORTFOLIO TRACKER")
print("==========================================")

# Display available stocks
print("\nAvailable Stocks:\n")

for stock, price in stocks.items():
    print(stock, "=", "₹", price)

# Number of stocks
n = int(input("\nHow many stocks do you want to buy? : "))

# User Input
for i in range(n):

    print("\n----------------------------------")

    stock_name = input("Enter Stock Name : ").upper()

    if stock_name in stocks:

        quantity = int(input("Enter Quantity : "))

        stock_price = stocks[stock_name]

        total = stock_price * quantity

        grand_total += total

        portfolio[stock_name] = {
            "Price": stock_price,
            "Quantity": quantity,
            "Total": total
        }

        print("Stock Added Successfully!")

    else:
        print("Stock not available!")

# Display Portfolio Summary
print("\n==========================================")
print("            PORTFOLIO SUMMARY")
print("==========================================")

for stock, details in portfolio.items():

    print("\nStock Name :", stock)
    print("Stock Price : ₹", details["Price"])
    print("Quantity :", details["Quantity"])
    print("Total Amount : ₹", details["Total"])

# Grand Total
print("\n------------------------------------------")
print("TOTAL INVESTMENT VALUE : ₹", grand_total)

# Profit Prediction
profit_percent = 12

future_value = grand_total + (grand_total * profit_percent / 100)

profit_amount = future_value - grand_total

print("\nExpected Profit (12%) : ₹", profit_amount)
print("Future Portfolio Value : ₹", future_value)

# Highest Investment Stock
highest_stock = max(portfolio, key=lambda x: portfolio[x]["Total"])

print("\nHighest Investment Stock :", highest_stock)

# Save Report
choice = input("\nDo you want to save report? (yes/no) : ").lower()

if choice == "yes":

    file = open("stock_report.txt", "w")

    file.write("ADVANCED STOCK PORTFOLIO REPORT\n")
    file.write("====================================\n")

    for stock, details in portfolio.items():

        file.write(f"\nStock Name : {stock}\n")
        file.write(f"Stock Price : ₹{details['Price']}\n")
        file.write(f"Quantity : {details['Quantity']}\n")
        file.write(f"Total Amount : ₹{details['Total']}\n")

    file.write("\n------------------------------------\n")
    file.write(f"TOTAL INVESTMENT : ₹{grand_total}\n")
    file.write(f"EXPECTED PROFIT : ₹{profit_amount}\n")
    file.write(f"FUTURE VALUE : ₹{future_value}\n")
    file.write(f"HIGHEST INVESTMENT STOCK : {highest_stock}\n")

    file.close()

    print("\nReport saved as stock_report.txt")

print("\n==========================================")
print("Program Ended Successfully")
print("==========================================")
