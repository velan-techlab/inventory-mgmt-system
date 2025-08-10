create table inventory (
    item_id int primary key,
    item_name varchar(100) not null,
    quantity int not null,
    price decimal(10, 2) not null
)

create Table sales_order (
    order_id int primary key,
    item_id int not null,
    order_date date not null,
    quantity int not null,
    foreign key (item_id) references inventory(item_id)
)

create Table purchase_order (
    purchase_id int primary key,
    item_id int not null,
    purchase_date date not null,
    quantity int not null,
    foreign key (item_id) references inventory(item_id)
)