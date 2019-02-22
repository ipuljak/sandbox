import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_currency(value):
    """Format the value to a readable currency format i.e. 500000 -> $500,000.00"""

    return locale.currency(value, grouping=True)
