class DoctrineWorkflow:
    """
    Handles the workflow: ShadowGrid → Sentinel → User approval
    """
    def __init__(self, sentinel):
        self.pending = []
        self.sentinel = sentinel

    def submit(self, doctrine):
        self.pending.append(doctrine)

    def sentinel_review(self, doctrine):
        """
        Sentinel auto-checks doctrine
        Can be expanded for more rules
        """
        return True  # placeholder

    def user_approve(self, doctrine):
        doctrine.approved = True
        if doctrine in self.pending:
            self.pending.remove(doctrine)
