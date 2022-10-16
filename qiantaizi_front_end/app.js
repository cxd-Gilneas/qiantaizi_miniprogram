//app.js
App({
  //onLaunch,onShow: options(path,query,scene,shareTicket,referrerInfo(appId,extraData))
  onLaunch: function(options){
    // 云开发环境的初始化
    // wx.cloud.init({
    //   env:"qiantaizi-8gc488bu0903f994"
    // })
  },
  onShow: function(options){

  },
  onHide: function(){

  },
  onError: function(msg){

  },
  //options(path,query,isEntryPage)
  onPageNotFound: function(options){

  },
  globalData: {
    website: 'https://ziaode.ren:5000/'
  }
});