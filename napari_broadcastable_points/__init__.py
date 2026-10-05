try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
__author__ = "Ian Hunt-Isaak"
__email__ = "ianhuntisaak@gmail.com"

from ._points import BroadcastablePoints

__all__ = [
    "BroadcastablePoints",
    "__author__",
    "__email__",
    "__version__",
]
