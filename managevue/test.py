import time

from flask import Flask, request, jsonify
from flask_cors import CORS

from managevue.changevue import clicked_vue, generate_components, generate_component

app = Flask(__name__)
CORS(app)


@app.route('/check_vue', methods=['POST'])
def check_vue():
    data = request.json
    project_name = data['project_name']
    page_name = data['page_name']
    module_name = data['module_name']
    clicked_vue(project_name, page_name, module_name)
    return jsonify({'success': True})


modules_info = [
    {
        "moduleName": "导航栏",
        "moduleEnName": "NavigationBar",
        "designConcept": "结合复古怀旧风格与现代设计元素，提供清晰的页面导航，方便用户快速找到所需内容。",
        "function": "提供网站内各主要页面的链接，包括首页、图片集推荐、艺人介绍等，并支持用户登录/注册功能的入口。",
        "layoutStyle": "采用经典字体和复古色调，如褐色、灰色、淡黄色等，以简洁的布局展现，确保用户界面友好且易于导航。",
        "imgStyle": "",
        "code": """<template>
      <nav class="navigation-bar">
        <div class="logo">
          <img src="@/assets/logo.png" alt="Logo" class="logo-image">
        </div>
        <ul class="nav-links">
          <li><a href="/ImageCollectionPlatform/HomePage">首页</a></li>
          <li><a href="/ImageCollectionPlatform/SearchResultsPage">图片集推荐</a></li>
          <li><a href="/ImageCollectionPlatform/ArtistMaintenancePage">艺人介绍</a></li>
          <li><a href="/ImageCollectionPlatform/UploadPage">发布图片集</a></li>
        </ul>
        <div class="user-actions">
          <el-button type="text" @click="handleLogin">登录</el-button>
          <el-button type="text" @click="handleRegister">注册</el-button>
        </div>
      </nav>
    </template>

    <script setup>
    import { ElButton } from 'element-plus';
    import {useRouter} from "vue-router";
    const router = useRouter()
    const handleLogin = () => {
      router.push({path: "/ImageCollectionPlatform/UserLoginPage"})
      console.log('Login modal should appear');
    };

    const handleRegister = () => {
      router.push({path: "/ImageCollectionPlatform/UserRegistrationPage"})
      console.log('Register modal should appear');
    };
    </script>

    <style scoped>
    .navigation-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #f0ebe3;
      padding: 10px 50px;
      font-family: 'Times New Roman', Times, serif;
    }

    .logo {
      flex: 1;
    }

    .logo-image {
      height: 50px;
    }

    .nav-links {
      flex: 2;
      list-style: none;
      display: flex;
      justify-content: center;
    }

    .nav-links li {
      margin: 0 15px;
    }

    .nav-links a {
      text-decoration: none;
      color: #5c3a21;
      font-size: 16px;
    }

    .user-actions {
      flex: 1;
      display: flex;
      justify-content: flex-end;
    }

    .el-button {
      color: #5c3a21;
      border-color: #5c3a21;
    }

    .el-button:hover {
      color: #3e2714;
      border-color: #3e2714;
    }
    </style>"""
    },
    {
        "moduleName": "图片集推荐模块",
        "moduleEnName": "ImageCollectionRecommendation",
        "designConcept": "通过展示精选的图片集来吸引用户的注意力，利用复古怀旧的设计风格结合现代元素，创造独特的视觉体验。",
        "function": "展示平台精选的图片集，提供图片集的预览图和简短描述，用户可以点击进入查看详细内容。",
        "layoutStyle": "使用复古色调的背景和旧式图标，以网格形式展示图片集，每个图片集项提供醒目的标题和简介。",
        "imgStyle": "",
        "code": """<template>
      <section class="image-collection-recommendation">
        <div class="title">
          <h2>图片集推荐</h2>
        </div>
        <div class="image-collection-container">
          <div class="image-collection-item" v-for="(image, index) in images" :key="index" @click="linkTo(image)">
            <el-image :src="image.images?image.images[0].url:''" fit="cover" class="image-collection-img"></el-image>
            <div class="image-collection-info">
              <h3>{{ image.title }}</h3>
              <p>{{ image.description }}</p>
            </div>
          </div>
        </div>
      </section>
    </template>

    <script setup>
    import {inject, ref} from 'vue';
    import {useRouter} from "vue-router";
    const router = useRouter()
    const axios = inject('$axios')
    const linkTo = function (e) {
      router.push({path: "/ImageCollectionPlatform/CollectionDetailsPage", query:{id: e.id}})
    }
    const images = ref([

    ]);

    axios.post(`/common/image_collection/page`, {page: 1, is_top: 1, orderby: [{"column": "is_top", "sort": 'desc'}]}).then(res => {
        images.value = res.data.items
      })


    </script>

    <style scoped>
    .image-collection-recommendation {
      background-color: #f0ebe3;
      padding: 20px;
      font-family: 'Times New Roman', Times, serif;
    }

    .title h2 {
      color: #5c3a21;
      text-align: center;
    }

    .image-collection-container {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 20px;
    }

    .image-collection-item {
      cursor: pointer;
      width: 30%;
      margin-bottom: 20px;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      transition: 0.3s;
    }

    .image-collection-item:hover {
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .image-collection-img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .image-collection-info {
      padding: 10px;
      text-align: center;
    }

    .image-collection-info h3 {
      color: #5c3a21;
      margin: 10px 0;
    }

    .image-collection-info p {
      color: #5c3a21;
      font-size: 14px;
    }
    </style>"""
    },
    {
        "moduleName": "最新图片集展示",
        "moduleEnName": "LatestImageCollectionDisplay",
        "designConcept": "展示平台最新上传的图片集，让用户能够快速获取最新内容。",
        "function": "以时间顺序展示最新的图片集，包括图片集的封面、标题和上传时间。",
        "layoutStyle": "采用简洁的布局和复古风格的设计元素，强调新鲜感和时效性。",
        "imgStyle": "",
        "code": """<template>
      <section class="latest-image-collection-display">
        <div class="title">
          <h2>最新图片集展示</h2>
        </div>
        <div class="latest-image-collection-container">
          <div class="latest-image-collection-item" v-for="(image, index) in latestImages" :key="index" @click="linkTo(image)">
            <el-image :src="image.images?image.images[0].url:''" fit="cover" class="latest-image-collection-img"></el-image>
            <div class="latest-image-collection-info">
              <h3>{{ image.title }}</h3>
              <p>{{ image.created_at }}</p>
            </div>
          </div>
        </div>
      </section>
    </template>

    <script setup>
    import {inject, ref} from 'vue';
    import {useRouter} from "vue-router";
    const router = useRouter()
    const axios = inject('$axios')

    const latestImages = ref([

    ]);

    const linkTo = function (e) {
      router.push({path: "/ImageCollectionPlatform/CollectionDetailsPage", query:{id: e.id}})
    }
    const images = ref([

    ]);

    axios.post(`/common/image_collection/page`, {page: 1, orderby: [{"column": "id", "sort": 'desc'}]}).then(res => {
        latestImages.value = res.data.items
      })

    </script>



    <style scoped>
    .latest-image-collection-display {
      background-color: #f0ebe3;
      padding: 20px;
      font-family: 'Times New Roman', Times, serif;
    }

    .title h2 {
      color: #5c3a21;
      text-align: center;
    }

    .latest-image-collection-container {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 20px;
    }

    .latest-image-collection-item {
      cursor: pointer;
      width: 30%;
      margin-bottom: 20px;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      transition: 0.3s;
    }

    .latest-image-collection-item:hover {
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .latest-image-collection-img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .latest-image-collection-info {
      padding: 10px;
      text-align: center;
    }

    .latest-image-collection-info h3 {
      color: #5c3a21;
      margin: 10px 0;
    }

    .latest-image-collection-info p {
      color: #5c3a21;
      font-size: 14px;
    }
    </style>"""
    },
    {
        "moduleName": "艺人介绍",
        "moduleEnName": "ArtistIntroduction",
        "designConcept": "介绍合作艺人或热门艺人，增加平台内容的丰富性和艺术性。",
        "function": "展示艺人的照片、简介和代表作品，提供链接到艺人专属页面的入口。",
        "layoutStyle": "使用复古风格的设计元素，如经典字体和复古色调，以卡片形式展示每位艺人。",
        "imgStyle": "",
        "code": """<template>
      <section class="artist-introduction">
        <div class="title">
          <h2>艺人介绍</h2>
        </div>
        <div class="artist-container">
          <div class="artist-item" v-for="(artist, index) in artists" :key="index" @click="linkTo">
            <el-image :src="artist.artists_url" fit="cover" class="artist-photo"></el-image>
            <div class="artist-info">
              <h3>{{ artist.name }}</h3>
              <p>{{ artist.bio }}</p>
              <el-button type="text">查看更多</el-button>
            </div>
          </div>
        </div>
      </section>
    </template>

    <script setup>
    import {inject, ref} from 'vue';
    import {useRouter} from "vue-router";
    const router = useRouter()
    const linkTo = function () {
      router.push({path: "/ImageCollectionPlatform/ArtistMaintenancePage"})
    }

    const artists = ref([
    ]);


    const axios = inject('$axios')

    axios.post(`/common/artist/page`, {orderby: [{"column": "id", "sort": 'desc'}]}).then(res => {
      artists.value = res.data.items
    })
    </script>

    <style scoped>
    .artist-introduction {
      background-color: #f0ebe3;
      padding: 20px;
      font-family: 'Times New Roman', Times, serif;
    }

    .title h2 {
      color: #5c3a21;
      text-align: center;
    }

    .artist-container {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      margin-top: 20px;
    }

    .artist-item {
      cursor: pointer;
      width: 30%;
      margin-bottom: 20px;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      transition: 0.3s;
    }

    .artist-item:hover {
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .artist-photo {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .artist-info {
      padding: 10px;
      text-align: center;
    }

    .artist-info h3 {
      color: #5c3a21;
      margin: 10px 0;
    }

    .artist-info p {
      color: #5c3a21;
      font-size: 14px;
    }

    .el-button {
      color: #5c3a21;
      border-color: #5c3a21;
    }
    </style>"""
    },
    {
        "moduleName": "用户登录/注册入口",
        "moduleEnName": "UserLoginRegistration",
        "designConcept": "提供用户登录和注册的入口，方便新用户注册和老用户登录。",
        "function": "在导航栏或页面显眼位置提供登录/注册按钮，点击后弹出登录/注册表单。",
        "layoutStyle": "采用简洁明了的设计，结合复古怀旧风格的按钮和表单设计元素。",
        "imgStyle": "",
        "code": """<template>
      <section class="user-login-registration">
        <div class="login-registration-container">
          <el-button @click="showLoginDialog = true" type="text">登录</el-button>
          <el-dialog title="登录" v-model="showLoginDialog" @close="clearLoginForm">
            <el-form :model="loginForm">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="showLoginDialog = false">取消</el-button>
              <el-button type="primary" @click="login">登录</el-button>
            </div>
          </el-dialog>

          <el-button @click="showRegistrationDialog = true" type="text">注册</el-button>
          <el-dialog title="注册" v-model="showRegistrationDialog" @close="clearRegistrationForm">
            <el-form :model="registrationForm">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="registrationForm.username" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="邮箱" prop="email">
                <el-input v-model="registrationForm.email" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="registrationForm.password" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="确认密码" prop="confirmPassword">
                <el-input type="password" v-model="registrationForm.confirmPassword" autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="showRegistrationDialog = false">取消</el-button>
              <el-button type="primary" @click="register">注册</el-button>
            </div>
          </el-dialog>
        </div>
      </section>
    </template>

    <script setup>
    import { ref } from 'vue';

    const showLoginDialog = ref(false);
    const showRegistrationDialog = ref(false);
    const loginForm = ref({ username: '', password: '' });
    const registrationForm = ref({ username: '', email: '', password: '', confirmPassword: '' });

    const clearLoginForm = () => {
      loginForm.value.username = '';
      loginForm.value.password = '';
    };

    const clearRegistrationForm = () => {
      registrationForm.value.username = '';
      registrationForm.value.email = '';
      registrationForm.value.password = '';
      registrationForm.value.confirmPassword = '';
    };

    const login = () => {
      // 实现登录逻辑
      console.log('登录信息', loginForm.value);
      showLoginDialog.value = false;
      clearLoginForm();
    };

    const register = () => {
      // 实现注册逻辑
      console.log('注册信息', registrationForm.value);
      showRegistrationDialog.value = false;
      clearRegistrationForm();
    };
    </script>

    <style scoped>
    .user-login-registration {
      text-align: center;
      margin-top: 20px;
    }

    .login-registration-container {
      display: inline-block;
    }

    .el-button {
      margin: 0 10px;
      color: #5c3a21;
      border-color: #5c3a21;
    }

    .dialog-footer {
      text-align: right;
    }
    </style>"""
    },
    {
        "moduleName": "搜索栏",
        "moduleEnName": "SearchBar",
        "designConcept": "允许用户快速找到他们感兴趣的图片集或艺人。",
        "function": "提供一个搜索框，用户可以输入关键词进行搜索。",
        "layoutStyle": "采用复古怀旧风格的设计，简洁的搜索框配以经典字体和色调。",
        "imgStyle": "",
        "code": """<template>
      <section class="search-bar">
        <div class="search-container">
          <el-input
            v-model="searchQuery"
            placeholder="搜索图片集或艺人..."
            prefix-icon="el-icon-search"
            class="search-input"
            @keyup.enter="performSearch"
          ></el-input>
        </div>
      </section>
    </template>

    <script setup>
    import { ref } from 'vue';

    const searchQuery = ref('');

    const performSearch = () => {
      // 实现搜索逻辑
      console.log('搜索内容', searchQuery.value);
      // 根据searchQuery.value进行搜索
    };
    </script>

    <style scoped>
    .search-bar {
      padding: 20px;
      background-color: #f0ead6;
      text-align: center;
    }

    .search-container {
      display: inline-block;
      width: 100%;
      max-width: 600px;
    }

    .search-input {
      width: 100%;
      border: 1px solid #5c3a21;
      color: #5c3a21;
    }

    .el-input__inner {
      border-color: #5c3a21;
      color: #5c3a21;
    }

    .el-input__icon {
      color: #5c3a21;
    }
    </style>"""
    },
    {
        "moduleName": "页脚",
        "moduleEnName": "Footer",
        "designConcept": "提供网站的版权、联系方式和其他重要链接。",
        "function": "展示版权信息、联系方式、社交媒体链接等。",
        "layoutStyle": "采用复古怀旧风格的设计，简洁的布局中包含所有必要信息。",
        "imgStyle": "",
        "code": """<template>
      <footer class="site-footer">
        <div class="footer-content">
          <p>© 2024 VintageArt. All rights reserved.</p>
          <div class="footer-links">
            <a href="#" class="footer-link">Privacy Policy</a>
            <a href="#" class="footer-link">Terms of Service</a>
            <a href="#" class="footer-link">Contact Us</a>
          </div>
          <div class="social-media-icons">
            <el-link class="social-icon">

            </el-link>
            <el-link class="social-icon">

            </el-link>
            <el-link class="social-icon">

            </el-link>
          </div>
        </div>
      </footer>
    </template>

    <script setup>
    // No need to manually import Element Plus components as per the instruction.
    </script>

    <style scoped>
    .site-footer {
      padding: 20px;
      background-color: #f0ead6;
      text-align: center;
      color: #5c3a21;
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .footer-links {
      margin-top: 10px;
    }

    .footer-link {
      margin: 0 10px;
      color: #5c3a21;
      font-size: 16px;
      text-decoration: none;
    }

    .social-media-icons {
      margin-top: 20px;
    }

    .social-icon {
      font-size: 24px;
      color: #5c3a21;
      margin: 0 5px;
    }
    </style>"""
    }
]
current_module = {}


@app.route('/generate_components_info', methods=['POST'])
def generate_components_info():
    return jsonify({'success': True, 'data': modules_info})


@app.route('/generate_components', methods=['POST'])
def generate():
    global current_module
    generate_components("ImageCollectionPlatform", "HomePage", modules_info)
    for module in modules_info:
        current_module = module
        time.sleep(10)
        generate_component("ImageCollectionPlatform", "HomePage", module)
    return jsonify({'success': True, 'data': {}})


@app.route('/current_module', methods=['POST'])
def get_current_module():
    return jsonify({'success': True, 'data': current_module})


if __name__ == '__main__':
    app.run(port=5002, debug=True)
