#!/usr/bin/env python3

""" スレッドに引数を渡す """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> None:
    logging.debug('start')
    time.sleep(secs)
    logging.debug('end')

def threading_02() -> None:
    logging.debug('start')

    # 引数を渡してスレッドを作成する
    thread_a = threading.Thread(target=worker, args=(10,))
    thread_b = threading.Thread(target=worker, args=( 5,))

    # スレッドを開始する
    thread_a.start()
    thread_b.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_02()
