#!/usr/bin/env python3

""" スレッドを作成する """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker_a() -> None:
    logging.debug('start')
    time.sleep(10)
    logging.debug('end')

def worker_b() -> None:
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def threading_01() -> None:
    logging.debug('start')

    # スレッドを作成する
    thread_a = threading.Thread(target=worker_a)
    thread_b = threading.Thread(target=worker_b)

    # スレッドを開始する
    thread_a.start()
    thread_b.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_01()
