class InvocationRejected(Exception):
    """
    Raised when an invocation cannot be compiled
    into the CCBP framework.
    """

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason
