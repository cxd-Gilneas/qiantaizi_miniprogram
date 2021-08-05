// pages/admin/admin.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    uncommitted: [],
    cuowei: [],
    sign_failed: [],
    tempFilePath: '',
    downloadwebsite: getApp().globalData.website + 'download',


    // 下载按钮相关值存储
    downloadbutton: true,

    // 弹窗相关值存储
    showSubmitDialog_start_true: false,
    showSubmitDialog_start_false: false,
    showSubmitDialog_check_true: false,
    showSubmitDialog_check_false: false,
    showSubmitDialog_export_true: false,
    showSubmitDialog_export_false: false,
    showSubmitDialog_download_true: false,
    oneButton: [{text: '确定'}],
  },

  // 本周开始签台子按钮的点击事件响应函数
  bindStart(e){
    wx.cloud.callFunction({
      name: 'qiantaizi_https',
      data: {
        url: getApp().globalData.website + 'admin',
        method: 'POST',
        data: {}
      }
    })
      .then(res => {
        console.log('成功', res);
        let result = JSON.parse(res.result)
        if(result.success){
          this.setData({  // 如果成功提交，那么出现弹窗
            showSubmitDialog_start_true: true
          })
        }
        else{
          this.setData({  // 如果提交失败，那么出现弹窗
            showSubmitDialog_start_false: true
          })
        }
      })
      .catch(res => {
        console.log('失败', res);
      })
  },

  // 核验是否有未签人员按钮的点击事件响应函数
  bindCheck(e){
    // wx.request({
    //   url: getApp().globalData.website + 'admin',
    //   method: 'GET',
    //   data: {},
    //   success:(result) => {
    //     console.log(result);
    //     if (result.data.success) {
    //       this.setData({
    //         uncommitted: result.data.data,
    //         showSubmitDialog_check_true: true,
    //       })
    //     }
    //     else {
    //       this.setData({
    //         showSubmitDialog_check_false: true
    //       })
    //     }
    //   }
    // })

    wx.cloud.callFunction({
      name: 'qiantaizi_https',
      data: {
        url: getApp().globalData.website + 'admin',
        method: 'GET',
        data: {}
      }
    })
      .then(res => {
        console.log('成功', res);
        let result = JSON.parse(res.result)
        if(result.success){
          this.setData({  // 如果成功提交，那么出现弹窗
            uncommitted: result.data,
            showSubmitDialog_check_true: true,
          })
        }
        else{
          this.setData({  // 如果提交失败，那么出现弹窗
            showSubmitDialog_check_false: true
          })
        }
      })
      .catch(res => {
        console.log('失败', res);
      })
  },

  // 输出本周签台子情况按钮的点击事件响应函数
  bindExport(e){
    // wx.request({
    //   url: getApp().globalData.website + 'admin',
    //   method: 'PUT',
    //   data: {},
    //   success:(result) => {
    //     console.log(result);
    //     if (result.data.success) {
    //       this.setData({
    //         cuowei: result.data.data[0],
    //         sign_failed: result.data.data[1],
    //         showSubmitDialog_export_true: true,
    //         downloadbutton: false
    //       })
    //     }
    //     else {
    //       this.setData({
    //         showSubmitDialog_export_false: true
    //       })
    //     }
    //   }
    // })

    wx.cloud.callFunction({
      name: 'qiantaizi_https',
      data: {
        url: getApp().globalData.website + 'admin',
        method: 'PUT',
        data: {}
      }
    })
      .then(res => {
        console.log('成功', res);
        let result = JSON.parse(res.result)
        if(result.success){
          this.setData({  // 如果成功提交，那么出现弹窗
            cuowei: result.data[0],
            sign_failed: result.data[1],
            showSubmitDialog_export_true: true,
            downloadbutton: false
          })
        }
        else{
          this.setData({  // 如果提交失败，那么出现弹窗
            showSubmitDialog_export_false: true
          })
        }
      })
      .catch(res => {
        console.log('失败', res);
      })
  },

  // 下载本周签台子表按钮的点击事件响应函数
  bindDownload(e){
    this.setData({
      showSubmitDialog_download_true: true,
    })
  },


  // 弹窗的确定按钮的点击事件响应函数
  tapDialogButton: function (e) {
    this.setData({
      showSubmitDialog_start_true: false,
      showSubmitDialog_start_false: false,
      showSubmitDialog_check_true: false,
      showSubmitDialog_check_false: false,
      showSubmitDialog_export_true: false,
      showSubmitDialog_export_false: false,
      showSubmitDialog_download_true: false
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