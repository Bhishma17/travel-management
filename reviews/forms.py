# reviews/forms.py
from django import forms
from .models import TouristReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = TouristReview
        fields = ['text', 'rating', 'image']
