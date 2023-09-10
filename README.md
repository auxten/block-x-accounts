# Twitter 账号批量屏蔽

## 介绍

Twitter 上有很多在热门帖子下面留言诈骗信息的账号，平时刷推突然出现让人非常尴尬。
这个困扰应该没有在英文圈，所以就直接写中文 README 了，不了解这个项目是干什么的就不用看了。

## 原理

使用 Selenium 模拟浏览器登录 Twitter，然后依次打开 blacklist.py 中列的账号主页，点击屏蔽按钮，最后退出。

## 使用方法

1. 安装 Python 3.8+，并安装依赖库：

    ```bash
    pip install -r requirements.txt
    ```

2. 【可选】修改 blacklist.py 文件，添加你想要屏蔽的账号。
3. 运行 main.py 文件，输入 Twitter 账号和密码，然后等待程序运行完毕。

    ```bash
    python3 main.py
    ```

## 注意事项

1. 作者私心，在最后加了一个关注 [@auxten](https://twitter.com/auxten) 的步骤，如果你不想关注，可以在 main.py 中注释掉。
2. 欢迎大家贡献账号，一起维护这个黑名单。你只需要把账号 ID （浏览器 URL 中的）添加到 blacklist.py 中即可。

## 需要帮助

1. 作者没有找到简单的在已有浏览器窗口打开 Twitter 的方法，所以只能劳烦大家在打开的 Chrome 窗口里登录 Twitter。
    如果有人知道怎么在已有浏览器窗口打开 Twitter，请告诉我，谢谢！