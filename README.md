<p align="center">
  <img src="assets/logo.svg" alt="Agentic GH Publisher Banner" width="800"/>
</p>

# Agentic GH Publisher

[![CI Quality Gate](https://github.com/Amz34/agentic-gh-publisher/actions/workflows/ci.yml/badge.svg)](https://github.com/Amz34/agentic-gh-publisher/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Security: Gitleaks](https://img.shields.io/badge/Security-Gitleaks%20Audited-purple.svg)](https://github.com/gitleaks/gitleaks)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

> **Autonomous, zero-leak enterprise GitHub repo scaffolder, CI/CD injector, and publisher engineered for AI agent worktrees.**

---

## The Tech Problem It Solves

When autonomous AI agent swarms produce codebases across local VMs, publishing them directly creates critical liabilities:
1. **Accidental Credential Exposure**: Agents dumping API keys or OAuth secrets into Git commit history.
2. **Unformatted Commits & Broken Presentation**: Missing standard license files, unverified commit signatures, and broken badges.
3. **Manual Overhead**: Developers spending hours hand-scaffolding CI/CD workflows and topics.

**`agentic-gh-publisher`** turns any raw agent folder into an enterprise-ready repository with an unbreakable Gitleaks gate, dynamic SVG badges, Semantic Release workflows, and GitHub API synchronization.

---

## Architectural Workflow
```
[Agent Workspace] ──> [Gitleaks AST Scan] ──> [CI/CD Injection] ──> [Conventional Commits] ──> [gh API Push]
```

---

## License
[MIT License](LICENSE) © 2026 Aamir Zahran
