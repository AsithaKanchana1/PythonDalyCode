import plotly.express as px

data = px.data.gapminder()

fig = px.scatter(
    data,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",  # Corrected argument
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[200, 60000],
    range_y=[25, 90],
    title="Animated Scatter Plot: Life Expectancy vs GDP Per Capita"
)
fig.show()
