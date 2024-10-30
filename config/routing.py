def get_app_list(self, request, app_label=None):
    from setorder.models import ModelOrder as Models

    app_dict = self._build_app_dict(request)
    model_data = {}
    for app_key in app_dict:
        app = app_dict[app_key]
        for app_model in app["models"]:
            if "model" in app_model:  # Check if 'model' key exists
                model_data[str(app_model["model"]._meta)] = app_model

    new_appdict = {}
    for i in Models.objects.all().select_related("section").order_by("section__order", "order"):
        try:
            if request.user.has_perm(
                    f"{i.title.split('.')[0]}.view_{i.title.split('.')[1]}") or request.user.is_superuser:
                if i.section.title in new_appdict:
                    new_appdict[i.section.title]["models"].append(model_data[i.title])
                else:
                    new_appdict[i.section.title] = dict(app_dict[i.app_label])
                    new_appdict[i.section.title].update({"name": i.section.title, "models": [model_data[i.title]]})
        except KeyError:
            ...
        except IndexError:
            ...
    if request.user.has_perm("setorder.view_modelorder") or request.user.is_superuser:
        new_appdict["setset"] = app_dict["setorder"]

    app_list = list(new_appdict.values())
    return app_list
