import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = ((df['gluc'] > 1).astype(int))
df['cholesterol'] = ((df['cholesterol'] > 1).astype(int))

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',  
        hue='value',
        col='cardio', 
        height=4,     
        aspect=1.2,    
      )
    g.set_axis_labels('Variable', 'Total')
    
    # Get the figure for the output
    fig = g

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.75},
        mask=mask,
        vmin=-0.2,  # Set the minimum value
        vmax=0.3,   # Set the maximum value
    )

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
