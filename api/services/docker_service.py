import docker
from docker.errors import DockerException
from fastapi import HTTPException, status


class DockerService:
    def get_container_status(self, host_address: str, container_id: str) -> dict:
        """
        Fetches the status of a Docker container using the provided Docker host URL.
        """
        try:
            client = docker.DockerClient(base_url=host_address)
            container = client.containers.get(container_id)
            health_status = (
                container.attrs.get("State", {}).get("Health", {}).get("Status", "N/A")
            )
            return {
                "container_id": container.id,
                "container_name": container.name,
                "status": container.status,
                "health_status": health_status,
            }
        except docker.errors.NotFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Error: Container with ID {container_id} not found",
            )
        except DockerException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Docker error: {str(e)}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unexpected error: {str(e)}",
            )
