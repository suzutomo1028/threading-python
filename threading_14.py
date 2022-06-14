#!/usr/bin/env python3

""" 条件によってスレッドの実行を排他する(Condition) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker_a(cond: threading.Condition) -> None:
    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with cond:
        # 条件が揃うまで待つ
        cond.wait()

        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

    # withを抜けると排他は解除される

def worker_b(cond: threading.Condition) -> None:
    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with cond:
        # 条件が揃うまで待つ
        cond.wait()

        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

    # withを抜けると排他は解除される

def worker_c(cond: threading.Condition) -> None:
    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with cond:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

        # 全てのスレッドに条件が揃ったことを通知する
        cond.notify_all()

    # withを抜けると排他は解除される

def threading_14() -> None:
    logging.debug('start')

    # スレッド間で共有のコンディションを作成する
    cond = threading.Condition()

    thread_a = threading.Thread(name='Thread-A', target=worker_a, args=(cond,))
    thread_b = threading.Thread(name='Thread-B', target=worker_b, args=(cond,))
    thread_c = threading.Thread(name='Thread-C', target=worker_c, args=(cond,))

    thread_a.start()
    thread_b.start()
    thread_c.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_14()
