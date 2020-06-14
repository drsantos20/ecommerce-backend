from django.apps import apps


def get_model_by_name(app_label, name):
    return apps.get_model(app_label=app_label, model_name=name)


def url_params_validation(url) -> str:
    model_name = url.setdefault('type', None)
    if not model_name:
        raise KeyError('type param not present in request')
    return model_name
