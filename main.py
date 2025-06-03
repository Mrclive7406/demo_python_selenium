from fastapi import FastAPI

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


# def cron_job():
#     print("я крон")


# scheduler = BackgroundScheduler
# scheduler.add_job(cron_job, "interval", seconds=60)
# scheduler.start
