import importlib.metadata

_real_version = importlib.metadata.version

def _patched_version(package_name):
    if package_name == "shapely":
        return "2.1.2"  # ou a versão que você tem instalada
    return _real_version(package_name)

importlib.metadata.version = _patched_version
