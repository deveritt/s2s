from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms
from django.forms import Form


class AddProductForm(Form):
    """
    We should add a clean here to give proper errors.
    """

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_class = 'no-asterisk'
        self.helper.form_tag = True
        self.helper.form_method = 'POST'
        self.helper.form_action = ''

        super(AddProductForm, self).__init__(*args, **kwargs)

        sku = forms.CharField(
            label="SKU"
        )

        name = forms.CharField(
            label="Name",
        )

        attributes = forms.JSONField(
            label="Attributes",
        )

        self.fields['sku'] = sku
        self.fields['name'] = name
        self.fields['attributes'] = attributes

        self.helper.layout = Layout(
            'sku',
            'name',
            'attributes',
            HTML("""<br><button type="submit" class="btn btn-primary">Add Product</button>""")
        )
