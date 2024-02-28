import re

from config.npm_config import HOME_PATH


def clicked_vue(project_name, page_name, module_name):
    '''
    激活页面组件
    :param project_name:
    :param page_name:
    :param module_name:
    :return:
    '''
    vue_path = fr"{HOME_PATH}\vue\{project_name}\src\views\{project_name}\{page_name}.vue"
    with open(vue_path, "r") as f:
        vue_html = f.read()
    s = re.search(r"""<div class="active-element-active">\s*(.*?)\s*</div>""", vue_html)
    if s:
        vue_html = vue_html.replace(s.group(0), s.group(1))
    with open(vue_path, "w") as f:
        vue_html = vue_html.replace(f"""<{module_name}/>""", f"""<div class="active-element-active">
        <{module_name}/>
      </div>""")
        f.write(vue_html)


def read_template(template_name):
    '''
    读取组件目标
    :param template_name:
    :return:
    '''
    with open(fr"{HOME_PATH}\template_vue\{template_name}.vue", "r") as f:
        return f.read()


def generate_components(project_name, page_name, modules):
    '''
    将所有页面使用占位符替换
    :param project_name:
    :param page_name:
    :param modules:
    :return:
    '''
    for module in modules:
        component_path = fr"{HOME_PATH}\vue\{project_name}\src\components\{project_name}\{page_name}\{module['moduleEnName']}.vue"
        temp = read_template("skeleton")
        with open(component_path, "w") as f:
            f.write(temp)


def generate_component(project_name, page_name, module):
    '''
    写入组件编写好的代码
    :param project_name:
    :param page_name:
    :param module:
    :return:
    '''
    component_path = fr"{HOME_PATH}\vue\{project_name}\src\components\{project_name}\{page_name}\{module['moduleEnName']}.vue"
    with open(component_path, "w", encoding="utf-8") as f:
        f.write(module['code'])
