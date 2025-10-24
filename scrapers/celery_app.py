from celery import Celery
from celery.schedules import crontab
from config import settings

# Initialize Celery
celery_app = Celery(
    'coupon_scraper',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=['tasks']
)

# Celery configuration
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=600,  # 10 minutes max per task
    task_soft_time_limit=540,  # 9 minutes soft limit
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=50,
)

# Celery Beat schedule (runs hourly)
celery_app.conf.beat_schedule = {
    'scrape-all-stores-hourly': {
        'task': 'tasks.scrape_all_stores',
        'schedule': crontab(minute=0),  # Every hour at :00
    },
    'cleanup-expired-coupons-daily': {
        'task': 'tasks.cleanup_expired_coupons',
        'schedule': crontab(hour=2, minute=0),  # Daily at 2 AM
    },
    'reset-daily-limits-daily': {
        'task': 'tasks.reset_daily_limits',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
}

if __name__ == '__main__':
    celery_app.start()
