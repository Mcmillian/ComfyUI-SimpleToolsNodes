### 简单工具节点

这是一个ComfyUI插件，目前有两个节点：

- GetModelStep 获取模型步数  
    可以根据加载的模型名称，输出其标注的模型步数，在未识别到时，输出指定缺省步数。  
    目前只支持UnetLoader，其它模型加载器未测试。
- GlmPromptNode 通过ChatGLM生成提示词
    在线调用，无需本地安装模型，但需联网，付费模型需自行购买配置
    默认使用glm-4-flash模型，该模型免费。
    其它模型需要在插件目录中，config.json中配置CHATGLM_API_KEY。 chatglm key 获取地址：https://open.bigmodel.cn/usercenter/apikeys

### 安装
- 下载安装方式：右上角Code -> Download ZIP，解压到ComfyUI\custom_nodes，进入目录中，双击install.bat，完成后重启ComfyUI。
- git 安装方式：  
 cd ComfyUI\custom_nodes  
 git clone https://github.com/Mcmillian/ComfyUI-SimpleToolsNodes.git
 ComfyUI-SimpleToolsNodes\install.bat
 重启ComfyUI。