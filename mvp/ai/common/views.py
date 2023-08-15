import joblib
import numpy as np
from django.shortcuts import render
from django.views.generic.edit import FormView


class CommonMixin:
    title, greetings, cards, result = None, None, None, None

    def get_context_data(self, **kwargs):
        context = super(CommonMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['greetings'] = self.greetings
        context['cards'] = self.cards
        context['result'] = self.result
        return context


class PredictionBaseView(CommonMixin, FormView):
    template_name, form_class, model_path, scaler_path = None, None, None, None
    result = ' Click "Predict" Button'

    def form_valid(self, form):
        try:
            model = joblib.load(self.model_path)
            scaler = joblib.load(self.scaler_path)
            X_test = np.array(list(form.cleaned_data.values())).reshape(1, -1)
            X_test = scaler.transform(X_test)
            result = model.predict(X_test)[0]

            form.instance.result = result
            form.save()

        except Exception as err:
            context = {'error_message': err}
            return render(self.request, 'ai/error.html', context)

        context = {"form": form, "result": result}
        return render(self.request, self.template_name, context)
