from django.apps import apps


def get_model_by_name(name):
    return apps.get_model(app_label='product', model_name=name)


def url_params_validation(url) -> str:
    model_name = url.setdefault('type', None)
    if not model_name:
        raise KeyError('type param not present in request')
    return model_name


def get_generic_serializer(name):
    model_name = url_params_validation(name)
    product = get_model_by_name(model_name)
    serializer_from_model = product.get_serializer()
    return serializer_from_model
