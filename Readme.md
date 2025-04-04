# Animated Scatter Plot: Life Expectancy vs GDP Per Capita 📊🌏✨

This project demonstrates how to create an animated scatter plot using the Plotly library in Python. The animation visualizes the relationship between GDP per capita and life expectancy over time for different countries. 🚀🌍⚛️

## Features 🎉🎨💡

- **Interactive Scatter Plot**: Visualize GDP per capita on the x-axis and life expectancy on the y-axis.
- **Animation**: Watch changes over time.
- **Dynamic Elements**:
  - Bubble size represents the population.
  - Bubble color categorizes by continent.
- **Hover Tooltips**: Display detailed information for each country when hovering over the data points.

## Prerequisites 🔢🎨🛠️

Make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation 📚🔧🌐

1. Clone the repository:

   ```bash
   git clone https://github.com/Asithakanchana1/animated-scatter-plot.git
   cd animated-scatter-plot
   ```

2. Install the required Python libraries:

   ```bash
   pip install plotly
   ```

## Code Explanation 📝🌈🔍

The code creates an animated scatter plot using Plotly's `express` module:

```python
import plotly.express as px

data = px.data.gapminder()

fig = px.scatter(
    data,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_grupe="country",
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
```

### Key Components: 📊🌍🔬

1. **`px.data.gapminder()`**:
   - Provides sample data on GDP per capita, life expectancy, population, and continents over the years.

2. **`px.scatter`**:
   - Creates the scatter plot with animation.

3. **Parameters**:
   - `x` and `y`: Map GDP per capita and life expectancy, respectively.
   - `animation_frame`: Adds animation over years.
   - `size`: Bubble size based on population.
   - `color`: Categorizes data by continent.
   - `hover_name`: Shows country names on hover.
   - `log_x`: Converts the x-axis to a logarithmic scale.
   - `size_max`: Limits the maximum bubble size.
   - `range_x` and `range_y`: Set axis ranges.

## How to Run 🚀🌐⚡

1. Open a terminal or command prompt in the project directory.

2. Run the script:

   ```bash
   python main.py
   ```

3. A browser window will open, displaying the animated scatter plot.

## Output 🎨🌍🌆

The scatter plot shows how life expectancy and GDP per capita change over time for different countries, with animations representing yearly transitions. 🚀🌐✨

## License 🔒📚⚡

This project is licensed under the MIT License. Feel free to use and modify the code. 😎🔧✨

## Contributions 🛠️⚛️📚

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project. 🎉📊🔍

## Contact 📧🎨👤

For any inquiries, please contact: 🌐📢🎉

- **Your Name**: [asitha.contact.me@gmail.com](mailto:asitha.contact.me@gmail.com)
- **GitHub**: [Asitha Kanchana](https://github.com/Asithakanchana1) 🔎🌈🌍

