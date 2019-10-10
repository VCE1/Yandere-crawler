import json
import Http
import Log


def get_json(page=1):
    """
    获取列表页的json数据
    :param page: 页码
    :type page: int
    :return: str
    """
    url = 'https://yande.re/post.json?page=' + str(page) #JSON API
    # tag搜索: url = 'https://yande.re/post.json?tags=' + str(tag)
    # WIP
    json_data = Http.get(url)
    if not json_data:
        Log.add('请求 ' + url + ' 失败')
        exit()

    try:
        json_data = json_data.decode('utf-8')
    except:
        Log.add(url + ' 解码失败')
        exit(500)
    return json_data


def get_li(json_data: str):
    """
    获取li数据列表
    :param json: json数组
    :type json: str
    :return: list
    """
    return json.loads(json_data)


def get_info(dic):
    """
    获取详情。即id,largeimgurl,width,height
    :param dic: json中单个post的数据
    :type dic: dictionary
    :return: list (id, size, ext, largeimg_url, width, height)
    """
    i = 0
    plist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jlist = ['id', 'file_size', 'file_ext', 'file_url', 'rating', 'status', 'width', 'height', 'score']
    # id file_size width height score为 int : 0,1,6,7,8
    # file_ext file_url rating status为 str : 2,3,4,5
    # score项目未使用
    # score的forum说明：“受欢迎程度”
    # 不需要下载原图的可以手动替换file_size file_url width height参数，体积与分辨率依次降低
    # Lastest JPG : jpeg_file_size jpeg_file_url jpeg_width jpeg_height
    # Sample Pic : sample_file_size sample_file_url sample_width sample_height
    for ele in jlist:
        plist[i] = dic[ele]
        i += 1
    plist[0] = str(plist[0])
    return plist
