// pages/dataentry/dataentry.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 学号、姓名的数据存储
    Name: '',
    studentID: '',

    // 弹窗相关值存储
    showSubmitDialog_true: false,
    showSubmitDialog_false: false,
    oneButton: [{text: '确定'}],
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

  // 提交按钮的点击事件响应函数
  bindSubmit(e){
    console.log(this.data.Name);
    console.log(this.data.studentID);
    wx.request({
      url: getApp().globalData.website,
      method: 'POST',
      data: {
        studentID: this.data.studentID,
        Name: this.data.Name
      },
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        if(result.data.success){
          this.setData({  // 如果成功提交，那么出现弹窗
            showSubmitDialog_true: true
          })
        }
        else{
          this.setData({  // 如果提交失败，那么出现弹窗
            showSubmitDialog_false: true
          })
        }
      }
    })

    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: getApp().globalData.website,
    //     method: 'POST',
    //     data: {
    //       studentID: this.data.studentID,
    //       Name: this.data.Name
    //     }
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)
    //     if(result.success){
    //       this.setData({  // 如果成功提交，那么出现弹窗
    //         showSubmitDialog_true: true
    //       })
    //     }
    //     else{
    //       this.setData({  // 如果提交失败，那么出现弹窗
    //         showSubmitDialog_false: true
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
      showSubmitDialog_true: false,
      showSubmitDialog_false: false
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