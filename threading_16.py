#!/usr/bin/env python3

""" スレッド固有のローカルデータを作成する(local) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker_a(local: threading.local) -> None:
    logging.debug('start')
    local.value = 100
    time.sleep(3)
    logging.debug('local.value = %d', local.value)
    logging.debug('end')

def worker_b(local: threading.local) -> None:
    logging.debug('start')
    local.value = 200
    time.sleep(1)
    logging.debug('local.value = %d', local.value)
    logging.debug('end')

def threading_16() -> None:
    logging.debug('start')

    # スレッド固有なローカルデータを作成する
    local = threading.local()

    thread_a = threading.Thread(name='Thread-A', target=worker_a, args=(local,))
    thread_b = threading.Thread(name='Thread-B', target=worker_b, args=(local,))

    thread_a.start()
    thread_b.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_16()
