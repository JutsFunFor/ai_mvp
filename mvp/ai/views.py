import warnings

from django.shortcuts import render
from django.views.generic.base import TemplateView

from ai.common.decorators import handle_form_valid
from ai.common.views import CommonMixin, PredictionBaseView
from ai.forms import HeartForm, HivForm, LungForm
from ai.models import MlModel

warnings.filterwarnings("ignore")


class IndexView(CommonMixin, TemplateView):
    template_name = 'ai/index.html'
    title = 'Longevity'
    greetings = "Explore ML Reasearch Capabilities"
    cards = MlModel.objects.all()


class HeartFailureView(PredictionBaseView):
    template_name = 'ai/heart.html'
    form_class = HeartForm
    model_path = 'pkl/heart.pkl'
    scaler_path = 'pkl/heart_scaler.pkl'


class LungCancerView(PredictionBaseView):
    template_name = 'ai/lung.html'
    form_class = LungForm
    model_path = 'pkl/lung.pkl'
    scaler_path = 'pkl/lung_scaler.pkl'


class HivPredView(PredictionBaseView):
    template_name = 'ai/hiv.html'
    form_class = HivForm
    model_path = 'pkl/hiv.pkl'
    scaler_path = 'pkl/hiv_scaler.pkl'
    ohe_features_path = 'pkl/hiv_features.pkl'

    @handle_form_valid(model_path, scaler_path, ohe_features_path)
    def form_valid(self, form, context):
        return render(self.request, self.template_name, context)
