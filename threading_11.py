#!/usr/bin/env python3

""" スレッドの実行を排他する(Semaphore) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(sem: threading.Semaphore) -> None:
    # 他のスレッドの実行を排他する
    # 既に排他されていれば解除まで待機する
    with sem:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

    # withを抜けると排他は解除される

def threading_11() -> None:
    logging.debug('start')

    # スレッド間で共有のセマフォを作成する
    # （2つのスレッドが同時に実行できる）
    sem = threading.Semaphore(2)

    for i in range(5):
        name = 'Thread-' + str(i)
        thread = threading.Thread(name=name, target=worker, args=(sem,))
        thread.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_11()
