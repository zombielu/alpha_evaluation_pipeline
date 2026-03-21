from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator
from datetime import datetime

with DAG(
    dag_id="alpha_evaluation_pipeline",
    start_date=datetime(2026,3,19),
    schedule="@daily",
    catchup=False,
) as dag:
    task1 = EcsRunTaskOperator(
        task_id="run_ecs_pipeline",
        cluster="alpha_evaluation_cluster",
        task_definition="alpha_evaluation_task",
        launch_type="FARGATE",
        overrides={},  # 必须有
        network_configuration={
            "awsvpcConfiguration": {
                "subnets": [
                    "subnet-a90e3597",
                    "subnet-55629633"
                ],
                "securityGroups": ["sg-a5ce2e8b"],
                "assignPublicIp": "ENABLED"
            }
        }
    )