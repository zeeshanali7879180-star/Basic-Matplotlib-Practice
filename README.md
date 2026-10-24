📊 Cake Sales Graph Using Matplotlib

A beginner-friendly Python project that demonstrates how to create and customize a line plot using Matplotlib.

This project visualizes daily cake sales using a line graph and demonstrates how to customize plot colors, line styles, markers, titles, axis labels, grid lines, and legends.

It is a simple project designed to understand the fundamentals of data visualization in Python.

✨ Features
📈 Line Plot: Visualize daily cake sales using a line graph.
🎨 Custom Colors: Change the color of the plotted line.
➖ Line Styles: Customize the line using a dashed style.
🔴 Markers: Display circular markers for individual data points.
📝 Plot Title: Add a descriptive title to the graph.
📌 Axis Labels: Label the horizontal and vertical axes.
📏 Grid Lines: Add grid lines to improve readability.
🏷️ Legend: Identify the data series using a legend.
🖥️ Graph Display: Display the final plot using plt.show().
🛠️ Technologies Used
Programming Language: Python 3
Library: Matplotlib
Visualization Type: Line Plot
📋 Requirements

To run this project, you need:

Python 3 installed on your computer.
Matplotlib installed in your Python environment.
A code editor, such as PyCharm or Visual Studio Code.
🚀 Installation and Setup
Step 1: Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder
bash
cd YOUR_PROJECT_FOLDER

Step 3: Install Matplotlib
bash
pip install matplotlib

Step 4: Run the Python Program

If your Python file is named cake_sales.py, run:

bash
python cake_sales.py


Note: Replace the example repository URL, folder name, and Python filename with your actual project details.

💻 Project Code
python
import matplotlib.pyplot as plt

# Enter days of the week
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Enter cake sales per day
y = [20, 34, 25, 15, 5]

# Create the line plot
plt.plot(
    x,
    y,
    color='red',
    linestyle='dashed',
    marker='o',
    label='Daily Cake Sales'
)

# Add title and axis labels
plt.title("Cake Sales Graph")
plt.xlabel("Days of the Week")
plt.ylabel("Sales")

# Add grid lines
plt.grid(linestyle='--', color='green')

# Display the legend
plt.legend()

# Display the graph
plt.show()

📊 Sample Dataset

The project uses the following sample data:

Day	Cake Sales
Monday	20
Tuesday	34
Wednesday	25
Thursday	15
Friday	5

The line graph represents the number of cakes sold on each day.

📖 Matplotlib Concepts Covered
1. Creating a Line Plot

Use plt.plot() to visualize the relationship between two sets of data.

2. Customizing Colors and Line Styles

Use parameters such as color, linestyle, and marker to customize the appearance of a graph.

3. Adding a Title

Use plt.title() to add a descriptive title.

4. Adding Axis Labels
plt.xlabel() labels the horizontal axis.
plt.ylabel() labels the vertical axis.
5. Adding Grid Lines

Use plt.grid() to display grid lines behind the plot.

6. Adding a Legend

Use the label parameter inside plt.plot() and call plt.legend() to identify the plotted data series.

7. Displaying the Graph

Use plt.show() to display the completed visualization.

🎯 Learning Objectives

Through this project, I practiced:

Importing and using the Matplotlib library.
Creating basic line plots.
Visualizing data using the X-axis and Y-axis.
Customizing line colors, styles, and markers.
Adding titles and axis labels.
Displaying grid lines and legends.
Improving the readability of data visualizations.
🔮 Future Improvements

This project can be improved by adding:

Bar charts for comparing daily sales.
Pie charts for displaying sales distribution.
Multiple lines to compare different products.
Real-world sales datasets.
Data visualization using Pandas.
Saving graphs as PNG or PDF files.
More advanced plot customization.
👨‍💻 Author

Your Name

Aspiring Python Developer | Learning Python and Data Visualization

GitHub: My GitHub Profile
📄 License

This project is created for educational purposes and to develop practical Python data visualization skills.
