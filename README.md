# PENGUIN_DATASET
🐧 Penguin Data Visualization with Seaborn & Matplotlib

This project demonstrates advanced data visualization techniques using the Palmer Penguins dataset.
It explores relationships between penguin physical measurements such as bill length, bill depth, flipper length, and body mass, categorized by species and sex.

The project uses Seaborn for high-level statistical plotting and Matplotlib for fine-grained control and saving figures.

📁 Dataset

Dataset Name: Palmer Penguins

Source: Seaborn built-in dataset (sns.load_dataset("penguins"))

Records Used:

Full dataset for most plots

First 100 rows for line plot and multivariate analysis

Key Features Used:

species

sex

bill_length_mm

bill_depth_mm

flipper_length_mm

body_mass_g

🛠️ Technologies & Libraries

Python

Pandas – Data handling

NumPy – Numerical operations

Matplotlib – Plot customization & saving

Seaborn – Statistical data visualization

📊 Visualizations Included
1️⃣ Scatter Plot – Bill Length vs Bill Depth

Colored and styled by sex

Shows relationship between bill dimensions

Saved as: bill-len & bill-depth.png

2️⃣ Bar Plot – Average Bill Depth

Comparison by species and sex

Displays standard deviation as error bars

Saved as: bill-len & bill-depth_BAR-PLOT.png

3️⃣ Histogram – Flipper Length Distribution

Split by sex

Includes KDE curve for smooth distribution

Saved as: Histogram_Flipper-length.png

4️⃣ Line Plot – Bill Depth vs Flipper Length

Shows trends by sex

Styled by species

Uses markers for better readability

Saved as: Lineplot_BillDepth_vs_FlipperLength.png

5️⃣ Correlation Heatmap

Displays correlations between numeric features

Upper triangle masked for clarity

Saved as: Penguins_Heatmap_Styled.png

6️⃣ Count Plot – Penguins by Species and Sex

Visualizes count distribution

Saved as: Penguins_Countplot.png

7️⃣ Violin Plot – Flipper Length Distribution

Split violins by sex

Shows quartiles inside the distribution

Saved as: Penguins_Violinplot.png

8️⃣ Pair Plot

Multivariate relationships between measurements

Colored by species

KDE used on diagonal plots

9️⃣ Strip Plot – Flipper Length

Displays individual data points

Includes jitter for better separation

Saved as: Penguins_StripPlot.png

🔟 Box Plot – Flipper Length

Compares distributions by species and sex

Highlights medians and outliers

Saved as: Penguins_BoxPlot.png

1️⃣1️⃣ Factor Plot (Categorical Bar Plot)

Mean flipper length by species and sex

Saved as: Penguins_FactorPlot.png

1️⃣2️⃣ Cat Plot (Boxen Plot)

Enhanced box plot for large distributions

Saved as: Penguins_CatPlot_Bar.png

1️⃣3️⃣ FacetGrid – Advanced Visualization

Separate panels for each species

Scatter + line plots by sex

Highly customized layout

Saved as: Penguins_FacetGrid_Advanced.png

▶️ How to Run the Project

Install required libraries:

pip install pandas numpy matplotlib seaborn


Run the Python script:

python penguins_visualization.py

📌 Output

All plots are:

Displayed interactively

Saved as high-quality .png files

Suitable for:

Data analysis reports

Assignments

Portfolio projects

Data visualization practice

🎯 Learning Objectives

Master Seaborn plot types

Understand categorical vs numerical visualization

Learn styling and aesthetics

Perform multivariate analysis

Practice real-world EDA workflows

✨ Author
Umer Shaikh

Umer Shaikh

If you want, I can also
