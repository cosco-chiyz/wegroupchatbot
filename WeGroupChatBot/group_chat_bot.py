# coding: utf-8
import base64
import hashlib
import inspect
import os
from typing import Any, List

import requests
from requests import HTTPError
from six import string_types, BytesIO


def send(bot_key, msg_type, **body):
    raise_exception = body.pop('raise_exception', True)
    if bot_key is None or not isinstance(bot_key, string_types) or len(body) == 0:
        raise ValueError()
    if not bot_key.startswith('https://'):
        bot_key = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'.format(key=bot_key)
    r = requests.post(bot_key, json={"msgtype": msg_type, msg_type: body})
    if r.status_code != 200:
        exception = HTTPError('access WeGroupChatBot proxy is error,please check key!', response=r)
    else:
        response_data = r.json()
        if response_data['errcode'] == 0:
            return True
        exception = HTTPError(response_data['errmsg'], response=r, )
    if raise_exception and exception is not None:
        raise exception
    return False


def upload_file(bot_key, filepath):
    if bot_key is None or os.path.exists(filepath) is False:
        raise ValueError()
    _, filename = os.path.split(filepath)
    if not bot_key.startswith('https://'):
        bot_key = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file'.format(key=bot_key)
    with open(filepath, 'rb') as f:
        r = requests.post(bot_key, files={
            'media': (filename, f)
        })
    assert r.status_code == 200
    r_data = r.json()
    assert r_data['errcode'] == 0, r_data['errmsg']
    return r_data['media_id']


class WeGroupChatBot(object):
    """
        企业微信群机器人接口
    """

    def __init__(self, bot_key):
        """
            初始化群机器人
        :param bot_key: 机器人 Webhook url的key参数或webhook的url
        """
        super(WeGroupChatBot, self).__init__()
        self.bot_key = bot_key

    def send_text(self, content, mentioned_list=None, mentioned_mobile_list=None):
        """
            发送纯文本消息，支持相关人提醒功能
        :param content:  发送的文本
        :param mentioned_list:  userid的列表，提醒群中的指定成员(@某个成员)，
                @all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
        :param mentioned_mobile_list: 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
        :return:
        """
        return send(self.bot_key, 'text', content=content,
                    mentioned_list=mentioned_list,
                    mentioned_mobile_list=mentioned_mobile_list
                    )

    def send_markdown(self, content):
        """
            发送markdown格式的文本
        :param content: markdown 格式的文本
        :return:
        """
        return send(self.bot_key, 'markdown', content=content)

    def send_image(self, filename_or_fp):
        """
            发送图片消息

        :param filename_or_fp: 发送的图片文件路径或句柄,支持JPG、PNG,原图片最大不能超过2M
        :return:
        """
        is_auto_close = False
        if isinstance(filename_or_fp, string_types):
            filename_or_fp = open(filename_or_fp, 'rb')
            is_auto_close = True
        buffer = BytesIO()
        buffer.write(filename_or_fp.read())
        byte_data = buffer.getvalue()
        base64_str = repr(base64.b64encode(byte_data))[2:-1]
        md5 = hashlib.md5()
        md5.update(byte_data)
        if is_auto_close:
            filename_or_fp.close()
        return send(self.bot_key, 'image', base64=base64_str, md5=md5.hexdigest())

    def send_news(self, news):
        """
        发送一组图文消息
        :param news: 发送图文消息列表
          [
           {
               "title" : "中秋节礼品领取",
               "description" : "今年中秋节公司有豪礼相送",
               "url" : "URL",
               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
           }
        ]
        :return:
        """
        if not isinstance(news, (tuple, list)):
            news = [news]
        return send(self.bot_key, 'news', articles=news)

    def send_a_news(self, title, url, description=None, picurl=None):
        """
            发送一条图文消息

        :param title: 标题，不超过128个字节，超过会自动截断
        :param url: 点击后跳转的链接。
        :param description: 描述，不超过512个字节，超过会自动截断
        :param picurl: 图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068*455，小图150*150。
        :return:
        """
        return self.send_news({'title': title, 'url': url, 'description': description, 'picurl': picurl})

    def upload_file(self, filepath):
        """上传文件

        :param filepath: 上传文件的路径
        :return: media_id: 上传后，服务器返回的 media_id
        """
        return upload_file(self.bot_key, filepath)

    def send_file(self, filepath):
        media_id = self.upload_file(filepath)
        return self.send_media(media_id)

    def send_media(self, media_id):
        """
            发送文件
            消息内容格式如下：
            {
                "msgtype": "file",
                "file": {
                     "media_id": "3a8asd892asd8asd"
                }
            }

        :param media_id: media id,may be upload by upload_file
        :return:
        """
        return send(self.bot_key, msg_type='file', media_id=media_id)


def _make_bot_call_proxy(self, method):
    def method_proxy(*args, **kwargs):
        ret = [method(bot, *args, **kwargs) for bot in self._bots]
        return ret

    return method_proxy


class WeGroupChatBots(object):
    """multi bots batch work."""

    _bots = []

    def __new__(cls, *args, **kwargs) -> Any:
        self = object.__new__(cls)
        for name, method in WeGroupChatBot.__dict__.items():
            if name.startswith('__') or not inspect.isfunction(method):
                continue
            setattr(self, name, _make_bot_call_proxy(self, method))

        return self

    def __init__(self, *bot_key: List[str]) -> None:
        super().__init__()
        self._bots = []

        for key in bot_key:
            bot = WeGroupChatBot(key)
            self._bots.append(bot)
