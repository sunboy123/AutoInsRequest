<template>
  <div id="app" style="margin:0  auto" class="divcss">
    <el-form ref="elForm" :model="formData" :rules="rules" size="medium" label-width="100px" label-position="top" > 
      <el-form-item label="请求网址" prop="url">
        <el-input v-model="formData.url" placeholder="请输入请求网址" clearable :style="{width: '100%'}"></el-input>
      </el-form-item>
      <el-form-item label="请求方式" prop="method">
        <el-select v-model="formData.method" placeholder="请选择请求方式" clearable :style="{width: '40%'}">
          <el-option v-for="(item, index) in methodOptions" :key="index" :label="item.label"
            :value="item.label" :disabled="item.disabled"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="请求头" prop="request_header">
        <el-input v-model="formData.request_header" type="textarea" placeholder="请输入浏览器复制的以冒号分割的请求头参数"
          show-word-limit :autosize="{minRows: 10, maxRows: 10}" :style="{width: '100%'}"></el-input>
      </el-form-item>
      <el-form-item label="请求参数" prop="args">
        <el-input v-model="formData.args" type="textarea" placeholder="请输入请求参数以字典形式（可选）"
          :autosize="{minRows: 4, maxRows: 4}" :style="{width: '100%'}"></el-input>
      </el-form-item>

      <el-form-item label="语言选择" prop="language">
        <el-select v-model="formData.language" placeholder="请选择语言选择" clearable :style="{width: '20%'}">
          <el-option v-for="(item, index) in languageOptions" :key="index" :label="item.label"
            :value="item.label" :disabled="item.disabled"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="" prop="field103">
        <el-button type="success" icon="el-icon-sort" size="medium" @click="coonvertForm"> 转换 </el-button>
      </el-form-item>
      <el-form-item label="结果代码" prop="code_result">
        <el-input v-model="formData.code_result" type="textarea" :autosize="{minRows: 10, maxRows: 10}"
          :style="{width: '100%'}"></el-input>
      </el-form-item>
      <el-form-item size="large">
        <!-- <el-button type="primary" @click="submitForm">提交</el-button> -->
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios';
import Qs from 'qs'
export default {
  name: 'app',
  components: {},
  props: [],
  data() {
    return {
      formData: {
        url: "",//this.formData.url,
        method: "",//this.formData.method,
        request_header: "",//this.formData.request_header,
        language: "",//this.formData.language,
        field103: undefined,
        code_result: "",
        args : ""
      },
      rules: {
        url: [{
          required: true,
          message: '请输入请求网址',
          trigger: 'blur'
        }],
        method: [{
          required: true,
          message: '请选择请求方式',
          trigger: 'change'
        }],
        request_header: [{
          required: true,
          message: '请输入浏览器复制的以冒号分割的请求头参数',
          trigger: 'blur'
        }],
        language: [{
          required: true,
          message: '请选择语言选择',
          trigger: 'change'
        }],
        code_result: [{
          required: true,
          message: '',
          trigger: 'blur'
        }],
      },
      methodOptions: [{
        "label": "GET",
        "value": 1
      }, {
        "label": "POST",
        "value": 2
      }],
      languageOptions: [{
        "label": "python",
        "value": 1
      }, {
        "label": "java",
        "value": 2
      }],
    }
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {
    // submitForm() {
    //   this.$refs['elForm'].validate(valid => {
    //     if (!valid) return
    //     // TODO 提交表单
    //   })
    // },
    //重置所有表单内容
    resetForm() {
      this.$refs['elForm'].resetFields()
    },
    coonvertForm(){
      var reqData = JSON.stringify(this.formData)
      var apiUrl = 'http://192.168.7.135:9000/code'
      console.log(reqData)
      // 请求api 将 参数发送并重构 // Qs使用复杂数据进行传输 转换为urlencode 类型 Qs.stringify
      this.axios.post(apiUrl,
        JSON.stringify(this.formData),
        // {headers: {'Content-Type': 'application/json; charset=UTF-8'}}
        ).then(function (response) {
        console.log(response);
      }).catch(function (error){
        console.log(error);
      })
      // this.formData.code_result = 'hhahhhaha'
    }
  }
}

</script>
<style>
.divcss {
  border: 1px;
  width: 50%;
  height: auto;
  left: 50%;
  top: 50%;
}
</style>
