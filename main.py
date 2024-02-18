import os.path
import re
import shutil
import time
from typing import Any

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from config.config_dev import OPEN_AI_MODEL, OPEN_AI_KEY, MODEL_PLATFORM, MAX_AI_TOKEN, GEMINI_TOKEN, MAX_AI_MODEL
from llm.gemini import GeminiLLm
from utils.imgsearch import search_img
from llm.maxai import MaxAi
from config.prompt import project, code, project_style, project_page, project_design


class VueOutputParser(StrOutputParser):
    def parse(self, text: str) -> Any:
        text = text.strip()
        match = re.search(r"```(vue)?(.*)(```)", text, re.DOTALL)
        # If no match found, assume the entire string is a JSON string
        if match is None:
            text = text
        else:
            # If match found, use the content within the backticks
            text = match.group(2)
        text = text.strip()
        return text

    @property
    def _type(self) -> str:
        return "vue_output_parser"


def start_run(prompt_str, params, output_parser=StrOutputParser()):
    llm = None
    if MODEL_PLATFORM == 'maxai':
        llm = MaxAi(api_key=MAX_AI_TOKEN, model=MAX_AI_MODEL)
    if MODEL_PLATFORM == 'gemini':
        llm = GeminiLLm(api_key=GEMINI_TOKEN)
    if MODEL_PLATFORM == 'openai':
        llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY, model=OPEN_AI_MODEL,
                         temperature=0.1, verbose=True)
    if llm is None:
        # 抛异常
        raise RuntimeError("未配置模型平台")
    prompt = ChatPromptTemplate.from_template(prompt_str, template_format="jinja2")
    while True:
        try:
            chain = prompt | llm | output_parser
            res = chain.invoke(params)
            if res is not None:
                return res
        except Exception as e:
            print(e)
            pass


'''
专业或企业风格：这类网站通常具有简约、清晰的设计，注重信息传达的效率和清晰度。色彩方案倾向于保守，使用空间、图标和字体来传达专业形象。

创意或艺术风格：这种风格的网站常常使用大胆的色彩、独特的布局和创新的交互设计。它们旨在展示设计者的创造力，适合艺术家、设计师和创新型企业。

简约风格：简约设计以最少的元素完成最大的表达。它避免使用过多的颜色、形状、纹理，追求“少即是多”的理念。

复古或怀旧风格：这些网站通过使用旧式字体、配色和图像，营造出一种回顾过去的感觉。适用于展示历史、传统或复古产品的品牌。

现代或前卫风格：采用最新的设计趋势，如扁平设计、大背景图片、视频以及过渡效果等。这类网站看起来时尚、新颖，适合科技公司或创新型企业。

互动性风格：这种风格的网站包含很多可以与用户互动的元素，如动画、滚动视差、游戏化元素等，为用户提供有趣的在线体验。

个人或博客风格：这类网站通常较为简约，集中在内容上，为个人提供一个展示思想、分享经验的平台。

电子商务风格：专为在线购物设计，强调产品展示、简化购买流程，并提供明确的行动呼吁（CTA）按钮。
'''

# project_intro = '''我想要做一个关于软件、资源、教程、优惠卷分享网站，要求网站风格偏欧美、要有设计感。现在要求你来实现一下软件、资源、教程、优惠卷检索列表页面（在同一页面），用于用户快速定位到自己想要的内容'''
pre_code = ""


def generate_page(project_name, project_title, project_intro, style):
    global pre_code
    project_path = r"C:\Users\Administrator\WebstormProjects\startproject\src"
    comp_path = os.path.join(project_path, "components", project_name, project_title)
    views_path = os.path.join(project_path, "views", project_name)
    if not os.path.exists(comp_path):
        os.makedirs(comp_path)
    if not os.path.exists(views_path):
        os.makedirs(views_path)
    project_intro = f'''我想要做一个{project_intro}。风格如下
        {style}
        '''
    res = start_run(project, {"q1": project_intro}, JsonOutputParser())
    print(f"按照你的需求意见为你分解出如下模块 {[i['moduleName'] for i in res]}")

    for idx, i in enumerate(res):
        img_style = i.get('imgStyle')
        img_src = []
        if img_style is not None:
            img_src = search_img(img_style)
            img_src = img_src[:min(len(img_src), 10)]
        code_str = start_run(code,
                             {"modules": res, "moduleName": i['moduleName'], 'imgSrc': img_src, "preCode": pre_code},
                             VueOutputParser())
        print(code_str)
        app = f'''<template>
    {' '.join('<%s/>' % a['moduleEnName'] for a in res[:idx+1])}
    </template>

    <script lang="ts" setup>
    {' '.join('import %s from "../../components/%s/%s/%s.vue";' % (a['moduleEnName'], project_name, project_title, a['moduleEnName']) for a in res[:idx+1])}
    </script>
    <style>
    @import url("../../style.css");
    </style>
    '''
        with open(f"{i['moduleEnName']}.vue", 'w', encoding="utf-8") as f:
            f.write(code_str)
        shutil.move(f"{i['moduleEnName']}.vue", comp_path)
        with open(os.path.join(views_path, f"{project_title}.vue"), 'w', encoding="utf-8") as f:
            f.write(app)
        pre_code = code_str


def run():
    project_intro = "极具个人风格的博客，(复古或怀旧风格：这些网站通过使用旧式字体、配色和图像，营造出一种回顾过去的感觉。适用于展示历史、传统或复古产品的品牌。)"
    question = start_run(project_design, {"projectName": project_intro}, JsonOutputParser())
    pages = start_run(project_page, {"userQuestion": question}, JsonOutputParser())
    for i in pages['pages']:
        while True:
            try:
                generate_page(pages['projectEnName'], i['pageEnName'], i, pages['style'])
                break
            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    run()
