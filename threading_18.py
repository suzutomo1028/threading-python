#!/usr/bin/env python3

""" スレッドの戻り値を取得する(1) """

from concurrent.futures import ThreadPoolExecutor
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(secs: float) -> float:
    logging.debug('secs = %d', secs)
    time.sleep(secs)
    return secs

def threading_18() -> None:
    futures = []

    # スレッドプールを使って非同期にスレッドを呼び出す
    # 今回は同時にインスタンス化できるスレッドは3つ
    with ThreadPoolExecutor(3) as executor:
        for i in range(5):
            secs = random.randint(1, 5)
            
            # スレッドを開始して、戻り値を取得する
            # この時点ではスレッドの戻り値が入る future ができるだけ
            future = executor.submit(worker, secs)
            futures.append(future)

        # 実行済みスレッドの future から戻り値を取出す
        for future in futures:
            logging.debug('result = %d', future.result())

if __name__ == '__main__':
    threading_18()
