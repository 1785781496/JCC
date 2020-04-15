

class DeployService:
    def __init__(self, customer=""):
        super(DeployService, self).__init__()
        self.customer = customer

    def get_product(self):
        return self.customer



if __name__ == '__main__':
    ds = DeployService()
