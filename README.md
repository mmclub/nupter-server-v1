# 掌上南邮V3 API Server V1

这是我们的掌上南邮V3最初版本的后台服务器，为掌上南邮背后的新闻模块等的JSON API请求提供服务。

## 广告

掌上南邮下载

[![Google Play](http://developer.android.com/images/brand/en_generic_rgb_wo_45.png)](https://play.google.com/store/apps/details?id=org.nupter.nupter)


[![Wandoujia](http://s.wdjimg.com/apps/images/logo_full.png)](http://www.wandoujia.com/apps/org.nupter.nupter)

![nupter](http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C785%3Bap%3D%C4%CF%BE%A9%D3%CA%B5%E7%B4%F3%D1%A7%B0%C9%2C90%2C793/sign=0b93f7ccb7003af34dbadc680511a52c/8634885494eef01f07690f00e1fe9925bd317d34.jpg)







## 技术结构

使用Python的Django框架编写。当初选择它的一个原因是因为它自带Admin模块。。可以偷懒不写后台。。。

四个API接口。具体可以见`nuptsite/urls.py`

- /news
- /jwc
- /newspaper
- /lost

分别给出校园新闻，教务新闻，团委手机报，失物招领的API

还有一个`/lost.html`,提供给合作的校学生会同学来查看并同步发布到人人主页上。不过后续沟通工作不好。。。然后就没有然后了


## 部署

请参见[部署笔记](http://jianshu.io/p/bNJWEs)

## 开源及发展

在一次VPS宕机之后，重新部署的时候，我花了一天用Ruby on Rails重写了Server，并一直跑到现在。所以老版本就开源吧。。。

此外，用Sinatra跑的爬取正方教务系统的另外一个Server也在测试中，会用于掌上南邮后续的版本中。

主要是出于安全性的考虑，我们的开源策略是，完成新版本的时候才将老版本的代码开源。






