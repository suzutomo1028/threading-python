#!/usr/bin/env python3

""" スレッド間でデータを送受信する(Queue) """

import threading
import time
import queue
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker_a(que: queue.Queue) -> None:
    logging.debug('start')

    # キューにメッセージを格納する
    msg = 'hello, world'
    que.put(msg)
    logging.debug('put - %s', msg)

    time.sleep(1)

    # キューからメッセージを取得する
    msg = que.get()
    logging.debug('get - %s', msg)

    logging.debug('end')

def worker_b(que: queue.Queue) -> None:
    logging.debug('start')

    # キューからメッセージを取得する
    msg = que.get()
    logging.debug('get - %s', msg)

    # キューにメッセージを格納する
    msg = msg.upper()
    que.put(msg)
    logging.debug('put - %s', msg)

    logging.debug('end')

def threading_12() -> None:
    logging.debug('start')

    # スレッド間で共有のキューを作成する
    que = queue.Queue()

    thread_a = threading.Thread(name='Thread-A', target=worker_a, args=(que,))
    thread_b = threading.Thread(name='Thread-B', target=worker_b, args=(que,))

    thread_a.start()
    thread_b.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_12()
