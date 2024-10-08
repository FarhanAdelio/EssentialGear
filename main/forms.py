from django.forms import ModelForm
from main.models import GearEntry
from django.utils.html import strip_tags



class GearEntryForm(ModelForm):
    class Meta:
        model = GearEntry
        fields = ["name", "price", "description","stock","rating"]

    def clean_gear(self):
        gear = self.cleaned_data["gear"]
        return strip_tags(gear)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)