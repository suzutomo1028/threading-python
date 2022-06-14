#!/usr/bin/env python3

""" デーモンスレッドを作成する """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> None:
    logging.debug('start')
    time.sleep(secs)
    logging.debug('end')

def threading_04() -> None:
    logging.debug('start')

    # 名前をつけてスレッドを作成する
    thread_a = threading.Thread(name='Thread-A', target=worker, args=(10,))
    thread_b = threading.Thread(name='Thread-B', target=worker, args=( 5,))

    # スレッドをデーモン化する
    thread_a.daemon = True

    # スレッドを開始する
    thread_a.start()
    thread_b.start()

    # デーモンスレッドは、プログラムの終了と共に強制終了する
    # （今回のケースでは Thread-B の終了は保証されない）

    logging.debug('end')

if __name__ == '__main__':
    threading_04()
