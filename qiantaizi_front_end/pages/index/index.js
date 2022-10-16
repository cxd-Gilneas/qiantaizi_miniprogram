//Page Object
Page({
  data: {
    // 学号、姓名的数据存储
    Name: '',
    studentID: '',
    Money: 99.99,
    qiantaizi_check: [],

    // 弹窗相关值存储
    showSubmitDialog: false,
    showSubmitDialog_message: '',
    showCheckDialog: false,
    oneButton: [{text: '确定'}],

    // picker 组件的数据存储
    multiArray1: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex1: [0, 0],
    multiArray2: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex2: [0, 0],
    multiArray3: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex3: [0, 0],
    multiArray4: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex4: [0, 0],
    multiArray5: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex5: [0, 0],
    multiArray6: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
    multiIndex6: [0, 0],
  },

  // 查看当前签台子情况的事件响应函数
  bindCheck: function(e) {
    console.log(this.data.Name);
    console.log(this.data.studentID);

    wx.request({
      url: getApp().globalData.website + 'check',
      method: 'PUT',
      data: {
        studentID: this.data.studentID,
        Name: this.data.Name
      },
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        this.setData({  // 如果成功提交，那么出现弹窗
          qiantaizi_check: result.data.data,
          showCheckDialog: true
        })
      }
    })

    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: getApp().globalData.website + 'check',
    //     method: 'PUT',
    //     data: {
    //       studentID: this.data.studentID,
    //       Name: this.data.Name
    //     }
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)  // 将接口数据转为json格式
    //     this.setData({  // 如果成功提交，那么出现弹窗
    //       qiantaizi_check: result.data,
    //       showCheckDialog: true
    //     })
    //   })
    //   .catch(res => {
    //     console.log('失败', res);
    //   })
  },

  // 存储学号框的事件响应函数
  bindinputstudentID: function(e) {
    console.log(e.detail.value)
    this.setData({
      studentID: e.detail.value
    })
  },

  // 存储姓名框的事件响应函数
  bindinputName: function(e) {
    console.log(e.detail.value)
    this.setData({
      Name: e.detail.value
    })
  },

  // 存储金钱框的事件响应函数
  bindinputMoney: function(e) {
    console.log(e.detail.value)
    this.setData({
      Money: e.detail.value
    })
  },  

  // 存储签的第一个台子的信息的事件响应函数
  bindMultiPickerChange1: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex1: e.detail.value
    })
  },
  // 这个事件响应函数的全部内容都是当某一列值发生滑动时带来连锁变化所需要的代码。如果没有连锁变化，就不用下列代码了
  bindMultiPickerColumnChange1: function (e) {  // 每当某一列的值发生滑动时触发
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  // 读取初始的数据
      multiArray1: this.data.multiArray1,
      multiIndex1: this.data.multiIndex1
    };
    data.multiIndex1[e.detail.column] = e.detail.value;  //每当某一列值发生滑动时，将滑动得到的值的索引返回给multiIndex的对应元素

    switch (e.detail.column) {  // 先看是哪一列发生了滑动
      case 0:
        switch (data.multiIndex1[0]) {  // 如果是第一列发生了滑动，看滑动得到的值是什么
          case 0:
            data.multiArray1[1] = ['无'];
            break;
          default:
            data.multiArray1[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },


  bindMultiPickerChange2: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex2: e.detail.value
    })
  },
  
  bindMultiPickerColumnChange2: function (e) {  
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  
      multiArray2: this.data.multiArray2,
      multiIndex2: this.data.multiIndex2
    };
    data.multiIndex2[e.detail.column] = e.detail.value;  

    switch (e.detail.column) {  
      case 0:
        switch (data.multiIndex2[0]) {  
          case 0:
            data.multiArray2[1] = ['无'];
            break;
          default:
            data.multiArray2[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },


  bindMultiPickerChange3: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex3: e.detail.value
    })
  },
  
  bindMultiPickerColumnChange3: function (e) {  
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  
      multiArray3: this.data.multiArray3,
      multiIndex3: this.data.multiIndex3
    };
    data.multiIndex3[e.detail.column] = e.detail.value;  

    switch (e.detail.column) {  
      case 0:
        switch (data.multiIndex3[0]) {  
          case 0:
            data.multiArray3[1] = ['无'];
            break;
          default:
            data.multiArray3[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },


  bindMultiPickerChange4: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex4: e.detail.value
    })
  },
  
  bindMultiPickerColumnChange4: function (e) {  
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  
      multiArray4: this.data.multiArray4,
      multiIndex4: this.data.multiIndex4
    };
    data.multiIndex4[e.detail.column] = e.detail.value;  

    switch (e.detail.column) {  
      case 0:
        switch (data.multiIndex4[0]) {  
          case 0:
            data.multiArray4[1] = ['无'];
            break;
          default:
            data.multiArray4[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },


  bindMultiPickerChange5: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex5: e.detail.value
    })
  },
  
  bindMultiPickerColumnChange5: function (e) {  
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  
      multiArray5: this.data.multiArray5,
      multiIndex5: this.data.multiIndex5
    };
    data.multiIndex5[e.detail.column] = e.detail.value;  

    switch (e.detail.column) {  
      case 0:
        switch (data.multiIndex5[0]) {  
          case 0:
            data.multiArray5[1] = ['无'];
            break;
          default:
            data.multiArray5[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },


  bindMultiPickerChange6: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex6: e.detail.value
    })
  },
  
  bindMultiPickerColumnChange6: function (e) {  
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {  
      multiArray6: this.data.multiArray6,
      multiIndex6: this.data.multiIndex6
    };
    data.multiIndex6[e.detail.column] = e.detail.value;  

    switch (e.detail.column) {  
      case 0:
        switch (data.multiIndex6[0]) {  
          case 0:
            data.multiArray6[1] = ['无'];
            break;
          default:
            data.multiArray6[1] = ['8：00~10：30', '12：00~14：30', '16：00~18：30', '20：00~22：30'];
            break;
        }
    }
    this.setData(data);
  },




  // 提交按钮的点击事件响应函数
  bindSubmit(e){
    console.log(this.data.Name);
    console.log(this.data.studentID);
    wx.request({
      url: getApp().globalData.website,
      method: 'PUT',
      data: {
        studentID: this.data.studentID,
        Name: this.data.Name,
        Money: this.data.Money,
        multiIndex1: this.data.multiIndex1,
        multiIndex2: this.data.multiIndex2,
        multiIndex3: this.data.multiIndex3,
        multiIndex4: this.data.multiIndex4,
        multiIndex5: this.data.multiIndex5,
        multiIndex6: this.data.multiIndex6,
      },
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        this.setData({  // 如果成功提交，那么出现弹窗
          showSubmitDialog_message: result.data.message,
          showSubmitDialog: true
        })
        wx.setStorage({  // 如果提交成功，那么缓存用户信息
          key: "userInfo",
          data: this.data
        })
      }
    })

    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: getApp().globalData.website,
    //     method: 'PUT',
    //     data: {
    //       studentID: this.data.studentID,
    //       Name: this.data.Name,
    //       Money: this.data.Money,
    //       multiIndex1: this.data.multiIndex1,
    //       multiIndex2: this.data.multiIndex2,
    //       multiIndex3: this.data.multiIndex3,
    //       multiIndex4: this.data.multiIndex4,
    //       multiIndex5: this.data.multiIndex5,
    //       multiIndex6: this.data.multiIndex6,
    //     }
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)
    //     this.setData({  // 如果成功提交，那么出现弹窗
    //       showSubmitDialog_message: result.message,
    //       showSubmitDialog: true
    //     })
    //     wx.setStorage({  // 如果提交成功，那么缓存用户信息
    //       key: "userInfo",
    //       data: this.data
    //     })
    //   })
    //   .catch(res => {
    //     console.log('失败', res);
    //   })
  },

  // 清空按钮的点击事件响应函数
  bindCleantable(e){
    this.setData({
      multiArray1: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex1: [0, 0],
      multiArray2: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex2: [0, 0],
      multiArray3: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex3: [0, 0],
      multiArray4: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex4: [0, 0],
      multiArray5: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex5: [0, 0],
      multiArray6: [['无', '周一', '周二', '周三', '周四', '周五', '周六', '周日'], ['无']],
      multiIndex6: [0, 0],
    })
  },

  // 弹窗的确定按钮的点击事件响应函数
  tapDialogButton: function (e) {
    this.setData({
      showSubmitDialog: false,
      showCheckDialog: false
    })
  },





  //options(Object)
  onLoad: function(e){  // 获取本机缓存数据
    var value = wx.getStorageSync('userInfo');
    if (value) {
      this.setData({  // 将本机缓存数据导入data
        Name: value.Name,
        studentID: value.studentID
      })
    }
  },
  onReady: function(){
    
  },
  onShow: function(){
    
  },
  onHide: function(){

  },
  onUnload: function(){

  },
  onPullDownRefresh: function(){

  },
  onReachBottom: function(){

  },
  onShareAppMessage: function(){

  },
  onPageScroll: function(){

  },
  //item(index,pagePath,text)
  onTabItemTap:function(item){

  }
});