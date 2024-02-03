from flask import Blueprint

static_blueprint = Blueprint('static', __name__, url_prefix='/static')


@static_blueprint.route('/')
def get_all_static():
    return 'get_all_static'


@static_blueprint.route('/cpu')
def get_cpu_static():
    return 'get_cpu_static'


@static_blueprint.route('/memory')
def get_memory_static():
    return 'get_memory_static'


@static_blueprint.route('/disk')
def get_disk_static():
    return 'get_disk_static'


@static_blueprint.route('/network')
def get_gpu_static():
    return 'get_gpu_static'


