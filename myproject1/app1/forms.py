from django import forms

CROP_CHOICES = [
    ('rice', 'Rice'),
    ('maize', 'Maize'),
    ('jute', 'Jute'),
    ('cotton', 'Cotton'),
    ('coconut', 'Coconut'),
    ('papaya', 'Papaya'),
    ('orange', 'Orange'),
    ('apple', 'Apple'),
    ('muskmelon', 'Muskmelon'),
    ('watermelon', 'Watermelon'),
    ('grapes', 'Grapes'),
    ('mango', 'Mango'),
    ('banana', 'Banana'),
    ('pomegranate', 'Pomegranate'),
    ('lentil', 'Lentil'),
    ('blackgram', 'Blackgram'),
    ('mungbean', 'Mungbean'),
    ('mothbeans', 'Mothbeans'),
    ('pigeonpeas', 'Pigeonpeas'),
    ('kidneybeans', 'Kidneybeans'),
    ('chickpea', 'Chickpea'),
    ('coffee', 'Coffee')
]

class CropForm(forms.Form):
    crops = forms.ChoiceField(choices=CROP_CHOICES, label='Select a crop')
from django import forms

class ConditionForm(forms.Form):
    conditions = ['N', 'P', 'K', 'temperature','ph','humidity','rainfall']
    condition = forms.ChoiceField(choices=conditions)