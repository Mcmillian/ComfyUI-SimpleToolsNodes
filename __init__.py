from .GetModelStep import GetModelStep
from .GlmPromptNode import GlmPromptNode
NODE_CLASS_MAPPINGS  = {
    "GetModelStep": GetModelStep,
    "GlmPromptNode": GlmPromptNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "GetModelStep": "get step by unet model name",
    "GlmPromptNode": "glm prompt"
}
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS"
]