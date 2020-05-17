from rest_framework import serializers

from ecommerce.shipping.models import Shipping


class ShippingSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('shipping', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        super(ShippingSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Shipping
        fields = '__all__'
