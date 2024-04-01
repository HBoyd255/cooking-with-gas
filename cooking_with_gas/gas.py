class Gas:
    def __init__(self, deployment_id: str):

        if not isinstance(deployment_id, str):
            raise TypeError("Deployment ID must be a string")

        self._deployment_id = deployment_id

    def get_deployment_id(self) -> str:
        return self._deployment_id

    def get_url(self) -> str:
        return f"https://script.google.com/macros/s/{self._deployment_id}/exec"
