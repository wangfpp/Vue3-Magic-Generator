import os.path
import re
import shutil
import time
from typing import Any

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from maxai import MaxAi
from prompt import project, code


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
    llm = MaxAi()
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


# project_intro = '''我想要做一个关于软件、资源、教程、优惠卷分享网站，要求网站风格偏欧美、要有设计感。现在要求你来实现一下软件、资源、教程、优惠卷检索列表页面（在同一页面），用于用户快速定位到自己想要的内容'''
project_intro = '''我想要做一个关于，要求网站风格偏欧美、要有设计感。组件不能重复设计'''


def run():
    t = time.time()
    project_title = f"demo{t}"
    project_path = r"C:\Users\Administrator\WebstormProjects\startproject\src"
    comp_path = os.path.join(project_path, "components", project_title)
    if not os.path.exists(comp_path):
        os.mkdir(comp_path)
    res = start_run(project, {"q1": project_intro}, JsonOutputParser())
    print(f"按照你的需求意见为你分解出如下模块 {[i['moduleName'] for i in res]}")
    for idx, i in enumerate(res):
        code_str = start_run(code, {"modules": res, "moduleName": i['moduleName']}, VueOutputParser())
        print(code_str)
        app = f'''<template>
{' '.join('<Part%s/>' % a for a in range(idx + 1))}
</template>

<script lang="ts" setup>
{' '.join('import Part%s from "./components/%s/Part%s.vue";' % (a, project_title, a) for a in range(idx + 1))}
</script>
<style>
@import url("style.css");
</style>
'''
        with open(f"Part{idx}.vue", 'w', encoding="utf-8") as f:
            f.write(code_str)
        shutil.move(f"Part{idx}.vue", comp_path)
        with open(os.path.join(project_path, f"App{t}.vue"), 'w', encoding="utf-8") as f:
            f.write(app)


if __name__ == "__main__":
    print(run())
