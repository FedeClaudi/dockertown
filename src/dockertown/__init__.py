__version__ = "0.2.4"

from .client_config import ClientNotFoundError
from .components.buildx.cli_wrapper import Builder
from .components.config.cli_wrapper import Config
from .components.container.cli_wrapper import Container, ContainerStats
from .components.context.cli_wrapper import (
    Context,
    DockerContextConfig,
    KubernetesContextConfig,
)
from .components.image.cli_wrapper import Image
from .components.network.cli_wrapper import Network
from .components.node.cli_wrapper import Node
from .components.plugin.cli_wrapper import Plugin
from .components.secret.cli_wrapper import Secret
from .components.service.cli_wrapper import Service
from .components.stack.cli_wrapper import Stack
from .components.system.cli_wrapper import SystemInfo
from .components.task.cli_wrapper import Task
from .components.volume.cli_wrapper import Volume
from .docker_client import DockerClient
from .exceptions import DockerException

# alias
docker = DockerClient()

__all__ = [
    "Builder",
    "ClientNotFoundError",
    "Config",
    "Container",
    "ContainerStats",
    "Context",
    "DockerContextConfig",
    "DockerException",
    "Image",
    "KubernetesContextConfig",
    "Network",
    "Node",
    "Plugin",
    "Secret",
    "Service",
    "Stack",
    "SystemInfo",
    "Task",
    "Volume",
    "DockerClient"
]
