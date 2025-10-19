from importlib.metadata import version
from pathlib import Path

package_name = Path(__file__).parent.name
__package__ = package_name
__version__ = version(package_name)
