#!/usr/bin/env python3

""" スレッド間でイベントを送受信する(Event) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker_a(evt: threading.Event) -> None:
    # イベントを待つ
    evt.wait()

    logging.debug('start')
    time.sleep(3)
    logging.debug('end')

def worker_b(evt: threading.Event) -> None:
    # イベントを待つ
    evt.wait()

    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker_c(evt: threading.Event) -> None:
    logging.debug('start')
    time.sleep(2)

    # イベントを発行する
    evt.set()

    logging.debug('end')

def threading_13() -> None:
    logging.debug('start')

    # スレッド間で共有のイベントを作成する
    evt = threading.Event()

    thread_a = threading.Thread(name='Thread-A', target=worker_a, args=(evt,))
    thread_b = threading.Thread(name='Thread-B', target=worker_b, args=(evt,))
    thread_c = threading.Thread(name='Thread-C', target=worker_c, args=(evt,))

    thread_a.start()
    thread_b.start()
    thread_c.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_13()
