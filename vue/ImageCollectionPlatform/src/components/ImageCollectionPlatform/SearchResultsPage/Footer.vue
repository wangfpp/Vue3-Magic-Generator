<template>
  <footer class="footer-wrapper">
    <div class="footer-content">
      <div class="footer-section">
        <h3>关于我们</h3>
        <p>这是一个复古风格的网站，旨在提供优质的内容和用户体验。</p>
      </div>
      <div class="footer-section">
        <h3>联系方式</h3>
        <p>邮箱：1764807112@qq.com</p>
        <p>Q Q：1764807112</p>
      </div>
      <div class="footer-section">
        <h3>快速链接</h3>
        <el-link type="primary" href="/ImageCollectionPlatform/HomePage">主页</el-link>
        <el-link type="primary" href="/ImageCollectionPlatform/SearchResultsPage">搜索</el-link>
        <el-link type="primary" href="#">账户管理</el-link>
      </div>
      <div class="footer-section">
        <h3>关注我们</h3>
        <el-image style="width: 24px; margin-right: 10px;" src="https://open.weixin.qq.com/zh_CN/htmledition/res/assets/res-design-download/icon64_appwx_logo.png" />
        <el-image style="width: 24px; margin-right: 10px;" src="https://wiki.connect.qq.com/wp-content/uploads/2013/10/03_qq_symbol-1-250x300.png" />
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2024 Vintage Style Web. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup>
import {TencentQq} from '@icon-park/vue-next';

import { ElLink, ElImage } from 'element-plus';
</script>

<style scoped>
.footer-wrapper {
  background-color: #f0ead6;
  color: #5c3a21;
  padding: 20px;
  text-align: center;
}

.footer-content {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.footer-section h3 {
  margin-bottom: 10px;
  color: #5c3a21;
}

.footer-section p, .footer-bottom p {
  color: #5c3a21;
  margin: 5px 0;
}

.footer-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer-bottom {
  border-top: 1px solid #c8b7a1;
  padding-top: 10px;
}

.el-link {
  display: block;
  margin: 5px 0;
}

.el-image {
  cursor: pointer;
}
</style>