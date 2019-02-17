import locale

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

def pretty_print_currency(value):
    """Pretty print monetary value. i.e. 500000 -> $500,000.00"""

    return locale.currency(value, grouping=True)