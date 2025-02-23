import httpx
from fastapi import APIRouter, BackgroundTasks, HTTPException, status

from api.schemas.models import MonitorPayload
from api.services.docker_service import DockerService
from api.utils.helpers import sanitize_host_address

router = APIRouter()
docker_service = DockerService()


async def send_webhook(return_url: str, message: str, status: str = "success") -> None:
    """
    Sends a webhook notification to the provided return URL.
    """
    data = {
        "message": message,
        "username": "Docker Monitor",
        "event_name": "Server Status Check",
        "status": status,
    }
    async with httpx.AsyncClient() as client:
        await client.post(return_url, json=data)


async def monitor_task(payload: MonitorPayload):
    try:
        settings = {setting.label: setting.default for setting in payload.settings}
        host_address = settings.get("Remote Host Address")
        container_id = settings.get("Container ID")

        if not host_address or not container_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Both 'host_address' and 'container_id' are required. One or both are missing.",
            )

        docker_host = sanitize_host_address(host_address)

        container_status = docker_service.get_container_status(
            docker_host, container_id
        )

        message = (
            f"Container ID: {container_status['container_id']}\n"
            f"Container Name: {container_status['container_name']}\n"
            f"Status: {container_status['status']}\n"
            f"Health Status: {container_status['health_status']}"
        )

        await send_webhook(payload.return_url, message, status="success")

    except HTTPException as e:
        # Send error webhook
        await send_webhook(payload.return_url, str(e.detail), status="error")


@router.post("/tick", status_code=status.HTTP_202_ACCEPTED)
def monitor(payload: MonitorPayload, background_tasks: BackgroundTasks):
    background_tasks.add_task(monitor_task, payload)
    return {"status": "accepted"}
