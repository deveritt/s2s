import json
from django.views.generic import FormView
from django.views.generic import TemplateView
from .forms import AddProductForm
from products.models import Product
from django.urls import reverse


class ProductListView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update({
            'products': json.dumps(list(Product.objects.all().values()), indent=4)
        })
        return context


class ProductAddView(FormView):

    template_name = 'add.html'
    form_class = AddProductForm

    def get_success_url(self):

        return reverse('s2s_products')

    def form_valid(self, form):

        try:

            Product.objects.create(
                sku = form.data.get('sku'),
                name = form.data.get('name'),
                attributes = json.loads(form.data.get('attributes'))
            )
            return super(ProductAddView, self).form_valid(form)

        except Exception as e:

            # Log the error and make it user friendly.
            # messages.error(self.request, e) # haven't set this up either
            self.request.messages.add("Unable to convert currency.")
