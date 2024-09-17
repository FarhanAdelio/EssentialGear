from django.forms import ModelForm
from main.models import GearEntry

class GearEntryForm(ModelForm):
    class Meta:
        model = GearEntry
        fields = ["name", "price", "description","stock","rating"]