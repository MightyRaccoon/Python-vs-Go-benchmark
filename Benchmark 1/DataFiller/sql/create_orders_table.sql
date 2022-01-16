BEGIN;

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    created_at TIMESTAMP,

    pickup_latitude DOUBLE PRECISION,
    pickup_longitude DOUBLE PRECISION,

    customer_latitude DOUBLE PRECISION,
    customer_longitude DOUBLE PRECISION
);

CREATE INDEX IF NOT EXISTS order_dttm ON orders (created_at);


COMMIT;