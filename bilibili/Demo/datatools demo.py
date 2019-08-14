from bilibili import datatools

#视频信息类
av_data=datatools.av_data() #首先实例化对象
info=av_data.get_av_info(63552232) #再获取完整的视频信息  该信息较大，解码时间可能较长1s+
res=av_data.get_coin(info) #这里传参不是视频id，而是上面完整的视频信息，主要考虑当需要获取多个信息时不重复爬取
print(res)
#av_data下其余get_xxx 方法用法与上相同



#视频评论类  因为评论可能较多，源码中采取每页延时0.3s处理
av_comments=datatools.comments_data() #首先实例化对象
reply_list=av_comments.get_reply_list(63552232,1)  #再获取完整的评论信息  参数（av号，评论页码）
reply_content_list=av_comments.get_reply_content(reply_list) #这里传参不是视频id，而是上面的评论信息，主要考虑不重复爬取
print(reply_content_list)

reply_user_list=av_comments.get_reply_user(reply_list) #用法与上类似
print(reply_user_list)




#视频弹幕类  因为一个视频下可能有多p，源码中采取每p延时0.3s处理
av_danmaku=datatools.danmaku_data()
danmaku_list=av_danmaku.get_danmaku_list(63552232)
print(danmaku_list)




#用户主页类

#1、投稿视频前100
author_page=datatools.authorpage_data()
author_vedios=author_page.get_author_video(15385187)
print(author_vedios)