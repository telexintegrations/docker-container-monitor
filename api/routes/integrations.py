from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/integration.json")
async def get_integration_json(request: Request):
    """Returns integration spec for integration with Telex"""
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {"created_at": "2025-02-18", "updated_at": "2025-02-18"},
            "descriptions": {
                "app_description": "Displays alerts for downtimes in docker containers",
                "app_logo": "https://ih1.redbubble.net/image.3865682305.9442/st,small,507x507-pad,600x600,f8f8f8.u1.jpg",
                "app_name": "Docker Container Monitor",
                "app_url": base_url,
                "background_color": "#ddd",
            },
            "integration_category": "Monitoring & Logging",
            "integration_type": "interval",
            "is_active": True,
            "key_features": ["Displays alerts for downtimes in docker containers"],
            "settings": [
                {
                    "label": "Remote Host Address",
                    "description": "Location of hosted docker container (DNS or IP Address)",
                    "type": "text",
                    "required": True,
                    "default": "",
                },
                {
                    "label": "Container ID",
                    "description": "The ID of container to monitor",
                    "type": "text",
                    "required": True,
                    "default": "",
                },
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "* * * * *",
                },
            ],
            "tick_url": f"{base_url}/tick",
            "target_url": "",
            "author": "David Enikuomehin",
        }
    }
