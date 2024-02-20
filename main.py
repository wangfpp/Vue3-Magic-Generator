import os.path
import re
import shutil
from typing import Any

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from config.config_dev import OPEN_AI_MODEL, OPEN_AI_KEY, MODEL_PLATFORM, MAX_AI_TOKEN, GEMINI_TOKEN, MAX_AI_MODEL
from config.npm_config import HOME_PATH
from llm.gemini import GeminiLLm
from utils.imgsearch import search_img
from llm.maxai import MaxAi
from config.prompt import project, code, project_page, project_design
from utils.npm import init_vue
import webbrowser


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


def generate_page(project_name: str, project_title: str, project_intro: str, style: str):
    '''
    :param project_name: 项目名称
    :param project_title: 页面名称
    :param project_intro: 页面详情
    :param style:
    :return:
    '''
    global pre_code
    project_path = os.path.join(HOME_PATH, "vue", project_name, "src")
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
    {' '.join('<%s/>' % a['moduleEnName'] for a in res[:idx + 1])}
    </template>

    <script lang="ts" setup>
    {' '.join('import %s from "@/components/%s/%s/%s.vue";' % (a['moduleEnName'], project_name, project_title, a['moduleEnName']) for a in res[:idx + 1])}
    </script>
    <style>
    @import url("@/style.css");
    </style>
    '''
        with open(f"{i['moduleEnName']}.vue", 'w', encoding="utf-8") as f:
            f.write(code_str)
        shutil.move(f"{i['moduleEnName']}.vue", comp_path)
        with open(os.path.join(views_path, f"{project_title}.vue"), 'w', encoding="utf-8") as f:
            f.write(app)
        pre_code = code_str
    webbrowser.open(f'http://localhost:5174/{project_name}/{project_title}')


def run(project_intro):
    question = start_run(project_design, {"projectName": project_intro}, JsonOutputParser())
    pages = start_run(project_page, {"userQuestion": question}, JsonOutputParser())
    project_name = pages['projectEnName']
    init_vue(project_name)
    with open(os.path.join(HOME_PATH, "base_vue", "src", "router", "index.js"), "r", encoding="utf-8") as f:
        router_js = f.read().replace(
            '${router}',
            ','.join(["{%s}" % f'''path: '/{project_name}/{router['pageEnName']}',
         name: "{project_name}{router['pageEnName']}",
         component: () => import('@/views/{project_name}/{router['pageEnName']}.vue')
         ''' for router in pages['pages']]))
        with open(os.path.join(HOME_PATH, "vue", project_name, "src", "router", "index.js"), "w",
                  encoding="utf-8") as fw:
            fw.write(router_js)
    for i in pages['pages']:
        while True:
            try:
                generate_page(pages['projectEnName'], i['pageEnName'], i, pages['style'])
                break
            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    run("""
门店管理系统
### 1. 用户权限和角色管理
- 实现多种角色定义（管理员、店长、销售员、配送员等），各角色具有不同的操作权限。
- 提供角色-specific功能访问，如销售员仅能管理商品和查看订单，不能进行退款审核。

### 2. 登录账号
- 安全的登录机制，支持密码和二次验证。
- 忘记密码和密码重置功能。

### 3. 基本信息管理
- 门店基本信息编辑，包括校区选择、店铺描述、门店照片上传。

### 4. 商品管理
- 商品上架管理，包括选择商品、填写原始价格、实际价格，默认库存为0。
- 商品分类与搜索功能，根据品牌、价格、评级等进行筛选。
- 商品库存管理，包括库存预警、库存历史记录。
- 商品批次追踪，以确保追溯性。

### 5. 服务管理
- 服务项目上架，如文档打印、照片打印等，包含服务名称、金额、描述。

### 6. 订单管理
- 订单处理流程，包括接收、回收、退货、指定配送员等。
- 订单状态跟踪和管理。

### 7. 优惠活动管理
- 优惠设置，包括分类优惠、通用优惠、特定商品优惠。
- 优惠券管理，包括金额、有效期、编码。
- 商品价格折扣管理，包括最新价格，折扣说明。

### 8. 用户与会员管理
- 用户基本信息查阅，包括消费统计、用户画像等。
- 会员系统，支持积分累计、兑换等。

### 9. 配送与雇员管理
- 配送员信息录入和管理。
- 雇员信息管理，包括指定权限。

### 10. 财务管理
- 支付记录管理。
- 门店对账，包括日报、周报、月报等。
- 退款审核管理。

### 11. 数据分析与报告
- 销售、库存、用户行为等多维度数据分析。
- 自动生成报告，辅助决策。

### 12. 第三方服务集成
- 支付渠道和物流服务商接口对接。
- 支持主流支付方式和物流跟踪。

### 13. 系统安全性
- 实现数据加密和安全防护措施，防止数据泄露。
- 遵守数据保护法规，保护用户隐私。

### 14. 移动端适配
- 提供移动端应用或响应式网页设计，适配手机和平板操作。

### 15. 消息与反馈
- 消息管理，包括短信、微信、站内消息日志查看。
- 用户和商家反馈通道，以及在线客服功能。

### 1. 界面设计风格

- **简约现代**：简约风格能减少用户的视觉负担，现代感的设计可以使系统看起来更加专业和先进。利用干净的线条和充足的留白，创建出清晰、易用的界面。

- **直观操作**：界面设计应直观易懂，常用功能如商品上架、订单管理等应易于访问，并通过图标或颜色提示进行辅助，减少用户的学习曲线。

### 2. 配色风格

- **温馨舒适**：选用温暖的颜色调如蓝色调、绿色调或暖黄色调，可以创建舒适的浏览和操作体验。这有助于减少使用者的压力，特别是在需要长时间操作系统的情况下。

- **专业统一**：保持颜色的一致性和专业性，选择2-3个主色调，并贯穿整个应用来保持品牌形象的一致性。例如，使用品牌颜色作为按钮、链接或图标的颜色。

### 3. 网页布局

- **导航栏明确**：顶部或侧边的导航栏包含所有主要功能区模块的入口，如商品管理、订单管理、优惠活动等，确保用户能快速跳转至相应部分进行操作。

- **内容优先**：布局应注重内容优先，确保核心操作和信息展示区域明显、易于阅读。例如，在商品管理页面，商品列表应占据主要位置，辅以清晰的添加、编辑按钮。

- **响应式设计**：网页应能自适应不同大小的屏幕，包括桌面、平板和手机。这样可以确保用户在各种设备上都有良好的体验。

- **交互提醒**：在操作如删除商品、退款审核等关键操作处，使用模态对话框确认用户的操作意图，防止误操作。

- **状态提示**：为操作提供即时反馈，如使用加载动画提示等待，操作成功或失败的提示，以及空状态时的引导提示等，增强用户体验。

### 4. 其他重点

- **高级搜索和过滤**：对于商品和订单等数据较多的页面，提供高级搜索和过滤功能，帮助用户快速找到所需信息。

- **数据可视化**：对于财务和数据分析部分，使用图表和统计数据呈现，帮助理解和决策。
""")
