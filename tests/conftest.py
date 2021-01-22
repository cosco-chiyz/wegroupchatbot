import pytest

from WeGroupChatBot import GroupChatBot


@pytest.fixture()
def bot():
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a73c9432-24f6-419b-a643-70baae301d17

    return GroupChatBot('a73c9432-24f6-419b-a643-70baae301d17')
