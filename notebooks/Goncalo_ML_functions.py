df['popularity_log'] = np.log1p(df['popularity'])
df['runtime_category'] = pd.cut(
    df['runtime'],
    bins=[0, 90, 120, 150, 240],
    labels=['Short', 'Standard', 'Long', 'Very Long']
)df['runtime_squared'] = df['runtime'] ** 2
df['runtime_x_rating'] = df['runtime'] * df['vote_average']
df['rating_category'] = pd.cut(
    df['vote_average'],
    bins=[0, 5, 6.5, 8, 10],
    labels=['Low', 'Average', 'Good', 'Excellent']
)