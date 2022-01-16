from typing import Dict, Union

from flask import Flask, jsonify, Response
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["DEBUG"] = True

pg_engine = create_engine(
    'postgresql://{}:{}@{}:{}/{}'.format(
        "admin",
        "admin",
        "172.22.0.2",
        5432,
        "test"
    )
)


@app.route("/order/<int:order_id>", methods=["GET"])
def get_record_by_id(order_id: int) -> Response:
    """
    :param order_id Order ID
    """

    query = text("""
        SELECT
            *
        FROM
            orders
        WHERE
            order_id = :order_id
    """)
    try:
        raw_data = pg_engine.execute(
            query,
            order_id=order_id
        )
    except Exception as e:
        return jsonify({"Message": f"Error {e}"})

    parsed_data = [dict((key, value) for key, value in row.items()) for row in raw_data]

    if len(parsed_data) == 1:
        return jsonify(parsed_data)
    else:
        return jsonify(parsed_data[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

