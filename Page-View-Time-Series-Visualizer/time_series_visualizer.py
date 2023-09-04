import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

df['date'] = pd.to_datetime(df['date'])

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15, 4))
    plt.plot(df['date'], df['value'], label='Data')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    # Define a mapping of numeric month values to month names
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    # Add a new column 'MonthName' with the month names
    df['month-name'] = df['month'].map(month_names)
  
    df_bar = df.groupby(['year', 'month-name'])['value'].mean().reset_index()

    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw bar plot
    pivot_data = df_bar.pivot(index='year', columns='month-name', values='value')
    pivot_data.plot(kind='bar', width=0.8, align='center', ax=ax)

    # Customize the chart
    plt.title('Monthly Values Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.xticks(rotation=0)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Define a mapping of numeric month values to month names
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create a new figure
    fig = plt.figure(figsize=(15, 6))
    plt.subplot(121)  # Left subplot for year-wise box plot
    sns.boxplot(data=df, x='year', y='value')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Create month-wise box plot
    plt.subplot(122)  # Right subplot for month-wise box plot
    sns.boxplot(data=df, x='month-name', y='value', order=month_names.values())
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

