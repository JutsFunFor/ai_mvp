from functools import wraps

import joblib
import pandas as pd
from django.shortcuts import render


def handle_form_valid(model_path, scaler_path, ohe_features_path):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            form = args[0]
            try:
                model = joblib.load(model_path)
                ohe_features = joblib.load(ohe_features_path)

                X_test = pd.DataFrame(form.cleaned_data, index=[0])
                X_test.columns = [f'Age_{X_test["age"][0]}', f'Gender_{X_test["gender"][0]}',
                                  'Hiv_diagnoses', 'Plwdhi', 'Linked_to_care']
                X_test = X_test.reindex(columns=ohe_features, fill_value=False)
                X_test = X_test.applymap(lambda x: isinstance(x, str) or x)

                result = model.predict(X_test)[0]

                form.instance.result = result
                form.save()

            except Exception as err:
                context = {'error_message': err}
                return render(request, 'ai/error.html', context)

            context = {"form": form, "result": f'{result:.2f}'}
            return view_func(request, *args, context, **kwargs)

        return wrapped_view

    return decorator
