class RuntimeErrorWithCode(Exception):  # Exception is the base
    """
    Exception raised when a specific error code is needed.
    """

    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = RuntimeErrorWithCode('An error occur.', 500)
print(err.__doc__)  # doc string will print the comments
