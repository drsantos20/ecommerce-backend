from ecommerce.utils import get_model_by_name, url_params_validation


def get_generic_serializer(name):
    model_name = url_params_validation(name)
    product = get_model_by_name('product', model_name)
    serializer_from_model = product.get_serializer()
    return serializer_from_model
