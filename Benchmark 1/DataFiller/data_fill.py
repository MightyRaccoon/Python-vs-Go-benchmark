import logging
import random
from colorlog import ColoredFormatter

from argparse import ArgumentParser
from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.exc import OperationalError

from utils import generate_row


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

    logger.info("Data Creation Start")
    logger.info("Args parse")

    args = get_args()

    pg_engine = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(
            "admin",
            "admin",
            "172.22.0.2",
            5432,
            "test"
        )
    )

    with pg_engine.connect() as db_connection:

        logger.info("Create Table with Generated Data")

        with open("sql/create_orders_table.sql", "r") as file:
            orders_table_query = file.read()

        db_connection.execute(text(orders_table_query))

        logger.info("Table Done")

        logger.info("Data Generation Start")
        with open("sql/insert_generated_order.sql", "r") as file:
            insert_order_query = text(file.read())

        indexes = list(range(args.rows_count))
        random.shuffle(indexes)

        for row_index in tqdm(indexes, desc="DataCreation"):
            row = generate_row(row_index)
            try:
                db_connection.execute(
                    insert_order_query,
                    order_id=row["order_id"],
                    created_at=row["row_created_at"],
                    pickup_latitude=row["pickup_latitude"],
                    pickup_longitude=row["pickup_longitude"],
                    customer_latitude=row["customer_latitude"],
                    customer_longitude=row["customer_longitude"]
                )
            except OperationalError as e:
                logger.error(e)
                break

        logger.info("Date Generation End")

    logger.info("Data Creation End")


if __name__ == "__main__":
    main()
