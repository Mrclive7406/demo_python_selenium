from fastapi import FastAPI
from backend_app.schemas.item_model import Item
import time
import threading
# from backend_app.core.config import settings
# from backend_app.api.routers import main_router

# from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI(
    # title=settings.app_title,
    # description=settings.app_description
)

# app.include_router(main_router)


EMPTY_ROUTERS = "/"
TEST_ROUTERS = "/test"


@app.get(EMPTY_ROUTERS)
async def read_root():
    return {"message": "Hello, World"}


@app.get(TEST_ROUTERS)
async def test_hendler():
    return {"message": "я тестовый"}


@app.post("/create-item/")
async def create_item(item: Item):
    return {"id": item.id, "name": item.name, "amount": item.amount}


def cron_job():
    while True:
        print("я крон")
        time.sleep(15)


# Запуск крон-задачи в отдельном потоке при старте приложения
def start_cron():
    thread = threading.Thread(target=cron_job, daemon=True)
    thread.start()


# Вызовем при запуске приложения
@app.on_event("startup")
async def startup_event():
    start_cron()

# scheduler = BackgroundScheduler
# scheduler.add_job(cron_job, "interval", seconds=60)
# scheduler.start
