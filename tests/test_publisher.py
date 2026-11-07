import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from agentic_gh.publisher import PublisherEngine, PublishConfig

class TestPublisherEngine(unittest.TestCase):
    def test_badge_markdown_generation(self):
        cfg = PublishConfig(
            repo_name="test-repo",
            owner="Amz34",
            description="Testing publisher",
            topics=["ai", "test"],
            repo_path="."
        )
        engine = PublisherEngine(cfg)
        md = engine.generate_badge_markdown()
        self.assertIn("Amz34/test-repo", md)
        self.assertIn("License: MIT", md)

    def test_audit_secrets_clean(self):
        cfg = PublishConfig(
            repo_name="test-repo",
            owner="Amz34",
            description="Testing publisher",
            topics=["ai"],
            repo_path="/tmp"
        )
        engine = PublisherEngine(cfg)
        self.assertIsInstance(engine.audit_secrets(), bool)

if __name__ == "__main__":
    unittest.main()
