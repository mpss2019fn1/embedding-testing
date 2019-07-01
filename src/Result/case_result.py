class CaseResult:
    PASSED_PREFIX = "✔"
    NOT_PASSED_PREFIX = "✖"

    ACTUAL_OUTPUT_PREFIX = "➔"
    EXPECTED_OUTPUT_PREFIX = "⚡"

    def __init__(self, test_input, expected_output, actual_output, passed):
        self.test_input = test_input
        self.expected_output = expected_output
        self.actual_output = actual_output
        self.passed = passed

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return print("\t")

    def print(self, indent):
        representation = f"{self.test_input} {CaseResult.ACTUAL_OUTPUT_PREFIX} {self.actual_output}"
        if self.passed:
            return indent + f"{CaseResult.PASSED_PREFIX}{representation}"
        else:
            return indent + f"{CaseResult.NOT_PASSED_PREFIX}{representation} {CaseResult.EXPECTED_OUTPUT_PREFIX} {self.expected_output}"
