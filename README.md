# qiantaizi_miniprogram
这里是中国农业大学甘薯实验室签台子小程序的全部源代码，包括前端和后端。前端是基于微信开发平台，后端基于flask框架。

下面是这些文件主要的代码文件及其内容的介绍

------------

## 前端：qiantaizi_front_end
### 1 cloud 文件夹
  里面包含的是一个云函数qiantaizi_https，用于绕过微信小程序的访问限制（小程序只能访问https），通过云函数的服务器执行http访问该小程序的实际服务器
  注意：node.js需要安装并部署到云函数的服务器上，此处没有显示
### 2 app.js app.json project.config.json等文件
  小程序的全局配置文件
### 3 pages 文件夹
  小程序的主体代码，其中包括多个页面，如index、help、admin等，其js文件、wxml文件、wxss文件等都在其中
  
------------
  
## 后端：qiantaizi_back_end
该后端是基于flask框架搭建的，不过只是个半成品，勉强能用就上线了
### 1 flaskr 文件夹
  后端的主体代码
#### 1） __init__.py 文件
  基于flask框架的后端代码
#### 2） db.py 文件
  数据库的创建与连接代码
#### 3） qiantaizi_4.py 文件
  签台子功能实现的核心代码
#### 4） schema.sql 文件
  创建数据库的SQL语句

### 2 instance 文件夹
  用于存储实例

### 3 venv 文件夹
  后端的虚拟环境，主要需要安装flask、numpy、pandas、openpyxl包。另外，自己写的qiantaizi_4.py也需要放一份到虚拟环境包中
  
  
