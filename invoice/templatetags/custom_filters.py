from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiplies the value by the argument."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None  # Or some fallback value if needed


@register.filter
def total_invoice_amount(items):
    total = 0
    for item in items:
        total += item.quantity * item.price
    return total
