import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def generate_time_serie_graph(df):
    """
    Generate a time serie graph
    """
    energy_columns = df.columns[1:] #exclude the timestamp column
    fig = make_subplots(rows=len(energy_columns), cols=1,shared_xaxes=True)
    for i, column in enumerate(energy_columns):
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df[column], mode="lines", name=column))
    # Update layout to make the chart more readable
    fig.update_layout(
        autosize=True,  # Automatically adjust the size of the chart
        title="Energy Generation Over Time",
        xaxis_title="Time",
        yaxis_title="Generation (MWh)",  # Adjust units if necessary
        legend_title="Energy Types",
        showlegend=True,  # Interactive legend enabled by default
        height=3000,  # Increase the height of the plot
        width=1000,
        hovermode="closest",
        xaxis=dict(
            showline=True,  # Show the x-axis line
            tickformat="%b %d %H",  # Customize date format (e.g., Month, Day, Year, Hour:Minute)
            tickangle=45,  # Rotate labels to avoid overlap
            nticks=20,
            tickmode="auto",  # Automatically determine the ticks 
            showticklabels=True,  # Show tick labels
            )
    )
    return fig

def correlation_matrix(df):
    """
    Generate a correlation matrix
    """
    if (len(df.columns) > 1):
        fig_corr = px.imshow(df.corr(), title='Correlation Matrix')
        return fig_corr
    else:    
        return None
    


