import logging
import time
import requests
from colorlog import ColoredFormatter

import numpy as np
from argparse import ArgumentParser
from numpy.random import randint
from tqdm import tqdm


def setup_logger():
    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red",
        },
    )

    logger = logging.getLogger("example")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


def get_args():

    arg_parser = ArgumentParser()
    arg_parser.add_argument("--rows-count", required=True, type=int)

    return arg_parser.parse_args()


def main():

    logger = setup_logger()
    logger.info("Start")
    args = get_args()
    timings = []
    for i in tqdm(range(args.rows_count), desc="ReadData"):
        id = randint(low=0, high=1000000)
        start = time.time()
        response = requests.get(
            f"http://172.22.0.4:5000/order/{id}"
        )
        elapsed = time.time() - start
        timings.append(elapsed)

    logger.info("Metrics")
    logger.info({
        "AvgTime": np.mean(timings),
        "Median": np.median(timings),
        "P_min": np.min(timings),
        "P_90": np.percentile(timings, q=0.9),
        "P_95": np.percentile(timings, q=0.95),
        "P_99": np.percentile(timings, q=0.99),
        "P_max": np.max(timings),
        "Std": np.std(timings),
        "Total": np.sum(timings)
    })


if __name__ == "__main__":
    main()
