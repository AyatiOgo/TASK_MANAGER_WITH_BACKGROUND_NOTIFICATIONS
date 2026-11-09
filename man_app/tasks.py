from celery import shared_task
import time


@shared_task(bind=True, max_retries=3)
def send_task_notification(self, task_id):

    try:
        print(f"Attempt {self.request.retries + 1}")

        # Simulate a temporary email service failure
        if self.request.retries < 2:
            raise ConnectionError("Email service temporarily unavailable")

        print(f"Notification sent for task {task_id}")

        return f"Notification sent for task {task_id}"

    except ConnectionError as exc:

        print("Notification failed. Retrying...")

        raise self.retry(
            exc=exc,
            countdown=5
        )