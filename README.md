# goodmorning_my_brother
微信推送每日早安
最近微信公众平台每日的天气预报推送刷屏了

我也要给自己的好兄弟/好姐妹安排上。

详细步骤如下看我的这篇文章

### https://www.wolai.com/4RBguWyzkRT7vnFPdbtAXa

### 效果
![image](https://user-images.githubusercontent.com/102737052/186066900-d0f138f8-bb78-4c06-b84a-c89bd6c0f4c5.png)
## 8.24更新 关于早上8点没有自动推送的问题
今早打开手机发现早上并没有进行自动的推送，因此，我又对workflows分支下的做了一些更改(新建了一个pushmessage.yml)，目前已经提交.
目前测试已正常。
关于时间的设定，使用的是UTC时间，可以在.yml文件中进行更改，详细解释[这里](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#onschedule) ,关于UTC时间与北京时间的转换可以见[这里](https://datetime360.com/cn/beijing-utc-time/).
时间的设定在这里
![image](https://user-images.githubusercontent.com/102737052/186312094-1cbeed3d-5526-400a-834d-b122a611ae75.png)
更多详细还是在上面那篇文章
