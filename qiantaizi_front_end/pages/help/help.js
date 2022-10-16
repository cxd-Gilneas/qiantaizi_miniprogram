// pages/help/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    day_monitoring: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: 'http://ziaode.ren:5000/',
    //     method: 'GET',
    //     data: {}
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)
    //     this.setData({
    //       day_monitoring: result.data,
    //     })
    //   })
    //   .catch(res => {
    //     console.log('失败', res);
    //   })

    wx.request({
      url: 'https://ziaode.ren:5000/',
      method: 'GET',
      data: {},
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        this.setData({
         day_monitoring: result.data.data,
        });
      }
    })
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
    // wx.cloud.callFunction({
    //   name: 'qiantaizi_https',
    //   data: {
    //     url: 'http://ziaode.ren:5000/',
    //     method: 'GET',
    //     data: {}
    //   }
    // })
    //   .then(res => {
    //     console.log('成功', res);
    //     let result = JSON.parse(res.result)
    //     this.setData({
    //       day_monitoring: result.data,
    //     })
    //   })
    //   .catch(res => {
    //     console.log('失败', res);
    //   })

    wx.request({
      url: 'https://ziaode.ren:5000/',
      method: 'GET',
      data: {},
      header: {'content-type': 'application/json'},
      success:(result) => {
        console.log(result);
        this.setData({
         day_monitoring: result.data.data,
        });
      }
    })
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