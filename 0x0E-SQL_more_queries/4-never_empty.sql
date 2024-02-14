#!/usr/bin/bash

# Database name passed as and argument
hbtn_0d_2="$1"


# Create the id_not_null table
mysql -hlocalhost -uroot -p "hbtn_0d_2" <<EOF
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
EOF
