# -*- coding: utf-8 -*-
import time
import uuid
import cProfile
import pstats
import io
import re
import os
import threading
import traceback
from robot.Conversation import Conversation

from robot.LifeCycleHandler import LifeCycleHandler
from robot.Brain import Brain
from robot.Scheduler import Scheduler
from robot.sdk import History
from robot import (
    AI,
    ASR,
    config,
    constants,
    logging,
    NLU,
    Player,
    statistic,
    TTS,
    utils,
)


logger = logging.getLogger(__name__)


class ConversationManager(object):
    """
    对话管理器，用于管理多个历史对话
    """
    def __init__(self,profiling=False):
        self._profiling = profiling
        self.newOne = None
        self.conversation_cache = {}

    def newConversation(self):
        """
        新建一个对话
        """
        self.newOne = None
        con = Conversation(self._profiling)
        self.newOne = con
        self.conversation_cache[con.uuid]= con
        return con
    
    def getNewConversation(self):
        """
        获取最新创建的一个对话
        """
        return self.newOne
    
    def getConversation(self,uuid):
        """
        根据uuid获取历史对话
        """
        return self.conversation_cache.get(uuid,None)
    
