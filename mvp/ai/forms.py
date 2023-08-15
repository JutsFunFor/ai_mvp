from django import forms

from ai.models import HeartPred, HivPred, LungPred


class HeartForm(forms.ModelForm):
    class Meta:
        model = HeartPred
        fields = ('age', 'sex', 'cp', 'chol')


class LungForm(forms.ModelForm):
    class Meta:
        model = LungPred
        fields = ('age', 'wheezing', 'fatigue', 'coughing', 'shortness_of_breath',
                  'smoking', 'swallowing_difficulty')


class HivForm(forms.ModelForm):
    class Meta:
        model = HivPred
        fields = ('age', 'gender', 'hiv_diagnoses', 'plwdhi', 'linked_to_care')
