class Gas:
    def __init__(self, deployment_id: str):

        if not isinstance(deployment_id, str):
            raise TypeError("Deployment ID must be a string")

        self.deployment_id = deployment_id

    def do_example(self):
        print("I'm doing an example")

    def add_one(self, x):
        return x + 1
