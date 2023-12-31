# common_imports.py
import sys

proton_dir = './../external/proton-python-client'
sys.path.append(proton_dir)

from proton.api import Session, ProtonError