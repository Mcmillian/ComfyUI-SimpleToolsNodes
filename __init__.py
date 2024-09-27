from .GetModelStep import GetModelStep
from .GlmPromptNode import GlmPromptNode
NODE_CLASS_MAPPINGS  = {
    "GetModelStep": GetModelStep,
    "GlmPromptNode": GlmPromptNode
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "GetModelStep": "获取Unet模型步数",
    "GlmPromptNode": "GLM提示词"
}
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS"
]