

## 查询接口
### /common/表名称/方法 通用增删改查
方法如下：
* add
* delete
* update
* query
```javascript
axios.post(`/common/artist/query`, {orderby: [{"column": "id", "sort": 'desc'}]}).then(res => {
  artists.value = res.data
})
```
* page
```javascript
axios.post(`/common/artist/page`, {orderby: [{"column": "id", "sort": 'desc'}]}).then(res => {
  artists.value = res.data.items
})
```
### /save_form_config 保存
* 主表保存后的主键拿给子表保存更新使用
* 附表关联主表`id`字段命名规则为`主表名称` + `'_id'`
```javascript
const onSubmit = () => {
  const f = {
    "table": "image_collection", "form": {},
    "children": [{"table": "image", "form": {}}]
  }
  axios.post(`/save_form_config`, f).then(res => {
    mainId.value = res.id
    init()
  })
};
```
