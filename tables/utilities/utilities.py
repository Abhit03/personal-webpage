from django.utils.safestring import mark_safe

def render_grade_color(grade): # pragma: no cover
    """
    Renders the grade color for grades - Good, normal and bad
    """
    css_class = None

    if grade >= 1.0 and grade <= 1.7:
        css_class = "good-grade"
    else:
        css_class = "normal-grade"

    return mark_safe(
        '<div class="{}">{}</div>'.format(css_class, grade)
    )



def render_gradealphabet_color(gradealphabet): # pragma: no cover
    """
    Renders the grade color for grade alphabet - Good, normal and bad
    """
    css_class = None

    if gradealphabet == "A" or gradealphabet == "A-":
        css_class = "good-grade"
    else:
        css_class = "normal-grade"

    return mark_safe(
        '<div class="{}">{}</div>'.format(css_class, gradealphabet)
    )



