import importlib
from importlib.metadata import (
    version as __version,
)
import sys as _sys
from types import (
    ModuleType,
)
from typing import (
    List,
)

_sys.setrecursionlimit(max(100000, _sys.getrecursionlimit()))

# __version__ = __version("pyecc")

_lazy_imports = {
    "bls": "pyecc.bls",
    "bls12_381": "pyecc.bls12_381",
    "bn128": "pyecc.bn128",
    "optimized_bls12_381": "pyecc.optimized_bls12_381",
    "optimized_bn128": "pyecc.optimized_bn128",
    "secp256k1": "pyecc.secp256k1",
}


def _import_module(name: str) -> ModuleType:
    module = importlib.import_module(_lazy_imports[name])
    globals()[name] = module
    return module


def __getattr__(name: str) -> ModuleType:
    if name in _lazy_imports:
        return _import_module(name)
    raise AttributeError(f"module 'pyecc' has no attribute '{name}'")


def __dir__() -> list[str]:
    return list(_lazy_imports.keys()) + list(globals().keys())
