def test_send_text(bot):
    assert bot.send_text('hello world!')


def test_send_image(bot):
    import os

    assert bot.send_image(os.path.join(os.path.abspath(os.path.dirname(__file__)), '2019.png'))


def test_send_markdown(bot):
    assert bot.send_markdown('实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n'
                             '>类型:<font color=\"comment\">用户反馈</font> \n'
                             '>普通用户反馈:<font color=\"comment\">117例</font> \n'
                             '>VIP用户反馈:<font color=\"comment\">15例</font>'
                             )


def test_send_a_news(bot):
    assert bot.send_a_news('Red Alert 2',
                           'https://www.baidu.com/link?url'
                           '=7eniCd8AvgT6WmhCiBTdrZKSECWtPFL2dLrpLvooBWcNUaqc9OCnzF4mKQwh6T5zTlxhvle0GHhcsyzQseYfiveXHP'
                           'otyNJLxMgO9vbqtrCCWBj9iDce2TM0RrBJe_VVrug2O2kfd4jQo4phkmwOCJCY2Hnfp3nW9XmPjFZ9JtFK0YQfQvOpV'
                           '71I7Frhyz78uy8_0WU_Y7VFv6QwFJ_uWxIUVaj7DHRc6zWdVNpdl9vVCyOXxOvK-m9ayHiqEabq&wd=&eqid=b91f80'
                           'e90008d81e000000055d24a9bb',
                           picurl='https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign'
                                  '=7ec55f8b6263f624185d3e01b745eb32/caef76094b36acafa207424e75d98d1000e99c99.jpg')
