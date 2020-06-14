from rest_framework import serializers

from ecommerce.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('order', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        super(OrderSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Order
        fields = '__all__'
