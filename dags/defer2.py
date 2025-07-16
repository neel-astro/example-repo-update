from airflow.decorators import dag
from pendulum import datetime
from airflow.sensors.date_time import DateTimeSensorAsync


@dag(
    start_date=datetime(2024, 5, 23, 20, 0),
    schedule="1 * * * *",
    catchup=False,
)
def async_dag_2():
    DateTimeSensorAsync(
        task_id="async_task",
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(seconds=30) }}""",
    )


async_dag_2()
