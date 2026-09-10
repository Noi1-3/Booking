from django import forms


class BootstrapFormMixin:
    """
    Універсальний міксін для автоматичного стилізування
    форм під Bootstrap та додавання плейсхолдерів у
    всі додатки проєкту.
    """

    placeholders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, forms.Select):
                css_class = 'form-select'
            elif isinstance(widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            else:
                css_class = 'form-control'

            current_classes = widget.attrs.get('class', '')
            if css_class not in current_classes:
                widget.attrs['class'] = f"{current_classes} {css_class}".strip()

            placeholder_text = self.placeholders.get(field_name) or field.label
            if placeholder_text and 'placeholder' not in widget.attrs:
                widget.attrs['placeholder'] = str(placeholder_text)