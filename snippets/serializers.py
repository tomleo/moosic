from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(required=True, max_length=100)
    code = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOCIES, default='friendly')

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.language = attrs.get('lanuage', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance
        return Snippet(**attrs)
