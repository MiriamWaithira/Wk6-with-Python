# LOADING AND SAVING THE NEW CSV FILE
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with the correct delimiter
file_path = 'Expense data.csv'
df = pd.read_csv(file_path, delimiter=';')

# Rename the columns to match the specified format
df.columns = ['Date', 'Item', 'Amount', 'Category', 'Time', 'Day']

# Save the organized data to a new CSV file
new_file_path = 'organized_expense_data.csv'
df.to_csv(new_file_path, index=False)

# Ensure correct date format by setting dayfirst=True
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='%d/%m/%Y')

# CREATING THE VISUALIZATIONS

# Bar Chart: Total amount spent per category
plt.figure(figsize=(10, 6))
df.groupby('Category')['Amount'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Amount Spent per Category')
plt.xlabel('Category')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
print("Bar chart saved as 'bar_chart.png'")

# Line Graph: Amount spent over time
plt.figure(figsize=(10, 6))
df.groupby('Date')['Amount'].sum().plot(kind='line', marker='o', color='green')
plt.title('Amount Spent Over Time')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.grid(True)
plt.tight_layout()
plt.savefig('line_graph.png')
print("Line graph saved as 'line_graph.png'")

# Pie Chart: Percentage of total amount spent per category
plt.figure(figsize=(8, 8))
df.groupby('Category')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Percentage of Total Amount Spent per Category')
plt.ylabel('')  # Remove the y-label
plt.tight_layout()
plt.savefig('pie_chart.png')
print("Pie chart saved as 'pie_chart.png'")
