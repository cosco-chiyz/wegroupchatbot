WeGroupChatBot
====

group chat bot for Wechat of enterprise 企业微信群机器人接口

### usage:

### GroupChatBot
```python
#Init

from WeGroupChatBot import GroupChatBot
import os

# https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8a6b7936-06b1-4ada-ab66-f6389d78f053

bot = GroupChatBot('8a6b7936-06b1-4ada-ab66-f6389d78f053')

# send text

bot.send_text('hello world!')

# send markdown
bot.send_markdown('实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n'
                             '>类型:<font color=\"comment\">用户反馈</font> \n'
                             '>普通用户反馈:<font color=\"comment\">117例</font> \n'
                             '>VIP用户反馈:<font color=\"comment\">15例</font>'
                             )
                             
# send a news
bot.send_a_news('Red Alert 2',
                           'https://www.baidu.com/link?url'
                           '=7eniCd8AvgT6WmhCiBTdrZKSECWtPFL2dLrpLvooBWcNUaqc9OCnzF4mKQwh6T5zTlxhvle0GHhcsyzQseYfiveXHP'
                           'otyNJLxMgO9vbqtrCCWBj9iDce2TM0RrBJe_VVrug2O2kfd4jQo4phkmwOCJCY2Hnfp3nW9XmPjFZ9JtFK0YQfQvOpV'
                           '71I7Frhyz78uy8_0WU_Y7VFv6QwFJ_uWxIUVaj7DHRc6zWdVNpdl9vVCyOXxOvK-m9ayHiqEabq&wd=&eqid=b91f80'
                           'e90008d81e000000055d24a9bb',
                           picurl='https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign'
                                  '=7ec55f8b6263f624185d3e01b745eb32/caef76094b36acafa207424e75d98d1000e99c99.jpg')

                             

#send file 

bot.send_file(os.path.join(os.path.abspath(os.path.dirname(__file__)), './tests/2019.png'))


```

#### Bot groups
```python
from WeGroupChatBot import GroupChatBots
bots= GroupChatBots('a73c9432-24f6-419b-a643-70baae301d17', 'a73c9432-24f1-418b-a643-70baae301d17')

# send text

bots.send_text('hello world!')
```