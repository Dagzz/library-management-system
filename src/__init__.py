"""
Main package for the application.

This module serves as the root of the application, containing all the sub-packages and modules 
that make up the library management system. Each sub-folder within `src` represents a key 
layer or component of the application.
"""

# Core components (config and models)
from .core import (
    config,
    models,
)

# Infrastructure layer (database connection and repositories)
from .infra import (
    database,
    repositories,
)

# Interfaces layer (controllers and views)
from .interfaces import (
    controllers,
    views,
)

# Business logic (services)
from .logic import (
    services,
)

__all__ = [
    "config",
    "models",
    "database",
    "repositories",
    "controllers",
    "views",
    "services",
    "fonts",
    "images",
    "styles",
]
