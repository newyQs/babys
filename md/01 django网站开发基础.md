# 第1章 Django网站开发基础

## 1.1 Django简史
django采用了MTV框架模式，即模型(Model)、模板(Template)和视图(View)，三者之间各自负责不同的职责：
```text
模型(Model)：数据存储层，处理数据相关的所有事务，例如如何存取，如何验证有效性，包含哪些行为以及数据之间的关系。
模板(Template)：表现层，处理与表现相关的决定，例如如何在页面或其他类型的文档中进行显示。
视图(View)：业务逻辑层，存储模型及调取恰当模块的相关逻辑，模型与模板的桥梁。
```

django具有如下特点：
```text
对象关系映射：
URL设计：
模板系统：
表单处理：
Cache系统
Auth认证系统：
国际化：
Admin后台系统：
```

## 1.2 Django和WSCI
WSGI(Web Server Gateway Interface)：**Web服务器网关接口**。
是Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口协议。
它是将Web服务器(如Apache或Nginx)的请求转发到后端Python Web应用程序或者Web框架。

Django、WSGI、Web服务器(如Apache或Nginx)之间的关系:
```text
Django是一个Web应用框架。WSGI是定义Web应用框架和Web服务器之间的通信协议。
一个完整的网站必须包含Web服务器，Web应用框架和数据库。
用户通过浏览器访问网址的时候，这个访问相当于向网站发送一个HTTP请求，
网站首先由Web服务器接收用户的HTTP请求，然后Web服务器通过WSGI将请求转发到Web应用框架进行处理，并得出处理结果。
Web应用框架通过WSGI将处理结果返回给Web服务器，最后由Web服务器将处理结果返回到用户的浏览器，用户即看到网页内容。
```

两种架构：
```text
客户端(HTTP请求) <--> WSGI Server (uWSGI, wsgiref) <--> WSGI Application

客户端(HTTP请求) <--> 代理服务器(Nginx) <--> WSGI Server (uWSGI, wsgiref) <--> WSGI Application
```

## 1.3 HTML、CSS和Javascript


## 1.4 搭建开发环境

1. pip install django

2. 下载.whl包，直接安装：pip install <filepath>


## 1.5 创建django项目

1. django-admin startproject <项目名>

项目文件说明：
+ manage.py：
+ asgi.py：
+ wsgi.py：
+ urls.py：
+ settings：

2. python manage.py startapp <app名称>

app文件说明：
+ migrations：
+ admin.py：
+ apps.py：
+ models.py：
+ tests.py：
+ views.py：

3. python manage.py runserver 0.0.0.0:8000

## 1.6 程序调试技巧


## 1.7 本章小结
