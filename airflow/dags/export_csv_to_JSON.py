import imp
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

PCW = imp.load_source('FileConverter', '../../python_csv_wrapper/csv_cheatsheet.py')
FILE_PATH = "test_files/payment_events_mock.csv"

default_args = {
    'owner': 'csioa',
    'depends_on_past': False,
    'start_date': datetime(2019, 6, 20),
    'retries': 3,
    'email_on_failure': False,
    'email_on_retry': False,
    'retry_delay': timedelta(minutes=10),
}


def read_headers(file_path):
    fc = PCW.FileConverter(file_path)
    print fc.get_headers()


def read_content(file_path):
    fc = PCW.FileConverter(file_path)
    print fc.file_to_dict_list()


with DAG(dag_id='csv_to_json',
         catchup=False,
         default_args=default_args) as dag:

    export_headers = PythonOperator(
        task_id='export_headers_task',
        provide_context=True,
        op_kwargs={
            'file_path': "FILE_PATH"
        },
        python_callable=read_headers,
        dag=dag
    )

    export_content = PythonOperator (
        task_id='export_content_task',
        provide_context=True,
        op_kwargs={
            'file_path': "FILE_PATH"
        },
        python_callable=read_content,
        dag=dag
    )

    export_headers >> export_content
