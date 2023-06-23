DROP TABLE IF EXISTS brands;
CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY,
    brand_name VARCHAR
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR
);


DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR,
    brand_id INTEGER,
    category_id INTEGER,
    model_year SMALLINT,
    list_price DECIMAL,
    CONSTRAINT fk_brands
        FOREIGN KEY(brand_id)
            REFERENCES brands(brand_id),

    CONSTRAINT fk_categories
        FOREIGN KEY(category_id)
            REFERENCES categories(category_id)
);

DROP TABLE IF EXISTS stocks;
CREATE TABLE stocks (
    store_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    CONSTRAINT fk_products
        FOREIGN KEY(product_id)
            REFERENCES products(product_id)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    street VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zip_code INTEGER
);

DROP TABLE IF EXISTS stores;
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    store_name VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    street VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zip_code INTEGER
);

DROP TABLE IF EXISTS staffs;
CREATE TABLE staffs (
    staff_id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    active BOOLEAN,
    store_id INTEGER,
    manager_id INTEGER,
    CONSTRAINT fk_stores
        FOREIGN KEY(store_id)
            REFERENCES stores(store_id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_status INTEGER,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    store_id INTEGER,
    staff_id INTEGER,
    CONSTRAINT fk_customers
        FOREIGN KEY(customer_id)
            REFERENCES customers(customer_id),
    CONSTRAINT fk_stores
        FOREIGN KEY(store_id)
            REFERENCES stores(store_id),
    CONSTRAINT fk_staffs
        FOREIGN KEY(staff_id)
            REFERENCES staffs(staff_id)
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    order_id INTEGER,
    item_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    list_price DECIMAL,
    discount DECIMAL,
    CONSTRAINT fk_orders
        FOREIGN KEY(order_id)
            REFERENCES orders(order_id),
    CONSTRAINT fk_products
        FOREIGN KEY(product_id)
            REFERENCES products(product_id)
);
