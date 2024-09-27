from zhipuai import ZhipuAI
import json
import os

p = os.path.dirname(os.path.realpath(__file__))


def get_api_key():
    try:
        config_path = os.path.join(p, 'config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        api_key = config["CHATGLM_API_KEY"]
    except:
        print("出错啦 Error: API key is required")
        return ""
    return api_key


class GlmPromptNode:

    def __init__(self):
        api_key = get_api_key()
        if api_key is not None:
            self.client = ZhipuAI(api_key=api_key)
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                # 可选列表
                "model": (["glm-4-flash", "glm-4", "glm-4-flashx", "glm-4-plus", "glm-4v-plus", "glm-4-0520",
                                      "glm-4-air", "glm-4-airx"],
                          {"default": "glm-4-flash"}
                          ),
                "max_tokens": ("INT", {"default": 1024, "min": 128, "max": 4096}),
            },
            "optional": {
                "system": ("STRING", {"multiline": True}),
            }
        }

    CATEGORY = "简单节点"
    OUTPUT_NODE = True
    RETURN_NAMES = ("clip-L", "clip-T5")
    RETURN_TYPES = ("STRING", "STRING")
    FUNCTION = "PROCESSOR"

    DESCRIPTION = """
    使用ChatGlm，生成更细致的提示词。
    """

    def PROCESSOR(self, prompt, model, max_tokens, system):
        if not hasattr(self, "client"):
            raise "请先在Config中设置CHATGLM_API_KEY"
        response = self.client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system or """你是Flux绘画模型的提示词构建师，通过精心构建的提示词，帮助用户实现写真级照片提示词。你的能力有:
- 理解用户需求，提炼关键信息；
- 构建详细且准确的提示词；
- 调整提示词以优化出图效果。

结果应给出英文纯文本格式的json，含有以下字段：theme，图片的主题。clip-L，图片的风格描述，如写实照片，素描，高清等等。clip-T5：图片的内容，对人物和周边环境应该详细描述。
json应该为有效的json，纯文本格式，不需要markdown格式"""},
                {"role": "user", "content": prompt}
            ],
        )
        result = response.choices[0].message.content.strip('```').strip('json').strip('\\n').replace('\"', '"')
        print(result)
        result = json.loads(result)
        print(result)
        return (result["clip-L"], result["clip-T5"])
