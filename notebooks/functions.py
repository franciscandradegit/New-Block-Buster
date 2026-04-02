# cleaning the production_companies, production_countries and spoken_languages columns
import ast

def extract_names(x):
    if isinstance(x, str):
        try:
            x = ast.literal_eval(x)
        except:
            return []

    if isinstance(x, list):
        return [d.get('name') for d in x if isinstance(d, dict)]

    return []


# Definig a function to make the values more readable
from matplotlib.ticker import FuncFormatter

def human_format(x, pos=None):
    if x >= 1e9:
        return f'{x*1e-9:.1f}B'
    elif x >= 1e6:
        return f'{x*1e-6:.1f}M'
    elif x >= 1e3:
        return f'{x*1e-3:.1f}K'
    else:
        return f'{x:.0f}'



def format_axes(ax):
    ax.xaxis.set_major_formatter(FuncFormatter(human_format))
    ax.yaxis.set_major_formatter(FuncFormatter(human_format))


