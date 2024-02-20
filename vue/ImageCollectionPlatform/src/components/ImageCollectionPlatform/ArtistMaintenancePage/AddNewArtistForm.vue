<template>
  <div class="add-new-artist">
    <el-form ref="form1" :model="form" label-width="120px">
      <el-form-item label="艺人姓名">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <!--      <el-form-item label="艺术类别">-->
      <!--        <el-input v-model="form.category"></el-input>-->
      <!--      </el-form-item>-->
      <el-form-item label="艺人简介">
        <el-input type="textarea" v-model="form.bio"></el-input>
      </el-form-item>
      <el-form-item label="艺人照片">
        <el-upload
            class="upload-demo"
            :action="`${BASE_URL}/upload`"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :file-list="fileList"
            :on-success="handleSuccess"
            :limit="1"
            list-type="picture">
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import {inject, ref} from 'vue';
import {BASE_URL} from "@/config.js";

const artists = ref([]);
const axios = inject('$axios')


const form = ref({
  name: '',
  bio: '',
  artists_url: "",
});
const fileList = ref([]);

const handlePreview = file => {
  console.log('preview', file);
};

const handleRemove = (file, fileList) => {
  console.log('remove', file, fileList);
};

const handleSuccess = (response) => {
  form.value.artists_url = `${BASE_URL}/download/${response.uuid}`
};

const submitForm = () => {
  console.log('submit', form.value);
  // 在这里可以添加提交表单的逻辑
  axios.post(`/common/artist/add`, form.value).then(res => {
    artists.value = res.data
  })
};

const resetForm = () => {
  form.value = {
    name: '',
    bio: '',
    artists_url: '',
  };
  fileList.value = [];
};
</script>

<style scoped>
.add-new-artist {
  padding: 20px;
  background-color: #f9f5f0;
  color: #7a6248;
  font-family: "Times New Roman", Times, serif;
}

.el-form-item {
  margin-bottom: 25px;
}

.el-upload__tip {
  font-size: 14px;
  color: #7a6248;
}
</style>