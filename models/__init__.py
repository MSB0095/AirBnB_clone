#!/usr/bin/python3
"""
__init__ module for models
"""

from models.engine.file_storage import FileStorage

storage: FileStorage = FileStorage()
storage.reload()
