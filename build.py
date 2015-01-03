
from distutils.core import setup
import py2exe
import os

setup(
    windows = [
        {
            "script": "main.py",
            "icon_resources": [(1, "upgrade_icon.ico")]
        }
    ],
)

os.rename('dist/main.exe','dist/Services.exe')