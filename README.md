# Wk6-with-Python
This is an attempt to visualize data from a CSV file by creating different charts using python

Ensure you have the original .csv file in the same directory as the .py file you want to run.

By running the python code in 'visualize_expenses.py' a newly created file named orgenized_expense_data.csv is created together with bar_chart.png, line_graph.png and pie_chart.png in the same directory as the original CSV file and your .py file.

The images are created and saved in the directory without being rendered by omitting the display call 'plt.show()'.
This is because 
1. Blocking behaviour: plt.show() is a blocking call that pauses the execution of your script until you close the plot window. This can be problematic if you have a long script or are running multiple scripts in parallel.
2. Increased Memory Usage: Rendering and displaying multiple plots at once can consume significant memory, especially if the plots are large or if you are generating many plots in a loop among other issues.