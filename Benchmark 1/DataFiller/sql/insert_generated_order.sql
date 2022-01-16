BEGIN;

INSERT INTO orders (order_id, created_at, pickup_latitude, pickup_longitude, customer_latitude, customer_longitude)
VALUES (:order_id, :created_at, :pickup_latitude, :pickup_longitude, :customer_latitude, :customer_longitude);

COMMIT;