from src.Result.case_result import CaseResult


class TestCaseResult:

    def test_success_representation(self):

        test_result = CaseResult("Angela_Merkel", "AKK", "AKK", True)

        assert str(test_result).startswith(CaseResult.PASSED_PREFIX)
        assert CaseResult.EXPECTED_OUTPUT_PREFIX not in str(test_result)

    def test_failure_representation(self):

        test_result = CaseResult("Angela_Merkel", "AKK", "Donald Trump", False)

        assert str(test_result).startswith(CaseResult.NOT_PASSED_PREFIX)
        assert CaseResult.EXPECTED_OUTPUT_PREFIX in str(test_result)