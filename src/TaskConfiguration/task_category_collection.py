import time


class TaskCategoryCollection:

    def __init__(self, categories):
        self.imported = time.time()
        self.categories = categories
