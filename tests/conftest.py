import pytest

from WeGroupChatBot import GroupChatBot


@pytest.fixture()
def bot():
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8a6b7936-06b1-4ada-ab66-f6389d78f05e
    return GroupChatBot('8a6b7936-06b1-4ada-ab66-f6389d78f05e')
