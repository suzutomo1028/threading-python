#!/usr/bin/env python3

""" スレッドを継承したクラスを作成する """

from typing import Callable
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

class DownCounter(threading.Thread):

    def __init__(self, count: int, timeout_func: Callable, name: str) -> None:
        super().__init__(name=name)
        self.__count: int = count
        self.__timeout_func: Callable = timeout_func
        self.__stop: bool = False

    def run(self) -> None:
        count = self.__count
        while True:
            if count <= 0:
                self.__timeout_func()
                count = self.__count
            else:
                logging.debug('%d', count)
                count -= 1
            if self.__stop:
                logging.debug('stop!')
                break
            time.sleep(1)

    def stop(self) -> None:
        self.__stop = True

def timeout() -> None:
    logging.debug('timeout!')

def threading_17() -> None:
    thread = DownCounter(count = 10, timeout_func=timeout, name='DownCounter')
    thread.start()

    # 25秒たったら停止する
    time.sleep(25)
    thread.stop()

if __name__ == '__main__':
    threading_17()
