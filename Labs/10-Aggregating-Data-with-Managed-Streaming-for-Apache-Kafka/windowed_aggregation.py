from datetime import datetime, timedelta
from time import time
import random
import faust
import os
import json


class RawModel(faust.Record):
    date: datetime
    value: float


class AggModel(faust.Record):
    date: datetime
    count: int
    mean: float

TOPIC = 'raw_data'
SINK = 'aggregated_data'
TABLE = 'tumbling_table'
BROKER_STRING = os.environ['BROKER_STRING'].replace(',', ';')
KAFKA = 'kafka://' + BROKER_STRING
CLEANUP_INTERVAL = 1.0
WINDOW = 10
WINDOW_EXPIRES = 1
PARTITIONS = 1

app = faust.App('windowed-agg', broker=KAFKA, version=1, topic_partitions=PARTITIONS)

app.conf.table_cleanup_interval = CLEANUP_INTERVAL
source = app.topic(TOPIC, value_type=RawModel)
sink = app.topic(SINK, value_type=AggModel)

stream = app.stream(sink)

output_filename = "/home/ec2-user/output.json"

def window_processor(key, events):
    timestamp = key[1][0]
    values = [event.value for event in events]
    count = len(values)
    mean = sum(values) / count

    print(
        f'processing window:'
        f'{len(values)} events,'
        f'mean: {mean:.2f},'
        f'timestamp {timestamp}',
    )

    sink.send_soon(value=AggModel(date=timestamp, count=count, mean=mean))

tumbling_table = (
    app.Table(
        TABLE,
        default=list,
        partitions=PARTITIONS,
        on_window_close=window_processor,
    )
    .tumbling(WINDOW, expires=timedelta(seconds=WINDOW_EXPIRES))
    .relative_to_field(RawModel.date)
)

@app.agent(source)
async def print_windowed_events(stream):
    async for event in stream:
        value_list = tumbling_table['events'].value()
        value_list.append(event)
        tumbling_table['events'] = value_list

@app.timer(0.1)
async def produce():
    await source.send(value=RawModel(value=random.random(), date=int(time())))

@app.task
async def get_aggregated():
    with open(output_filename, "a+") as f:
        async for value in stream:
            print(f"Outputting aggregated event to {output_filename}")
            out_object = { 'date': value.date, 'mean': value.mean }
            f.write(json.dumps(out_object) + "\n")
            f.flush()


if __name__ == '__main__':
    app.main()