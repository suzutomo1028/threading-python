#!/usr/bin/env python3

""" スレッドに名前をつける """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> None:
    logging.debug('start')
    time.sleep(secs)
    logging.debug('end')

def threading_03() -> None:
    logging.debug('start')

    # 名前をつけてスレッドを作成する
    thread_a = threading.Thread(name='Thread-A', target=worker, args=(10,))
    thread_b = threading.Thread(name='Thread-B', target=worker, args=( 5,))

    # スレッドを開始する
    thread_a.start()
    thread_b.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_03()
