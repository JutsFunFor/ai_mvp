from django.db import models


class MlModel(models.Model):
    header = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)
    href = models.CharField(max_length=128)
    link = models.CharField(max_length=128)

    def __str__(self):
        return f"Model for {self.header}"


class HeartPred(models.Model):
    age = models.PositiveIntegerField(default=50)
    sex = models.IntegerField(choices=[(0, 'Female'), (1, 'Male')], default=0)
    cp = models.IntegerField(choices=[(0, 'Asymptomatic'), (1, 'Non-Anginal Pain'),
                                      (2, 'Atypical Angina'), (3, 'Typical Angina')], default=0)
    chol = models.PositiveIntegerField(default=150)
    result = models.SmallIntegerField()
    fk = models.ForeignKey(MlModel, on_delete=models.CASCADE, default=1)


class LungPred(models.Model):
    choices = [(0, 'No'), (1, 'Yes')]

    age = models.PositiveIntegerField(default=50)
    wheezing = models.BooleanField(choices=choices, default='No')
    fatigue = models.BooleanField(choices=choices, default='No')
    coughing = models.BooleanField(choices=choices, default='No')
    shortness_of_breath = models.BooleanField(choices=choices, default='No')
    smoking = models.BooleanField(choices=choices, default='No')
    swallowing_difficulty = models.BooleanField(choices=choices, default='No')
    result = models.SmallIntegerField()
    fk = models.ForeignKey(MlModel, on_delete=models.CASCADE, default=2)


class HivPred(models.Model):
    age_choices = [
        ('All', 'All'),
        ('13 - 19', '13 - 19'),
        ('20 - 29', '20 - 29'),
        ('30 - 39', '30 - 39'),
        ('40 - 49', '40 - 49'),
        ('50 - 59', '50 - 59'),
        ('60+', '60+'),

    ]
    gender_choices = [
        ('All', 'All'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ]

    age = models.CharField(choices=age_choices, max_length=10, default='All')
    gender = models.CharField(choices=gender_choices, max_length=11, default='Female')
    hiv_diagnoses = models.PositiveIntegerField(default=10)
    plwdhi = models.FloatField(default=0.7)

    linked_to_care = [(i, i) for i in range(0, 101)]
    linked_to_care = models.PositiveIntegerField(choices=linked_to_care, default=50)
    result = models.FloatField()
    fk = models.ForeignKey(MlModel, on_delete=models.CASCADE, default=3)
