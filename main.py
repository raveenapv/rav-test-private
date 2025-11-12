from fastapi import FastAPI


app = FastAPI(title="Deployment Test Service")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/status")
async def status() -> dict[str, str]:
    return {
        "service": "deployment",
        "environment": "k8s",
        "status": "running",
    }

