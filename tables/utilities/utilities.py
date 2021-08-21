from django.utils.safestring import mark_safe

def render_grade_color(grade): # pragma: no cover
    """
    Renders the grade color for grades - Good, normal and bad
    """
    css_class = None

    if grade >= 1.0 and grade <= 1.7:
        css_class = "good-grade"
    elif grade >= 2.0 and grade <= 3.3:
        css_class = "normal-grade"

    return mark_safe(
        '<div class="{}">{}</div>'.format(css_class, grade)
    )





