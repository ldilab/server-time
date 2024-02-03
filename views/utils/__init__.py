from models.dynamic import DynamicCPUModel, DynamicMemModel, DynamicDiskModel, DynamicGPUModel, DynamicImageModel, \
    DynamicContainerModel
from models.static import StaticCPUModel, StaticMemModel, StaticDiskModel, StaticGPUModel


def get_model_of_from(dtype: str, _of: str, _from: str):
    if dtype not in ["static", "dynamic"]:
        raise ValueError("dtype must be 'static' or 'dynamic'")
    target_model = None
    static_models = {
        'cpu': StaticCPUModel,
        'memory': StaticMemModel,
        'disk': StaticDiskModel,
        'gpu': StaticGPUModel,
    }
    dynamic_models = {
        'cpu': DynamicCPUModel,
        'memory': DynamicMemModel,
        'disk': DynamicDiskModel,
        'gpu': DynamicGPUModel,
        'image': DynamicImageModel,
        'container': DynamicContainerModel,
    }

    if dtype == 'static':
        if _of in ["image", "container"]:
            raise ValueError("'image' and 'container' are not supported in static. Use 'dynamic' instead.")
        target_model = static_models.get(_of)
    elif dtype == 'dynamic':
        target_model = dynamic_models.get(_of)
    target_model = target_model if _from == 'all' else target_model.query.filter_by(servername=_from)
    return target_model
