// pages/user/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

    password: '',

    // 弹窗相关值存储
    showSubmitDialog: false,
    oneButton: [{text: '确定'}],
  },

  // 密码框的事件响应函数
  bindinputPassword: function(e) {
    console.log(e.detail.value)
    this.setData({
      password: e.detail.value
    })
  },

  // 登录按钮的事件响应函数
  bindLogin: function(e) {
    console.log(e.detail.value)
    wx.request({
      url: getApp().globalData.website + 'user',
      method: 'PUT',
      data: {
        password: this.data.password
      },
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        if (result.data.success) {
          wx.navigateTo({
            url: '/pages/admin/admin'
            })
        }
        else {
          this.setData({  // 如果密码错误，那么出现弹窗
            showSubmitDialog: true
          })
        }
      }
    })

    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: getApp().globalData.website + 'user',
    //     method: 'PUT',
    //     data: {
    //       password: this.data.password
    //     }
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)  // 将接口数据转为json格式
    //     if (result.success) {
    //       wx.navigateTo({
    //         url: '/pages/admin/admin'
    //         })
    //     }
    //     else {
    //       this.setData({  // 如果密码错误，那么出现弹窗
    //         showSubmitDialog: true
    //       })
    //     }
    //   })
    //   .catch(res => {
    //     console.log('失败', res);
    //   })
  },

  // 弹窗的确定按钮的点击事件响应函数
  tapDialogButton: function (e) {
    this.setData({
      showSubmitDialog: false
    })
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})