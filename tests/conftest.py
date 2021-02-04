import pytest

from WeGroupChatBot import GroupChatBot
from WeGroupChatBot.group_chat_bot import WeGroupChatBots


@pytest.fixture()
def bot():
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a73c9432-24f6-419b-a643-70baae301d17

    return GroupChatBot('a73c9432-24f6-419b-a643-70baae301d17')


@pytest.fixture()
def bots():
    return WeGroupChatBots('a73c9432-24f6-419b-a643-70baae301d17', 'a73c9432-24f1-418b-a643-70baae301d17')
