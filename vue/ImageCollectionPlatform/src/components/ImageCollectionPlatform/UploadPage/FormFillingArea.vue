<template>
  <div class="form-filling-area">
    <el-form ref="form1" :model="form" label-width="120px" class="demo-form-inline">
      <el-form-item label="图片集标题">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input type="textarea" v-model="form.description"></el-input>
      </el-form-item>
      <el-form-item label="类别">
        <LSelect v-model="form.category_id" table="category" placeholder="请选择"></LSelect>
      </el-form-item>
      <el-form-item label="艺术家">
        <LSelect v-model="form.artist_id" table="artist" placeholder="请选择"></LSelect>
      </el-form-item>
      <el-form-item label="上传图片">
        <el-upload
            class="upload-demo"
            :action="`${BASE_URL}/upload`"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :on-success="handleSuccess"
            :file-list="fileList"
            drag
            multiple
            list-type="picture">
          <el-button size="small" type="primary">点击上传</el-button>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">发布</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import {inject, ref, reactive} from 'vue';
import {useRoute, useRouter} from "vue-router";
import {BASE_URL} from "@/config.js";
import LSelect from "@/components/common/form/LSelect.vue";

const router = useRouter()
const route = useRoute()

const form = ref({
  title: '',
  description: '',
  category_id: '',
  artist_id: '',
})
const axios = inject('$axios')

const fileList = ref([]);
const postList = ref([]);
const categoryList = ref([]);
const artistList = ref([]);

const mainId = ref(route.query['id'])

const init = () => {
  axios.post(`/common/image_collection/query`, {id: mainId.value}).then(res => {
    form.value = res.data[0]
  })
  axios.post(`/common/image/query`, {image_collection_id: mainId.value}).then(res => {
    fileList.value = res.data
    postList.value = res.data
  })
}


axios.post(`/common/artist/query`, {}).then(res => {
  artistList.value = res.data
})

axios.post(`/common/category/query`, {}).then(res => {
  categoryList.value = res.data
})


if (mainId.value) {
  init()
}
const handlePreview = file => {
  console.log('preview', file);
};

const handleRemove = (file, fileList) => {
  axios.post(`/common/image/delete`, {id: file.id}).then(res => {
    init()
  })
};
const handleSuccess = (response) => {
  postList.value.push({url: `${BASE_URL}/download/${response.uuid}`})
};

const onSubmit = () => {
  const f = {
    "table": "image_collection", "form": form.value,
    "children": postList.value.map(i => {
      return {"table": "image", "form": i}
    })
  }
  axios.post(`/save_form_config`, f).then(res => {
    mainId.value = res.id
    init()
  })
};
</script>

<style scoped>
.form-filling-area {
  font-family: 'Courier New', Courier, monospace;
  background-color: #f0ead6;
  padding: 20px;
  border-radius: 5px;
}

.el-form-item {
  margin-bottom: 20px;
}

.demo-form-inline .el-form-item {
  margin-right: 10px;
}

.el-button {
  background-color: #dcd0c0;
  border-color: #dcd0c0;
  color: #333;
}

.el-button:hover {
  background-color: #c4b395;
  border-color: #c4b395;
}

.el-input, .el-textarea__inner, .el-select {
  background-color: #fff;
  border-color: #dcd0c0;
}

.el-upload {
  border-color: #dcd0c0;
}
</style>