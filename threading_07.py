#!/usr/bin/env python3

""" 複数のスレッドの終了を待つ """

import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> None:
    logging.debug('start')
    time.sleep(secs)
    logging.debug('end')

def threading_07() -> None:
    logging.debug('start')

    # 5つのスレッドを作成する
    for i in range(5):
        secs = random.randint(1, 9)
        name = 'Thread-' + str(i)

        thread = threading.Thread(name=name, target=worker, args=(secs,))
        thread.daemon = True
        thread.start()

    # 全てのスレッドの終了を待つ
    for thread in threading.enumerate():
        # 自身のスレッドは除外する
        if thread is threading.current_thread():
            continue
        thread.join()

    logging.debug('end')

if __name__ == '__main__':
    threading_07()
