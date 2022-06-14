#!/usr/bin/env python3

""" スレッドを遅延起動する """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> None:
    logging.debug('start')
    time.sleep(secs)
    logging.debug('end')

def threading_08() -> None:
    logging.debug('start')

    # 3秒後に起動するスレッドを作成する
    thread = threading.Timer(interval=3, function=worker, args=(5,))

    # 実際には、この3秒後にスレッドが開始する
    thread.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_08()
