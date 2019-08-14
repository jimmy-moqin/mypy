from bilibili import download
#av号开头的都能下载，ep等bangumi类视频不可以
#搜索下载
search=download.search("妈咪叔")
download.av_download(search,1)
#av号下载
download.av_download(63344404)


#歌单下载
download.au_download("am22222")
#单曲下载
download.au_download("au33333")


#漫画下载暂时不提供