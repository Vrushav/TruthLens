from src.scoring.trust_engine import TrustEngine
from src.analysis.issue_factory import IssueFactory


def test_score_calculation():

    engine = TrustEngine()

    issues = [IssueFactory.create("SEC001"), IssueFactory.create("RUN001")]

    result = engine.calculate(issues)

    assert result.trust_score == 50
    assert len(result.issues) == 2
    assert result.production_ready is False


def test_perfect_score():

    engine = TrustEngine()

    result = engine.calculate([])

    assert result.trust_score == 100
    assert result.production_ready is True
    assert len(result.issues) == 0
