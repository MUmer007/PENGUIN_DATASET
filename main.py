import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
DataL = sns.load_dataset("penguins")

# Scatter plot
sns.scatterplot(
    x="bill_length_mm",
    y="bill_depth_mm",
    data=DataL,
    hue="sex",
    style="sex",
    palette="Accent",
    markers={"Male": "o", "Female": ">"}
)

plt.title("Bill Length vs Bill Depth by Sex")
plt.savefig("bill-len & bill-depth.png")
plt.show()


# BAR PLOT
plt.figure(figsize=(8,6))
sns.barplot(
    x="species", 
    y="bill_depth_mm", 
    hue="sex", 
    data=DataL, 
    palette="Accent", 
    ci="sd",           
    capsize=0.2,       
    alpha=0.85,        
    edgecolor="black",
    linewidth=1.2
)

plt.title("Average Bill Depth by Species and Sex", fontsize=14, weight="bold")
plt.xlabel("Penguin Species", fontsize=12)
plt.ylabel("Bill Depth (mm)", fontsize=12)
plt.legend(title="Sex", fontsize=10, title_fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("bill-len & bill-depth_BAR-PLOT.png")
plt.show()


# Histogram
plt.figure(figsize=(8,6))
sns.histplot(
    data=DataL, 
    x="flipper_length_mm", 
    hue="sex", 
    bins=20, 
    multiple="dodge",   
    palette="Accent", 
    edgecolor="black", 
    linewidth=1,
    alpha=0.8,
    kde=True            
)

plt.title("Distribution of Flipper Length by Sex", fontsize=14, weight="bold")
plt.xlabel("Flipper Length (mm)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Histogram_Flipper-length.png")  
plt.show()



# Load dataset
DataL = sns.load_dataset("penguins").head(100)

# Line Plot between flipper length & bill depth
plt.figure(figsize=(8,6))
sns.lineplot(
    data=DataL,
    x="flipper_length_mm",
    y="bill_depth_mm",
    hue="sex",        
    style="species",  
    markers=True,     
    dashes=False,     
    palette="Accent",
    linewidth=2
)

plt.title("Bill Depth vs Flipper Length", fontsize=14, weight="bold")
plt.xlabel("Flipper Length (mm)", fontsize=12)
plt.ylabel("Bill Depth (mm)", fontsize=12)
plt.legend(title="Sex / Species", fontsize=10, title_fontsize=11)
plt.grid(linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("Lineplot_BillDepth_vs_FlipperLength.png")
plt.show()

numeric_data = DataL[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]


corr = numeric_data.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

# Heatmap
plt.figure(figsize=(9,7))
sns.heatmap(
    corr,
    mask=mask,          
    annot=True,     
    fmt=".2f",      
    annot_kws={"size": 10, "weight": "bold", "color": "black"},
    cmap="YlGnBu",      
    vmin=-1, vmax=1,     
    center=0,
    square=True,         
    linewidths=1, 
    linecolor="white",
    cbar_kws={"shrink": 0.8, "aspect": 10}
)

plt.title("Correlation Heatmap of Penguin Measurements", fontsize=16, weight="bold", pad=20)
plt.xticks(rotation=45, ha="right", fontsize=11)
plt.yticks(rotation=0, fontsize=11)

plt.tight_layout()
plt.savefig("Penguins_Heatmap_Styled.png")
plt.show()


# Countplot
plt.figure(figsize=(8,6))
sns.countplot(
    data=DataL,
    x="species",
    hue="sex",
    palette="Accent",
    edgecolor="black",
    linewidth=1.2
)

plt.title("Count of Penguins by Species and Sex", fontsize=14, weight="bold")
plt.xlabel("Penguin Species", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(title="Sex", fontsize=10, title_fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("Penguins_Countplot.png")
plt.show()


# Violin Plot

plt.figure(figsize=(9,6))
sns.violinplot(
    data=DataL,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    split=True,          
    inner="quart",      
    palette="Accent",
    linewidth=1.2
)

plt.title("Distribution of Flipper Length by Species and Sex", fontsize=14, weight="bold")
plt.xlabel("Penguin Species", fontsize=12)
plt.ylabel("Flipper Length (mm)", fontsize=12)
plt.legend(title="Sex", fontsize=10, title_fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("Penguins_Violinplot.png")
plt.show()



# PAIR PLOT 

sns.set_theme(style="whitegrid", context="talk")

pair_plot = sns.pairplot(
    data=DataL,
    hue="species",
    palette="Spectral",      
    diag_kind="kde",
    corner=True,
    plot_kws={'s': 70, 'alpha': 0.8, 'edgecolor': 'black'},
    diag_kws={'fill': True}
)

pair_plot.fig.suptitle(
    "Colorful Pair Plot of Penguin Measurements",
    fontsize=18,
    weight="bold",
    y=1.02
)

pair_plot.fig.patch.set_facecolor("#fefefe")

plt.show()

# Strip Plot

penguins_clean = DataL.dropna(subset=["sex", "flipper_length_mm"])

sns.set_theme(style="whitegrid", context="talk", font_scale=1.1)

plt.figure(figsize=(9, 6))
sns.stripplot(
    data=penguins_clean,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    dodge=True,
    jitter=0.25,
    palette="Accent",
    alpha=0.7,
    size=6,
    linewidth=0.7,
    edgecolor="black"
)

plt.title("Strip Plot: Flipper Length Distribution by Species and Sex", fontsize=14, fontweight="bold")
plt.xlabel("Penguin Species", fontsize=12)
plt.ylabel("Flipper Length (mm)", fontsize=12)
plt.legend(title="Sex", fontsize=10, title_fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("Penguins_StripPlot.png", bbox_inches='tight')
plt.show()


# BOX PLOT


sns.set_theme(style="whitegrid", context="talk")

plt.figure(figsize=(9,6))
sns.boxplot(
    data=DataL,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    palette="rainbow",
    linewidth=1.3,
    width=0.6
)

plt.title("Box Plot of Flipper Length by Species and Sex", fontsize=16, weight="bold")
plt.xlabel("Penguin Species", fontsize=12)
plt.ylabel("Flipper Length (mm)", fontsize=12)
plt.legend(title="Sex", fontsize=10, title_fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("Penguins_BoxPlot.png", bbox_inches="tight")
plt.show()



sns.set_theme(style="whitegrid", context="talk")

factor_plot = sns.catplot(
    data=DataL,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    kind="bar",            
    palette="Set2",
    height=6,
    aspect=1.3
)

factor_plot.fig.suptitle(
    "Factor Plot of Flipper Length by Species and Sex",
    fontsize=16,
    weight="bold",
    y=1.03
)

factor_plot.fig.patch.set_facecolor("#fdfdfd")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("Penguins_FactorPlot.png", dpi=300, bbox_inches="tight")
plt.show()


# CAT PLOT

sns.set_theme(style="whitegrid", context="talk")

cat_plot = sns.catplot(
    data=DataL,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    kind="boxen",
    palette="Set2",
    height=6,
    aspect=1.3,
    errorbar="sd"     # replaces deprecated 'ci' parameter
)

cat_plot.fig.suptitle(
    "Cat Plot (Bar) — Flipper Length by Species and Sex",
    fontsize=16,
    weight="bold",
    y=1.03
)

plt.tight_layout()
plt.savefig("Penguins_CatPlot_Bar.png", bbox_inches="tight")
plt.show()


# FACET GRID
g = sns.FacetGrid(
    DataL,
    col="species",
    hue="sex",
    palette="Spectral",
    height=5,
    aspect=1.1
)

# Add scatter and regression lines in each facet
g.map_dataframe(
    sns.scatterplot,
    x="bill_length_mm",
    y="flipper_length_mm",
    s=70,
    alpha=0.8,
    edgecolor="black"
)

g.map_dataframe(
    sns.lineplot,
    x="bill_length_mm",
    y="flipper_length_mm",
    estimator=None,
    lw=1.5,
    alpha=0.6
)

# Add titles and legend
g.add_legend(title="Sex", fontsize=10, title_fontsize=11)
g.set_axis_labels("Bill Length (mm)", "Flipper Length (mm)", fontsize=12)
g.set_titles(col_template="{col_name}", size=13, weight="bold")

# Add a global title and style tweaks
g.fig.suptitle(
    "FacetGrid: Bill Length vs Flipper Length by Species and Sex",
    fontsize=18,
    weight="bold",
    y=1.05
)

g.fig.patch.set_facecolor("#f8f9fa")

for ax in g.axes.flatten():
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_facecolor("#ffffff")

plt.tight_layout()
plt.savefig("Penguins_FacetGrid_Advanced.png", dpi=300, bbox_inches="tight")
plt.show()
    