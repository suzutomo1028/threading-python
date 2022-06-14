#!/usr/bin/env python3

""" スレッドの実行を排他する(RLock) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

x = 0

def worker_a(lock: threading.RLock) -> None:
    global x

    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with lock:
        logging.debug('start')
        x += 1
        time.sleep(2)
        logging.debug('x = %d', x)
        logging.debug('end')

    # withを抜けると排他は解除される

def worker_b(lock: threading.RLock) -> None:
    global x

    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with lock:
        logging.debug('start')
        x += 1
        time.sleep(3)
        logging.debug('x = %d', x)
        logging.debug('end')

    # withを抜けると排他は解除される

def worker_c(lock: threading.RLock) -> None:
    global x

    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with lock:
        logging.debug('start')
        x += 1
        time.sleep(5)
        logging.debug('x = %d', x)
        logging.debug('end')

    # withを抜けると排他は解除される

def threading_10() -> None:
    logging.debug('start')

    # スレッド間で共有のロックを作成する
    lock = threading.RLock()

    thread_a = threading.Thread(name='Thread-A', target=worker_a, args=(lock,))
    thread_b = threading.Thread(name='Thread-B', target=worker_b, args=(lock,))
    thread_c = threading.Thread(name='Thread-C', target=worker_c, args=(lock,))

    thread_a.start()
    thread_b.start()
    thread_c.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_10()
