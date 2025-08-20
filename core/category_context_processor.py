from todo.models import Category


def global_category(request):
    global_categories=Category.objects.filter(is_active=True).order_by('title')
    return {'global_categories': global_categories}
    