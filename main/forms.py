from django.forms import TextInput, ModelForm
from .models import School


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ["email", "phone", "full_name", "short_name", "region", "district", "inhabited_locality"]

