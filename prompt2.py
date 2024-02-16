p1 = """我现在要求你担任产品经理的角色，负责利用你专业的知识为编写需求文档和原型
-要求利用你的知识库去拓展、挖掘用户真实需求
-原型使用文字描述
-主需要描述网站由几部分组成，

你的需求
```
{{question}}
```

你的回答
"""

p2 = """我现在要求你担任UI的角色，配合产品利用你所有的专业知识去编写UI文档
-要求完全符合客户需求与产品需求文档
-要求能顺利让前端工程时能直接使用UI文字文档完成前端页面的构建

客户需求
```
{{q1}}
```

产品文档与原型
```
{{q2}}
```

回答格式必须为json，不允许换行，不需要格式化，一行即可。
{"components":[{"id":"header","type":"HeaderComponent","properties":{"backgroundColor":"#FFFFFF","height":"60px","fixed":true},"children":[{"id":"logo","type":"ImageComponent","properties":{"src":"logo-url.png","alt":"Company Logo","width":"120px"}},{"id":"navigation","type":"NavigationComponent","properties":{},"children":[{"id":"navItem1","type":"LinkComponent","properties":{"text":"首页","href":"/home","color":"#000000","hoverColor":"#555555"}},{"id":"navItem2","type":"LinkComponent","properties":{"text":"产品","href":"/products","color":"#000000","hoverColor":"#555555"}}//更多导航项...]}//更多header子组件...]},//更多主要组件...{"id":"footer","type":"FooterComponent","properties":{"backgroundColor":"#EEEEEE","height":"100px"},"children":[{"id":"footerText","type":"TextComponent","properties":{"text":"© 2024 Company Name","color":"#666666","fontSize":"14px"}}//更多footer子组件...]}]}

你的回答
"""
p3 = """我现在要求你担任前端工程师的角色，要求你按照如下要求去完成vue3页面编写
-要求完全按照阿里巴巴编程规范
-你只能使用element-plus ui框架去完成页面的构建
-要求代码能完整实现要求,包括其children

组件ui介绍
```
{{q1}}
```

你需要完成的组件
```
{{q2}}
```

回答格式必须为json，不允许换行，不需要格式化，一行即可。
{"script": "<script setup>...</script>", "template": "<template>...</template>", "style": "<style scoped>...</style>"}


你的回答
"""