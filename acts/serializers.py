
from rest_framework import serializers

from acts.models import Akt
from main.models import Invent
from datetime import datetime


class ActSerializer(serializers.ModelSerializer):

    class Meta:
        model = Akt
        fields = ('recipient', 'address', 'fio', 'position', 'inventory', )


    def validate_inventory(self, inventory):
        for i in inventory.split(','):
            try:
                Invent.objects.get(invent_number=i)
                a = Invent.objects.get(invent_number=i)
                if a.act_number:
                    raise serializers.ValidationError('Error')
            except:
                raise serializers.ValidationError('Инвентарь не найден')

        return inventory

    def validate_recipient(self, recipient):
        request = self.context.get('request')
        if recipient == request.user:
            raise serializers.ValidationError('Нельзя отправлять себе')
        return recipient


    def create(self, validated_data):
        request = self.context.get('request')
        sender = request.user
        validated_data['sender'] = sender

        act = Akt.objects.create(**validated_data)
        for i in act.inventory.split(','):
            inv = Invent.objects.get(invent_number=i)
            inv.act_number = act.id
            inv.save()
        act.created_at = datetime.now()
        act.save()
        return act



    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sender'] = str(instance.sender)
        return representation