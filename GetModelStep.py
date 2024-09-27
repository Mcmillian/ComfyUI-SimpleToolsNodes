import re


class GetModelStep:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "step": ("INT", {"default": 20, "min": 1, "max": 99})
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO",
                "prompt": "PROMPT",
                "unique_id": "UNIQUE_ID",
            },
        }

    CATEGORY = "简单节点"
    OUTPUT_NODE = True
    RETURN_NAMES = ("模型名称", "步数")
    RETURN_TYPES = ("STRING", "INT")
    FUNCTION = "parse"
    DESCRIPTION = "根据模型名称来获取步数，无法识别时，使用缺省的step值"

    def parse(self, model, step, prompt, extra_pnginfo, unique_id):
        workflow = extra_pnginfo["workflow"]
        node_id = None  # Initialize node_id to handle cases where no match is found
        link_id = None
        link_to_node_map = {}

        for node in workflow["nodes"]:
            if node["type"] == "GetModelStep" and node["id"] == int(unique_id) and not link_id:
                for node_input in node["inputs"]:
                    if node_input["name"] == "model":
                        link_id = node_input["link"]

            node_outputs = node.get("outputs", None)
            if not node_outputs:
                continue
            for output in node_outputs:
                node_links = output.get("links", None)
                if not node_links:
                    continue
                for link in node_links:
                    link_to_node_map[link] = node["id"]
                    if link_id and link == link_id:
                        break

        if link_id:
            node_id = link_to_node_map.get(link_id, None)

        if node_id is None:
            raise ValueError("No matching node found for the given title or id")

        values = prompt[str(node_id)]
        name = ""
        if "inputs" in values:
            if "unet_name" in values["inputs"]:
                name = str(values["inputs"]["unet_name"])  # Convert to string here
            else:
                raise NameError(f"Widget not found: {node_id}.unet_name")

        # 正则获取 整数step的数字
        pattern = r'(\d+)(steps?|步)'
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            step = int(match.group(1))
        else:
            print("模型名不包含步数信息，使用默认步数：" + str(step))
        return (name, step,)
