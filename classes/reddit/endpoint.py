#!/usr/bin/env python3
import logging
import praw
from classes.reddit.context import MentionContext
from classes.util import configuration

from praw.models.reddit.comment import Comment
from praw.models.reddit.message import Message


def comment_contains_username(comment: Comment):
    return Reddit.r.user.me().name in comment.body


class Reddit:
    # Static PRAW.reddit reference.  Define type for IDE integration.
    r = praw.Reddit(client_id="void", user_agent="void", client_secret="void")

    def __init__(self):
        raise NotImplementedError("The reddit class is not intended for instantiation.")

    @classmethod
    def login(cls):
        cls.r = praw.Reddit(user_agent=(
            'Generate an outcome for random tables, under the name'
            '/u/roll_one_for_me. Written and maintained by /u/PurelyApplied'),
            site_name="roll_one")

    @classmethod
    def logout(cls):
        del cls.r

    @staticmethod
    def beep_boop():
        """Builds and returns reply footer "Beep Boop I'm a bot...\""""
        s = "\n\n-----\n\n"
        s += ("*Beep boop I'm a bot.  " +
              "You can find usage and known issue details about me, as well as my source code, on " +
              "[GitHub](https://github.com/PurelyApplied/roll_one_for_me) page.  " +
              "I am written and maintained by /u/PurelyApplied.*\n\n"
              )
        s += "\n\n^(v{}; code base last updated {})".format(*configuration.get_version_and_updated())
        return s

    @classmethod
    def get_mentions(cls) -> "user-mention generator":
        return [msg for msg in cls.r.inbox.unread() if isinstance(msg, Comment) and comment_contains_username(msg)]

    @classmethod
    def get_private_messages(cls):
        return [msg for msg in cls.r.inbox.unread() if isinstance(msg, Message)]

    @classmethod
    def get_tables_from_mention(cls, mention):
        pass

    @classmethod
    def get_mention_context(cls, mention) -> MentionContext:
        logging.warning("get_mention_context is not implemented")
        return MentionContext({}, [])

if __name__ == "__main__":
    Reddit.login()
    pass
