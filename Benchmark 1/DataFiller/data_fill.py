import colorlog

from argparse import ArgumentParser

from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from utils import generate_row


handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(asctime)s - %(log_color)s%(levelname)-8s%(reset)s - %(blue)s%(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        reset=True,
        log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style="%"
    )
)

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)


def get_args():

    arg_parser = ArgumentParser()
    arg_parser.add_argument("--rows-count", required=True, type=int)

    return arg_parser.parse_args()


def main():

    logger.info("Data Creation Start")
    logger.info("Args parse")

    args = get_args()

    pg_engine = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(
            "admin",
            "admin",
            "0.0.0.0",
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

        for row_index in tqdm(range(args.rows_count)):
            row = generate_row(row_index)
            db_connection.execute(
                insert_order_query,
                order_id=row["order_id"],
                created_at=row["row_created_at"],
                pickup_latitude=row["pickup_latitude"],
                pickup_longitude=row["pickup_longitude"],
                customer_latitude=row["customer_latitude"],
                customer_longitude=row["customer_longitude"]
            )

        logger.info("Date Generation End")

    logger.info("Data Creation End")


if __name__ == "__main__":
    main()
