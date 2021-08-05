// 云函数入口文件
const cloud = require('wx-server-sdk')
//引入got用于做网络请求
var got = require('got');

cloud.init()

// 云函数入口函数
exports.main = async (event, context) => {
  let url = event.url;
  let data = event.data;

  if (event.method == 'GET'){
    let postResponse = await got(url, {
    method: event.method,
    headers:{'Content-Type': 'application/json'}
    });
    return postResponse.body;
  }
  else{
    let postResponse = await got(url, {
    method: event.method,
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(event.data)  // 将提交的信息转为字符串格式
    });
    return postResponse.body;
  }
}
