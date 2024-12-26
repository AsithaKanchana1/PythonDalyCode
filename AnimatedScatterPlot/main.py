import plotly.express as px

data = px.data.gapminder()

fig = px.scatter(
    data,
    x = "gdpPercap",
    y = "lifeExp",
    animation_frame = "year",
    animation_grupe = "country",
    size = "pop",
    color = "continent",
    hover_name = "country",
    log_x = True,
    size_max = 55,
    range_x = [200, 60000],
    range_y = [25, 90],
    title = "Animater Scatter Plot : Life Expectency vs GOP Per Capita"
    
)
fig.show()
