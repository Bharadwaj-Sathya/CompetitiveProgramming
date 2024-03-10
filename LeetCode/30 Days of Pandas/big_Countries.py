import pandas as pd

# Create DataFrame with the provided data
data = {
    'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
    'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
    'area': [652230, 28748, 2381741, 468, 1246700],
    'population': [25500100, 2831741, 37100000, 78115, 20609294],
    'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
}

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[
        (world['area'] >= 3_000_000) | \
        (world['population'] >= 25_000_000)
    ][['name', 'population', 'area']]

# Filter big countries
world_df = big_countries(pd.DataFrame(data))



# Print the output
print(world_df)