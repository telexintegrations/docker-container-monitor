def sanitize_host_address(host: str) -> str:
    """
    Sanitizes the host address to ensure it starts with 'tcp://'.
    """
    if host.startswith(("http://", "https://")):
        # Replace http/https with tcp
        host = host.replace("http://", "tcp://").replace("https://", "tcp://")
    elif not host.startswith("tcp://"):
        # Add tcp:// prefix if missing
        host = f"tcp://{host}:2375"
    return host
