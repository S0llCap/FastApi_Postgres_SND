CREATE TABLE adv_data.Events 
( ID BIGINT NOT NULL,
  Event_Date DATE NOT NULL,
  Event_Time TIME NOT NULL,
  Attribute1 BIGINT NULL,
  Attribute2 BIGINT NULL,
  Attribute3 BIGINT NULL,
  Attribute4 TEXT NULL,
  Attribute5 TEXT NULL,
  Attribute6 BOOLEAN NULL,
  Metric1 BIGINT NOT NULL,
  Metric2 DOUBLE PRECISION NOT NULL
  
)
PARTITION BY RANGE (Event_Date);
CREATE INDEX Metrics_IDX ON adv_data.Events (Metric1, Metric2);

CREATE TABLE adv_data.events_p20240201 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-01') TO ('2024-02-02');
CREATE TABLE adv_data.events_p20240202 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-02') TO ('2024-02-03');
CREATE TABLE adv_data.events_p20240203 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-03') TO ('2024-02-04');
CREATE TABLE adv_data.events_p20240204 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-04') TO ('2024-02-05');
CREATE TABLE adv_data.events_p20240205 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-05') TO ('2024-02-06');
CREATE TABLE adv_data.events_p20240206 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-06') TO ('2024-02-07');
CREATE TABLE adv_data.events_p20240207 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-07') TO ('2024-02-08');
CREATE TABLE adv_data.events_p20240208 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-08') TO ('2024-02-09');
CREATE TABLE adv_data.events_p20240209 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-09') TO ('2024-02-10');
CREATE TABLE adv_data.events_p20240210 PARTITION OF adv_data.Events
FOR VALUES FROM ('2024-02-10') TO ('2024-02-11');


GRANT select, insert, update ON all tables IN SCHEMA adv_data TO walle;