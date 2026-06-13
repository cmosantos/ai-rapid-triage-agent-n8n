import json
import unittest
from pathlib import Path


WORKFLOW_PATH = Path("workflow/ai-rapid-triage-agent.json")


class TestWorkflowTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = json.loads(WORKFLOW_PATH.read_text(encoding="utf-8"))
        cls.nodes = cls.workflow.get("nodes", [])
        cls.node_names = {node.get("name") for node in cls.nodes}
        cls.raw_text = WORKFLOW_PATH.read_text(encoding="utf-8")

    def test_workflow_has_expected_name(self):
        self.assertEqual(self.workflow.get("name"), "AI Rapid Triage Agent")

    def test_required_nodes_exist(self):
        expected = {
            "When chat message received",
            "AI Agent",
            "OpenAI Chat Model",
            "Code in JavaScript",
            "Append row in sheet",
            "Send a message",
            "Chat",
        }
        self.assertTrue(expected.issubset(self.node_names))

    def test_public_template_has_no_embedded_credentials(self):
        self.assertNotIn('"credentials"', self.raw_text)

    def test_public_template_uses_placeholders(self):
        self.assertIn("REPLACE_WITH_GOOGLE_SHEET_ID", self.raw_text)
        self.assertIn("analyst@example.com", self.raw_text)

    def test_workflow_is_inactive_by_default(self):
        self.assertFalse(self.workflow.get("active"))

    def test_connections_are_defined(self):
        connections = self.workflow.get("connections", {})
        self.assertIn("When chat message received", connections)
        self.assertIn("AI Agent", connections)
        self.assertIn("Code in JavaScript", connections)


if __name__ == "__main__":
    unittest.main()
