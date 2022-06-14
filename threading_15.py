#!/usr/bin/env python3

""" 他のスレッドが起動するまでスレッドの実行を待機する(Barrier) """

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(barr: threading.Barrier) -> None:
    # 他のスレッドの起動を待つ
    i = barr.wait()
    logging.debug('i = %d', i)

    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


def threading_15() -> None:
    logging.debug('start')

    # スレッド間で共有のバリアを作成する
    # （3つのスレッドの起動を待機）
    barr = threading.Barrier(3)

    for i in range(6):
        name = 'Thread-' + str(i)
        thread = threading.Thread(name=name, target=worker, args=(barr,))
        thread.start()

    logging.debug('end')

if __name__ == '__main__':
    threading_15()
