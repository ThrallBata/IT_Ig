class DataMixin:
    # paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.annotate(Count('product'))
        return context